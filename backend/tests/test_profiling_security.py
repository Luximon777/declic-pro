"""
Tests de sécurité du système de profilage DE'CLIC PRO.
Vérifie que chaque type MBTI produit la bonne vertu dominante.
"""

import pytest
import sys
sys.path.insert(0, '/app/backend')

from server import compute_profile, calculate_vertus_profile, MBTI_TO_VERTU_FALLBACK


# Profils de test pour chaque type MBTI
MBTI_TEST_PROFILES = {
    # NT - Analystes → Sagesse
    "INTJ": {"v1": "I", "v2": "I", "v3": "N", "v4": "N1,N2,S1,S2", "v5": "T", "v6": "T", "v7": "J", "v8": "J"},
    "INTP": {"v1": "I", "v2": "I", "v3": "N", "v4": "N1,N2,S1,S2", "v5": "T", "v6": "T", "v7": "P", "v8": "P"},
    "ENTJ": {"v1": "E", "v2": "E", "v3": "N", "v4": "N1,N2,S1,S2", "v5": "T", "v6": "T", "v7": "J", "v8": "J"},
    "ENTP": {"v1": "E", "v2": "E", "v3": "N", "v4": "N1,N2,S1,S2", "v5": "T", "v6": "T", "v7": "P", "v8": "P"},
    
    # NF - Diplomates → Humanité/Transcendance
    "INFJ": {"v1": "I", "v2": "I", "v3": "N", "v4": "N1,N2,S1,S2", "v5": "F", "v6": "F", "v7": "J", "v8": "J"},
    "INFP": {"v1": "I", "v2": "I", "v3": "N", "v4": "N1,N2,S1,S2", "v5": "F", "v6": "F", "v7": "P", "v8": "P"},
    "ENFJ": {"v1": "E", "v2": "E", "v3": "N", "v4": "N1,N2,S1,S2", "v5": "F", "v6": "F", "v7": "J", "v8": "J"},
    "ENFP": {"v1": "E", "v2": "E", "v3": "N", "v4": "N1,N2,S1,S2", "v5": "F", "v6": "F", "v7": "P", "v8": "P"},
    
    # SJ - Sentinelles → Justice/Humanité
    "ISTJ": {"v1": "I", "v2": "I", "v3": "S", "v4": "S1,S2,N1,N2", "v5": "T", "v6": "T", "v7": "J", "v8": "J"},
    "ISFJ": {"v1": "I", "v2": "I", "v3": "S", "v4": "S1,S2,N1,N2", "v5": "F", "v6": "F", "v7": "J", "v8": "J"},
    "ESTJ": {"v1": "E", "v2": "E", "v3": "S", "v4": "S1,S2,N1,N2", "v5": "T", "v6": "T", "v7": "J", "v8": "J"},
    "ESFJ": {"v1": "E", "v2": "E", "v3": "S", "v4": "S1,S2,N1,N2", "v5": "F", "v6": "F", "v7": "J", "v8": "J"},
    
    # SP - Explorateurs → Courage/Transcendance
    "ISTP": {"v1": "I", "v2": "I", "v3": "S", "v4": "S1,S2,N1,N2", "v5": "T", "v6": "T", "v7": "P", "v8": "P"},
    "ISFP": {"v1": "I", "v2": "I", "v3": "S", "v4": "S1,S2,N1,N2", "v5": "F", "v6": "F", "v7": "P", "v8": "P"},
    "ESTP": {"v1": "E", "v2": "E", "v3": "S", "v4": "S1,S2,N1,N2", "v5": "T", "v6": "T", "v7": "P", "v8": "P"},
    "ESFP": {"v1": "E", "v2": "E", "v3": "S", "v4": "S1,S2,N1,N2", "v5": "F", "v6": "F", "v7": "P", "v8": "P"},
}


class TestMBTICalculation:
    """Tests de calcul MBTI."""
    
    @pytest.mark.parametrize("expected_mbti,answers", MBTI_TEST_PROFILES.items())
    def test_mbti_calculation(self, expected_mbti, answers):
        """Vérifie que chaque profil de réponses produit le bon MBTI."""
        profile = compute_profile(answers)
        assert profile.get("mbti") == expected_mbti, \
            f"Attendu {expected_mbti}, obtenu {profile.get('mbti')}"


class TestVertuMapping:
    """Tests du mapping MBTI → Vertu."""
    
    @pytest.mark.parametrize("mbti,answers", MBTI_TEST_PROFILES.items())
    def test_vertu_coherence(self, mbti, answers):
        """Vérifie que la vertu calculée correspond au mapping MBTI."""
        profile = compute_profile(answers)
        vertus = calculate_vertus_profile(answers, mbti_type=profile.get("mbti"))
        
        expected_dominant, expected_secondary = MBTI_TO_VERTU_FALLBACK.get(mbti, ("?", "?"))
        actual_dominant = vertus.get("dominant")
        
        assert actual_dominant == expected_dominant, \
            f"MBTI {mbti}: Vertu attendue '{expected_dominant}', obtenue '{actual_dominant}'"
    
    def test_estp_not_sagesse(self):
        """Cas spécifique: ESTP ne doit jamais donner Sagesse."""
        answers = MBTI_TEST_PROFILES["ESTP"]
        profile = compute_profile(answers)
        vertus = calculate_vertus_profile(answers, mbti_type=profile.get("mbti"))
        
        assert vertus.get("dominant") != "sagesse", \
            "ESTP ne doit pas avoir Sagesse comme vertu dominante!"
        assert vertus.get("dominant") == "courage", \
            "ESTP doit avoir Courage comme vertu dominante!"


class TestGroupCoherence:
    """Tests de cohérence des groupes MBTI."""
    
    def test_nt_group_sagesse(self):
        """Tous les NT (Analystes) doivent avoir Sagesse ou Justice."""
        nt_types = ["INTJ", "INTP", "ENTJ", "ENTP"]
        for mbti in nt_types:
            answers = MBTI_TEST_PROFILES[mbti]
            profile = compute_profile(answers)
            vertus = calculate_vertus_profile(answers, mbti_type=profile.get("mbti"))
            assert vertus.get("dominant") in ["sagesse", "justice"], \
                f"{mbti} devrait avoir sagesse ou justice, pas {vertus.get('dominant')}"
    
    def test_sp_group_courage(self):
        """Tous les SP (Explorateurs) avec T doivent avoir Courage."""
        sp_t_types = ["ISTP", "ESTP"]
        for mbti in sp_t_types:
            answers = MBTI_TEST_PROFILES[mbti]
            profile = compute_profile(answers)
            vertus = calculate_vertus_profile(answers, mbti_type=profile.get("mbti"))
            assert vertus.get("dominant") == "courage", \
                f"{mbti} devrait avoir courage, pas {vertus.get('dominant')}"


class TestEdgeCases:
    """Tests des cas limites."""
    
    def test_empty_answers(self):
        """Réponses vides ne doivent pas crasher."""
        profile = compute_profile({})
        vertus = calculate_vertus_profile({}, mbti_type=profile.get("mbti"))
        
        assert profile.get("mbti") is not None
        assert vertus.get("dominant") is not None
    
    def test_partial_answers(self):
        """Réponses partielles ne doivent pas crasher."""
        partial_answers = {"v1": "E", "v3": "N"}
        profile = compute_profile(partial_answers)
        vertus = calculate_vertus_profile(partial_answers, mbti_type=profile.get("mbti"))
        
        assert profile.get("mbti") is not None
        assert len(profile.get("mbti", "")) == 4
    
    def test_invalid_values(self):
        """Valeurs invalides ne doivent pas crasher."""
        invalid_answers = {"v1": "X", "v2": "123", "v3": "invalid"}
        profile = compute_profile(invalid_answers)
        vertus = calculate_vertus_profile(invalid_answers, mbti_type=profile.get("mbti"))
        
        assert profile.get("mbti") is not None
        assert vertus.get("dominant") is not None


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
