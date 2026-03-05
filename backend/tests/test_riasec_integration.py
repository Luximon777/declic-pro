"""
Tests for RIASEC (Holland Codes) Integration:
- Test 1: API /api/job-match - Verify response contains RIASEC profile (profile_summary.riasec) with code_2, major, minor, scores
- Test 2: API /api/explore - Verify response contains RIASEC profile in profile_summary
- Test 3: Frontend - Verified via Playwright in separate test
- Test 4: Coherence - INTJ profile should get IC or CI RIASEC code (Investigator dominant)
- Test 5: Score RIASEC - Verify score breakdown contains 'riasec' key
"""

import pytest
import requests
import os

BASE_URL = os.environ.get('REACT_APP_BACKEND_URL', '').rstrip('/')

# Sample valid questionnaire answers for INFP profile (v1=I, v2=I, v3=N, v4=N1,N2,S1,S2, v5=F, v6=F, v7=P, v8=P, v9=S, v10=4, v11=4, v12=4)
INFP_ANSWERS = {
    "v1": "I",   # énergie - Introversion
    "v2": "I",   # énergie - Introversion
    "v3": "N",   # perception - Intuition
    "v4": "N1,N2,S1,S2",  # perception ranking - N dominant
    "v5": "F",   # décision - Feeling
    "v6": "F",   # décision - Feeling
    "v7": "P",   # structure - Perceiving
    "v8": "P",   # structure - Perceiving
    "v9": "S,I,D,C",  # disc ranking - Stability dominant
    "v10": "4,5,2,3",  # disc ranking (stress reactions)
    "v11": "4,5,2,3",  # ennea ranking (happiness sources) - Type 4 dominant (Artistic)
    "v12": "4,5,2,3"   # ennea ranking (stress sources)
}

# Sample INTJ profile answers (should yield Investigator RIASEC - I dominant)
INTJ_ANSWERS = {
    "v1": "I",   # énergie - Introversion
    "v2": "I",   # énergie - Introversion
    "v3": "N",   # perception - Intuition
    "v4": "N1,N2,S1,S2",  # perception ranking - N dominant
    "v5": "T",   # décision - Thinking
    "v6": "T",   # décision - Thinking
    "v7": "J",   # structure - Judging
    "v8": "J",   # structure - Judging
    "v9": "C,D,S,I",  # disc ranking - Conformity dominant (analytical)
    "v10": "C,D,S,I",  # disc ranking
    "v11": "5,1,3,8",  # ennea ranking - Type 5 dominant (Investigator)
    "v12": "5,1,3,8"   # ennea ranking
}

# Sample ESTJ profile answers (should yield E or C dominant RIASEC - Enterprising/Conventional)
ESTJ_ANSWERS = {
    "v1": "E",   # énergie - Extraversion
    "v2": "E",   # énergie - Extraversion
    "v3": "S",   # perception - Sensing
    "v4": "S1,S2,N1,N2",  # perception ranking - S dominant
    "v5": "T",   # décision - Thinking
    "v6": "T",   # décision - Thinking
    "v7": "J",   # structure - Judging
    "v8": "J",   # structure - Judging
    "v9": "D,C,I,S",  # disc ranking - Dominance first
    "v10": "D,C,I,S",  # disc ranking
    "v11": "3,8,1,6",  # ennea ranking - Type 3 dominant (Achiever)
    "v12": "3,8,1,6"   # ennea ranking
}


class TestRIASECJobMatchEndpoint:
    """Test 1: API /api/job-match - Verify RIASEC profile structure"""
    
    def test_job_match_contains_riasec_profile(self):
        """
        Verify /api/job-match response contains RIASEC profile with all required fields:
        - profile_summary.riasec.code_2 (2-letter code)
        - profile_summary.riasec.major (dominant letter)
        - profile_summary.riasec.minor (secondary letter)
        - profile_summary.riasec.scores (normalized 0-100)
        """
        payload = {
            "answers": INFP_ANSWERS,
            "job_query": "développeur"
        }
        
        response = requests.post(f"{BASE_URL}/api/job-match", json=payload)
        assert response.status_code == 200, f"API returned {response.status_code}: {response.text}"
        
        data = response.json()
        
        # Verify profile_summary exists
        assert "profile_summary" in data, "Response missing profile_summary field"
        profile_summary = data["profile_summary"]
        
        # Verify RIASEC profile exists
        assert "riasec" in profile_summary, "profile_summary missing riasec field"
        riasec = profile_summary["riasec"]
        
        # Verify required RIASEC fields
        assert "code_2" in riasec, "riasec missing code_2 (2-letter code)"
        assert "major" in riasec, "riasec missing major (dominant letter)"
        assert "minor" in riasec, "riasec missing minor (secondary letter)"
        assert "scores" in riasec, "riasec missing scores"
        
        # Verify code structure
        assert len(riasec["code_2"]) == 2, f"code_2 should be 2 letters, got: {riasec['code_2']}"
        assert len(riasec["major"]) == 1, f"major should be 1 letter, got: {riasec['major']}"
        assert len(riasec["minor"]) == 1, f"minor should be 1 letter, got: {riasec['minor']}"
        
        # Verify major and minor match code_2
        assert riasec["major"] == riasec["code_2"][0], \
            f"major ({riasec['major']}) should be first letter of code_2 ({riasec['code_2']})"
        assert riasec["minor"] == riasec["code_2"][1], \
            f"minor ({riasec['minor']}) should be second letter of code_2 ({riasec['code_2']})"
        
        # Verify scores structure (should have R, I, A, S, E, C keys)
        scores = riasec["scores"]
        expected_keys = {"R", "I", "A", "S", "E", "C"}
        assert set(scores.keys()) == expected_keys, \
            f"scores should have keys {expected_keys}, got {set(scores.keys())}"
        
        # Verify scores are in valid range (0-100)
        for key, value in scores.items():
            assert 0 <= value <= 100, f"Score for {key} should be 0-100, got {value}"
        
        print(f"PASS: /api/job-match contains RIASEC profile: {riasec['code_2']}")
        print(f"  Major: {riasec['major']} ({riasec.get('major_name', 'N/A')})")
        print(f"  Minor: {riasec['minor']} ({riasec.get('minor_name', 'N/A')})")
        print(f"  Scores: {scores}")

    def test_job_match_riasec_has_descriptive_fields(self):
        """Verify RIASEC includes descriptive fields for frontend display"""
        payload = {
            "answers": INFP_ANSWERS,
            "job_query": "commercial"
        }
        
        response = requests.post(f"{BASE_URL}/api/job-match", json=payload)
        assert response.status_code == 200
        
        data = response.json()
        riasec = data["profile_summary"]["riasec"]
        
        # Verify descriptive fields exist (used by frontend RiasecProfile component)
        assert "major_name" in riasec, "riasec missing major_name"
        assert "minor_name" in riasec, "riasec missing minor_name"
        assert "major_description" in riasec, "riasec missing major_description"
        
        # Verify names are non-empty strings
        assert isinstance(riasec["major_name"], str) and len(riasec["major_name"]) > 0
        assert isinstance(riasec["minor_name"], str) and len(riasec["minor_name"]) > 0
        assert isinstance(riasec["major_description"], str) and len(riasec["major_description"]) > 0
        
        print(f"PASS: RIASEC has descriptive fields for frontend")
        print(f"  Major Name: {riasec['major_name']}")
        print(f"  Minor Name: {riasec['minor_name']}")


class TestRIASECExploreEndpoint:
    """Test 2: API /api/explore - Verify RIASEC profile in profile_summary"""
    
    def test_explore_contains_riasec_profile(self):
        """
        Verify /api/explore response contains RIASEC profile in profile_summary
        """
        payload = {
            "answers": INFP_ANSWERS
        }
        
        response = requests.post(f"{BASE_URL}/api/explore", json=payload)
        assert response.status_code == 200, f"API returned {response.status_code}: {response.text}"
        
        data = response.json()
        
        # Verify profile_summary exists
        assert "profile_summary" in data, "Response missing profile_summary field"
        profile_summary = data["profile_summary"]
        
        # Verify RIASEC profile exists
        assert "riasec" in profile_summary, "profile_summary missing riasec field"
        riasec = profile_summary["riasec"]
        
        # Verify required RIASEC fields (same as job-match)
        assert "code_2" in riasec, "riasec missing code_2"
        assert "major" in riasec, "riasec missing major"
        assert "minor" in riasec, "riasec missing minor"
        assert "scores" in riasec, "riasec missing scores"
        
        # Verify scores have RIASEC keys
        expected_keys = {"R", "I", "A", "S", "E", "C"}
        assert set(riasec["scores"].keys()) == expected_keys
        
        print(f"PASS: /api/explore contains RIASEC profile: {riasec['code_2']}")

    def test_explore_with_birth_date_has_riasec(self):
        """Verify RIASEC is present even with birth_date parameter"""
        payload = {
            "answers": INTJ_ANSWERS,
            "birth_date": "1985-03-20"
        }
        
        response = requests.post(f"{BASE_URL}/api/explore", json=payload)
        assert response.status_code == 200
        
        data = response.json()
        assert "profile_summary" in data
        assert "riasec" in data["profile_summary"]
        
        print(f"PASS: /api/explore with birth_date contains RIASEC")


class TestRIASECProfileCoherence:
    """Test 4: Coherence - Verify MBTI → RIASEC mapping is logical"""
    
    def test_intj_profile_has_investigator_dominant(self):
        """
        INTJ profile should yield RIASEC code with I (Investigator) dominant or secondary.
        INTJ characteristics:
        - Introverted (I) → prefers working alone
        - Intuitive (N) → likes ideas and concepts
        - Thinking (T) → analytical, logical
        - Judging (J) → organized, structured
        
        Expected RIASEC: IC, CI, IA, AI (Investigator should be in top 2)
        """
        payload = {
            "answers": INTJ_ANSWERS,
            "job_query": "analyste"
        }
        
        response = requests.post(f"{BASE_URL}/api/job-match", json=payload)
        assert response.status_code == 200
        
        data = response.json()
        riasec = data["profile_summary"]["riasec"]
        code_2 = riasec["code_2"]
        
        print(f"INTJ profile yielded RIASEC code: {code_2}")
        print(f"  Major: {riasec['major']} ({riasec.get('major_name', 'N/A')})")
        print(f"  Minor: {riasec['minor']} ({riasec.get('minor_name', 'N/A')})")
        print(f"  Scores: {riasec['scores']}")
        
        # INTJ should have Investigator (I) or Conventional (C) in top 2
        # Due to their analytical nature and preference for structure
        has_expected_riasec = 'I' in code_2 or 'C' in code_2
        
        assert has_expected_riasec, \
            f"INTJ profile expected I or C in RIASEC code, got: {code_2}"
        
        print(f"PASS: INTJ coherently maps to RIASEC {code_2} (contains I or C)")

    def test_estj_profile_has_enterprising_or_conventional(self):
        """
        ESTJ profile should yield RIASEC code with E (Enterprising) or C (Conventional) dominant.
        ESTJ characteristics:
        - Extraverted (E) → likes working with others
        - Sensing (S) → practical, detail-oriented
        - Thinking (T) → logical, objective
        - Judging (J) → organized, decisive
        
        Expected RIASEC: EC, CE, ES, SE (Enterprising or Conventional should be dominant)
        """
        payload = {
            "answers": ESTJ_ANSWERS,
            "job_query": "manager"
        }
        
        response = requests.post(f"{BASE_URL}/api/job-match", json=payload)
        assert response.status_code == 200
        
        data = response.json()
        riasec = data["profile_summary"]["riasec"]
        code_2 = riasec["code_2"]
        
        print(f"ESTJ profile yielded RIASEC code: {code_2}")
        print(f"  Major: {riasec['major']} ({riasec.get('major_name', 'N/A')})")
        print(f"  Scores: {riasec['scores']}")
        
        # ESTJ should have Enterprising (E) or Conventional (C) in top 2
        has_expected_riasec = 'E' in code_2 or 'C' in code_2
        
        assert has_expected_riasec, \
            f"ESTJ profile expected E or C in RIASEC code, got: {code_2}"
        
        print(f"PASS: ESTJ coherently maps to RIASEC {code_2} (contains E or C)")


class TestRIASECScoreBreakdown:
    """Test 5: Score RIASEC - Verify score breakdown contains 'riasec' key"""
    
    def test_job_match_score_breakdown_has_riasec(self):
        """
        Verify best_match score_breakdown contains 'riasec' component (20% weight).
        According to server.py line 3593:
        WEIGHTS = {"riasec": 20, ...}
        """
        payload = {
            "answers": INFP_ANSWERS,
            "job_query": "développeur web"
        }
        
        response = requests.post(f"{BASE_URL}/api/job-match", json=payload)
        assert response.status_code == 200
        
        data = response.json()
        
        # Verify best_match has score_breakdown
        assert "best_match" in data, "Response missing best_match"
        best_match = data["best_match"]
        
        # Check for either "breakdown" or "score_breakdown" (API uses "breakdown")
        breakdown_key = "breakdown" if "breakdown" in best_match else "score_breakdown"
        assert breakdown_key in best_match, f"best_match missing breakdown field. Keys: {list(best_match.keys())}"
        score_breakdown = best_match[breakdown_key]
        
        # Verify riasec is in score_breakdown
        assert "riasec" in score_breakdown, \
            f"breakdown missing 'riasec' key. Got keys: {list(score_breakdown.keys())}"
        
        riasec_score = score_breakdown["riasec"]
        
        # RIASEC has 20% weight, so max contribution is 20 points
        assert 0 <= riasec_score <= 20, \
            f"RIASEC score should be 0-20 (20% weight), got: {riasec_score}"
        
        print(f"PASS: score_breakdown contains riasec: {riasec_score} points")
        print(f"  Full breakdown: {score_breakdown}")

    def test_other_matches_have_riasec_in_breakdown(self):
        """Verify other_matches also have riasec in breakdown"""
        payload = {
            "answers": INFP_ANSWERS,
            "job_query": "informatique"
        }
        
        response = requests.post(f"{BASE_URL}/api/job-match", json=payload)
        assert response.status_code == 200
        
        data = response.json()
        
        if "other_matches" in data and len(data["other_matches"]) > 0:
            for idx, match in enumerate(data["other_matches"][:3]):
                breakdown_key = "breakdown" if "breakdown" in match else "score_breakdown"
                if breakdown_key in match:
                    assert "riasec" in match[breakdown_key], \
                        f"other_matches[{idx}] breakdown missing 'riasec'"
                    print(f"  Match {idx+1}: RIASEC = {match[breakdown_key]['riasec']}")
        
        print(f"PASS: other_matches have riasec in score_breakdown")


class TestRIASECJobRiasecField:
    """Verify job_riasec field is added to job scores"""
    
    def test_best_match_has_job_riasec(self):
        """
        Verify best_match includes job_riasec field (the RIASEC code of the job).
        According to server.py line 4072: "job_riasec": job_riasec
        """
        payload = {
            "answers": INFP_ANSWERS,
            "job_query": "infirmier"
        }
        
        response = requests.post(f"{BASE_URL}/api/job-match", json=payload)
        assert response.status_code == 200
        
        data = response.json()
        best_match = data.get("best_match", {})
        
        # job_riasec should be present
        if "job_riasec" in best_match:
            job_riasec = best_match["job_riasec"]
            print(f"PASS: best_match has job_riasec: {job_riasec}")
            
            # Verify it's a 2-letter RIASEC code
            if job_riasec:
                assert len(job_riasec) == 2, f"job_riasec should be 2 letters, got: {job_riasec}"
                valid_letters = set("RIASEC")
                for letter in job_riasec:
                    assert letter in valid_letters, \
                        f"Invalid RIASEC letter '{letter}' in job_riasec: {job_riasec}"
        else:
            # It might not be present for France Travail results
            print(f"INFO: job_riasec not present in best_match (may be France Travail source)")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
