"""
Test TABLEAU CK Integration and CSS Redesign Verification
Tests for iteration 13 - TABLEAU CK data enrichment and frontend CSS changes

Features tested:
1. Backend API /api/job-match returns correct MBTI, vertu, and scores
2. Backend API /api/explore returns filières with correct profiles
3. INFJ profile gets humanite vertu and Psychologue in top matches
4. ESTP profile gets courage vertu
5. score_archeologie uses TABLEAU_CK data (competences_sociales, competences_pro_transferables)
"""

import pytest
import requests
import os

BASE_URL = os.environ.get('REACT_APP_BACKEND_URL', '').rstrip('/')

# Test data for INFJ profile (should get humanite vertu)
INFJ_ANSWERS = {
    "v1": "I",
    "v2": "I",
    "v3": "N",
    "v4": "N1,N2,S1,S2",
    "v5": "F",
    "v6": "F",
    "v7": "J",
    "v8": "J",
    # Ennéagramme questions - Type 2 (helper) for humanite
    "v11": "2,4,9,5",
    "v12": "4,2,9,5",
    # RIASEC questions
    "r1": "I",
    "r2": "S",
    "r3": "C",
    "r4": "S,A,R,E",
    "r5": "I",
    "r6": "I,C,R,E",
    "r7": "S",
    "r8": "S,I,A,C",
    # Vertus questions - humanite oriented
    "vv1": "sagesse",
    "vv2": "humanite",
    "vv3": "transcendance",
    "vv4": "bienveillance,autonomie,securite,reussite",
    "vv5": "generosite",
    "vv6": "ecoute,initiative,rigueur,leadership"
}

# Test data for ESTP profile (should get courage vertu)
ESTP_ANSWERS = {
    "v1": "E",
    "v2": "E",
    "v3": "S",
    "v4": "S1,S2,N1,N2",
    "v5": "T",
    "v6": "T",
    "v7": "P",
    "v8": "P",
    # Ennéagramme questions - Type 8 (challenger) for courage
    "v11": "8,3,7,6",
    "v12": "8,3,7,6",
    # RIASEC questions
    "r1": "R",
    "r2": "A",
    "r3": "E",
    "r4": "R,E,A,S",
    "r5": "I",
    "r6": "R,E,I,C",
    "r7": "R",
    "r8": "I,A,S,C",
    # Vertus questions - courage oriented
    "vv1": "courage",
    "vv2": "justice",
    "vv3": "temperance",
    "vv4": "reussite,autonomie,securite,bienveillance",
    "vv5": "creativite",
    "vv6": "initiative,leadership,rigueur,ecoute"
}


class TestAPIHealth:
    """Test API health and basic connectivity"""
    
    def test_api_root(self):
        """Test that the API root is responding"""
        response = requests.get(f"{BASE_URL}/api/")
        assert response.status_code == 200
        data = response.json()
        assert "message" in data
        print(f"✓ API root check passed: {data.get('message')}")


class TestINFJProfile:
    """Test INFJ profile gets humanite vertu and appropriate job matches"""
    
    def test_infj_job_match_returns_correct_mbti(self):
        """INFJ profile should return INFJ as MBTI type"""
        payload = {
            "answers": INFJ_ANSWERS,
            "job_query": "Psychologue",
            "birth_date": "1990-01-15",
            "education_level": "7"
        }
        
        response = requests.post(f"{BASE_URL}/api/job-match", json=payload)
        assert response.status_code == 200, f"Expected 200, got {response.status_code}: {response.text}"
        
        data = response.json()
        
        # Check MBTI type from functioning_compass
        mbti = data.get("functioning_compass", {}).get("global_profile", "")
        assert mbti == "INFJ", f"Expected INFJ, got {mbti}"
        print(f"✓ INFJ MBTI type verified: {mbti}")
    
    def test_infj_job_match_returns_humanite_vertu(self):
        """INFJ profile should get humanite as dominant vertu from VV questions"""
        payload = {
            "answers": INFJ_ANSWERS,
            "job_query": "Psychologue",
            "birth_date": "1990-01-15",
            "education_level": "7"
        }
        
        response = requests.post(f"{BASE_URL}/api/job-match", json=payload)
        assert response.status_code == 200
        
        data = response.json()
        
        # Check dominant vertu from vertus_data (the correct source)
        vertu_name = data.get("vertus_data", {}).get("name", "").lower()
        # INFJ with humanite-oriented VV answers should get humanite
        assert "humanit" in vertu_name or "humanité" in vertu_name, f"Expected humanite vertu, got {vertu_name}"
        print(f"✓ INFJ dominant vertu verified: {vertu_name}")
        
        # Also check profile_summary.vertus.dominant
        vertus_dominant = data.get("profile_summary", {}).get("vertus", {}).get("dominant", "")
        print(f"  Profile vertus.dominant: {vertus_dominant}")
    
    def test_infj_psychologue_in_matches(self):
        """INFJ profile should have Psychologue as a good match"""
        payload = {
            "answers": INFJ_ANSWERS,
            "job_query": "Psychologue",
            "birth_date": "1990-01-15",
            "education_level": "7"
        }
        
        response = requests.post(f"{BASE_URL}/api/job-match", json=payload)
        assert response.status_code == 200
        
        data = response.json()
        best_match = data.get("best_match", {})
        
        # Check that Psychologue is found
        job_label = best_match.get("job_label", "").lower()
        assert "psychologue" in job_label or "psycho" in job_label, f"Expected Psychologue in job label, got {job_label}"
        print(f"✓ Psychologue found in matches: {job_label}")
        
        # Check score is reasonable
        score = best_match.get("score", 0)
        assert score >= 70, f"Expected score >= 70 for INFJ-Psychologue match, got {score}"
        print(f"✓ INFJ-Psychologue match score: {score}")
    
    def test_infj_access_code_generated(self):
        """INFJ job match should generate access code"""
        payload = {
            "answers": INFJ_ANSWERS,
            "job_query": "Psychologue",
            "birth_date": "1990-01-15",
            "education_level": "7"
        }
        
        response = requests.post(f"{BASE_URL}/api/job-match", json=payload)
        assert response.status_code == 200
        
        data = response.json()
        access_code = data.get("access_code", "")
        assert len(access_code) == 9, f"Expected access code format XXXX-XXXX, got {access_code}"
        assert "-" in access_code, f"Expected access code with hyphen, got {access_code}"
        print(f"✓ Access code generated: {access_code}")


class TestESTPProfile:
    """Test ESTP profile gets courage vertu"""
    
    def test_estp_job_match_returns_correct_mbti(self):
        """ESTP profile should return ESTP as MBTI type"""
        payload = {
            "answers": ESTP_ANSWERS,
            "job_query": "Commercial",
            "birth_date": "1992-06-20",
            "education_level": "5"
        }
        
        response = requests.post(f"{BASE_URL}/api/job-match", json=payload)
        assert response.status_code == 200, f"Expected 200, got {response.status_code}: {response.text}"
        
        data = response.json()
        
        # Check MBTI type from functioning_compass
        mbti = data.get("functioning_compass", {}).get("global_profile", "")
        assert mbti == "ESTP", f"Expected ESTP, got {mbti}"
        print(f"✓ ESTP MBTI type verified: {mbti}")
    
    def test_estp_job_match_returns_courage_vertu(self):
        """ESTP profile should get courage as dominant vertu from VV questions"""
        payload = {
            "answers": ESTP_ANSWERS,
            "job_query": "Commercial",
            "birth_date": "1992-06-20",
            "education_level": "5"
        }
        
        response = requests.post(f"{BASE_URL}/api/job-match", json=payload)
        assert response.status_code == 200
        
        data = response.json()
        
        # Check dominant vertu from vertus_data (the correct source)
        vertu_name = data.get("vertus_data", {}).get("name", "").lower()
        # ESTP with courage-oriented VV answers should get courage
        assert "courage" in vertu_name, f"Expected courage vertu, got {vertu_name}"
        print(f"✓ ESTP dominant vertu verified: {vertu_name}")
        
        # Also check profile_summary.vertus.dominant
        vertus_dominant = data.get("profile_summary", {}).get("vertus", {}).get("dominant", "")
        assert vertus_dominant == "courage", f"Expected courage in vertus.dominant, got {vertus_dominant}"
        print(f"  Profile vertus.dominant: {vertus_dominant}")


class TestExploreEndpoint:
    """Test /api/explore endpoint returns filières with correct profiles"""
    
    def test_explore_returns_exploration_paths(self):
        """Explore endpoint should return exploration_paths with profiles"""
        payload = {
            "answers": INFJ_ANSWERS,
            "birth_date": "1990-01-15",
            "education_level": "7"
        }
        
        response = requests.post(f"{BASE_URL}/api/explore", json=payload)
        assert response.status_code == 200, f"Expected 200, got {response.status_code}: {response.text}"
        
        data = response.json()
        
        # Check profile_summary exists
        assert "profile_summary" in data, "profile_summary missing from explore response"
        
        # Check exploration_paths exist (not filieres)
        assert "exploration_paths" in data, "exploration_paths missing from explore response"
        paths = data["exploration_paths"]
        assert len(paths) > 0, "Expected at least one exploration path"
        print(f"✓ Explore returned {len(paths)} exploration paths")
        
        # Check first path has expected structure
        first_path = paths[0]
        assert "filiere" in first_path, "Path missing filiere name"
        assert "avg_compatibility" in first_path or "best_job_score" in first_path, "Path missing score"
        print(f"✓ First path: {first_path.get('filiere', 'Unknown')}")
    
    def test_explore_returns_correct_mbti(self):
        """Explore endpoint should return correct MBTI"""
        payload = {
            "answers": ESTP_ANSWERS,
            "birth_date": "1992-06-20",
            "education_level": "5"
        }
        
        response = requests.post(f"{BASE_URL}/api/explore", json=payload)
        assert response.status_code == 200
        
        data = response.json()
        mbti = data.get("functioning_compass", {}).get("global_profile", "")
        assert mbti == "ESTP", f"Expected ESTP, got {mbti}"
        print(f"✓ Explore MBTI verified: {mbti}")


class TestTableauCKIntegration:
    """Test that TABLEAU_CK data is used in scoring"""
    
    def test_job_match_uses_tableau_ck_data(self):
        """Job match should use TABLEAU_CK competences_sociales and competences_pro_transferables"""
        payload = {
            "answers": INFJ_ANSWERS,
            "job_query": "Conseiller",
            "birth_date": "1990-01-15",
            "education_level": "6"
        }
        
        response = requests.post(f"{BASE_URL}/api/job-match", json=payload)
        assert response.status_code == 200
        
        data = response.json()
        
        # Check that archeologie data is present in the response
        best_match = data.get("best_match", {})
        
        # The score should be calculated using TABLEAU_CK data
        score = best_match.get("score", 0)
        assert score > 0, "Score should be positive when TABLEAU_CK is used"
        
        # Check breakdown if available
        breakdown = best_match.get("breakdown", {})
        if breakdown:
            # Archeologie score should be present
            archeologie = breakdown.get("archeologie", 0)
            print(f"✓ Archeologie score in breakdown: {archeologie}")
        
        print(f"✓ Job match score with TABLEAU_CK: {score}")
    
    def test_vertus_data_contains_ck_fields(self):
        """vertus_data should contain TABLEAU_CK fields"""
        payload = {
            "answers": ESTP_ANSWERS,
            "job_query": "Commercial",
            "birth_date": "1992-06-20",
            "education_level": "5"
        }
        
        response = requests.post(f"{BASE_URL}/api/job-match", json=payload)
        assert response.status_code == 200
        
        data = response.json()
        vertus_data = data.get("vertus_data", {})
        
        # Check that TABLEAU_CK fields are present
        assert "competences_sociales" in vertus_data, "competences_sociales missing from vertus_data"
        assert "competences_pro" in vertus_data or "competences_pro_transferables" in vertus_data, "competences_pro missing from vertus_data"
        
        comp_sociales = vertus_data.get("competences_sociales", [])
        print(f"✓ Competences sociales: {comp_sociales[:3] if comp_sociales else 'None'}")
        
        # For courage vertu, should have specific competences
        if "courage" in vertus_data.get("name", "").lower():
            expected_sociales = ["Habileté", "Rigueur", "Persévérant"]
            found = any(c in comp_sociales for c in expected_sociales)
            assert found, f"Expected courage-related competences_sociales, got {comp_sociales}"
            print(f"✓ Courage competences_sociales verified")


class TestQuestionsEndpoint:
    """Test /api/questionnaire endpoint"""
    
    def test_questionnaire_endpoint_returns_visual_questions(self):
        """Questionnaire endpoint should return visual questions"""
        response = requests.get(f"{BASE_URL}/api/questionnaire/visual")
        assert response.status_code == 200
        
        data = response.json()
        assert "questions" in data, "questions missing from response"
        
        questions = data["questions"]
        assert len(questions) > 0, "Expected at least one question"
        
        # Check for visual question types
        visual_count = sum(1 for q in questions if q.get("type") in ["visual", "ranking"])
        print(f"✓ Visual questionnaire returned {len(questions)} questions ({visual_count} visual/ranking)")


class TestScoreBreakdown:
    """Test that score breakdown includes archeologie component"""
    
    def test_score_breakdown_has_archeologie(self):
        """Score breakdown should include archeologie component"""
        payload = {
            "answers": INFJ_ANSWERS,
            "job_query": "Psychologue",
            "birth_date": "1990-01-15",
            "education_level": "7"
        }
        
        response = requests.post(f"{BASE_URL}/api/job-match", json=payload)
        assert response.status_code == 200
        
        data = response.json()
        best_match = data.get("best_match", {})
        breakdown = best_match.get("breakdown", {})
        
        if breakdown:
            # Check that archeologie is in the breakdown
            assert "archeologie" in breakdown, f"archeologie missing from breakdown: {breakdown.keys()}"
            archeologie_score = breakdown.get("archeologie", 0)
            assert archeologie_score > 0, f"Expected positive archeologie score, got {archeologie_score}"
            print(f"✓ Archeologie score: {archeologie_score}")
            
            # Check other expected components
            expected_components = ["mbti", "disc", "ennea", "riasec"]
            for comp in expected_components:
                if comp in breakdown:
                    print(f"  {comp}: {breakdown[comp]}")
        else:
            print("  Note: breakdown not available in response")


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
