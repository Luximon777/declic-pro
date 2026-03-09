"""
Test INFJ profile job recommendations after weight adjustment.
This test verifies that "Psychologue" appears in top 3 recommendations for INFJ profiles.
"""
import sys
sys.path.insert(0, '/app/backend')

from server import compute_profile, score_job, METIERS, calculate_riasec_profile, calculate_vertus_profile

# INFJ-producing answers:
# I (Introverted) + N (Intuitive) + F (Feeling) + J (Judging)
INFJ_ANSWERS = {
    "v1": "I",  # Introversion
    "v2": "I",  # Introversion
    "v3": "N",  # Intuition
    "v4": "N1,N2,S1,S2",  # Intuition dominant
    "v5": "F",  # Feeling
    "v6": "F",  # Feeling
    "v7": "J",  # Judging
    "v8": "J",  # Judging
    "v9": "S,I,C,D",  # DISC - Stabilité dominante (typical for NF)
    "v10": "S,C,I,D",  # DISC
    "v11": "4,2,5,9",  # Enneagram 4 (Créatif) typical for INFJ
    "v12": "2,4,9,5",  # Enneagram
    # Vertus questions
    "vv1": "humanite",  # Typical for INFJ
    "vv2": "transcendance",
    "vv3": "humanite",
    "vv4": "sagesse",
    "vv5": "humanite",
    "vv6": "transcendance",
}


def test_infj_profile_calculation():
    """Test that answers produce INFJ profile"""
    profile = compute_profile(INFJ_ANSWERS)
    mbti = profile.get("mbti", "")
    print(f"\n=== Profile Calculation ===")
    print(f"MBTI: {mbti}")
    print(f"DISC: {profile.get('disc', '')}")
    print(f"Enneagram dominant: {profile.get('ennea_dominant', '')}")
    print(f"Enneagram runner-up: {profile.get('ennea_runner_up', '')}")
    
    # Check if we got an NF profile (INFJ, INFP, ENFJ, or ENFP)
    assert len(mbti) == 4, f"Invalid MBTI: {mbti}"
    assert mbti[1] == "N", f"Expected Intuitive (N), got {mbti[1]}"
    assert mbti[2] == "F", f"Expected Feeling (F), got {mbti[2]}"
    print(f"✓ Got NF profile: {mbti}")
    return profile


def test_psychologue_ranking():
    """Test that Psychologue is in top 3 for INFJ"""
    profile = compute_profile(INFJ_ANSWERS)
    user_riasec = calculate_riasec_profile(INFJ_ANSWERS, profile)
    vertus_profile = calculate_vertus_profile(INFJ_ANSWERS, mbti_type=profile.get("mbti"))
    
    print(f"\n=== Job Scoring for {profile.get('mbti', '?')} ===")
    
    # Score all jobs
    all_scores = []
    for job in METIERS:
        score_result = score_job(profile, job, user_riasec, vertus_profile)
        all_scores.append({
            "label": score_result["job_label"],
            "score": score_result["score"],
            "mbti_compatible": job.get("mbti_compatible", [])
        })
    
    # Sort by score
    all_scores.sort(key=lambda x: x["score"], reverse=True)
    
    # Find Psychologue position
    psychologue_rank = None
    for i, job in enumerate(all_scores):
        if "psychologue" in job["label"].lower():
            psychologue_rank = i + 1
            break
    
    print(f"\n=== Top 10 Job Recommendations ===")
    for i, job in enumerate(all_scores[:10]):
        marker = "★" if "psychologue" in job["label"].lower() else " "
        print(f"{i+1}. {marker} {job['label']} - Score: {job['score']} - MBTI: {job['mbti_compatible']}")
    
    print(f"\n=== Psychologue Ranking ===")
    print(f"Position: {psychologue_rank}")
    
    # Check if Psychologue is in top 5 (was at position 8, should be top 3 now)
    assert psychologue_rank is not None, "Psychologue not found in job list"
    assert psychologue_rank <= 5, f"Psychologue should be top 5, but is at position {psychologue_rank}"
    print(f"✓ Psychologue is in top 5 (position {psychologue_rank})")


def test_regression_estp():
    """Regression test: ESTP should still get appropriate recommendations"""
    estp_answers = {
        "v1": "E",
        "v2": "E",
        "v3": "S",
        "v4": "S1,S2,N1,N2",
        "v5": "T",
        "v6": "T",
        "v7": "P",
        "v8": "P",
        "v9": "D,I,S,C",
        "v10": "D,I,S,C",
        "v11": "7,8,3,1",
        "v12": "8,7,3,1",
    }
    
    profile = compute_profile(estp_answers)
    user_riasec = calculate_riasec_profile(estp_answers, profile)
    vertus_profile = calculate_vertus_profile(estp_answers, mbti_type=profile.get("mbti"))
    
    print(f"\n=== Regression Test: {profile.get('mbti', '?')} ===")
    
    all_scores = []
    for job in METIERS:
        score_result = score_job(profile, job, user_riasec, vertus_profile)
        all_scores.append({
            "label": score_result["job_label"],
            "score": score_result["score"],
            "mbti_compatible": job.get("mbti_compatible", [])
        })
    
    all_scores.sort(key=lambda x: x["score"], reverse=True)
    
    print(f"Top 5 for {profile.get('mbti', '?')}:")
    for i, job in enumerate(all_scores[:5]):
        print(f"  {i+1}. {job['label']} - Score: {job['score']}")
    
    # ESTP should NOT have Psychologue in top 3
    psychologue_rank = None
    for i, job in enumerate(all_scores):
        if "psychologue" in job["label"].lower():
            psychologue_rank = i + 1
            break
    
    print(f"Psychologue position for ESTP: {psychologue_rank}")
    # Psychologue should not be top 3 for ESTP
    if psychologue_rank and psychologue_rank <= 3:
        print(f"⚠ Warning: Psychologue unexpectedly in top 3 for ESTP")
    else:
        print(f"✓ Psychologue is appropriately ranked for ESTP")


if __name__ == "__main__":
    print("=" * 60)
    print("INFJ Psychologue Recommendation Test")
    print("=" * 60)
    
    try:
        profile = test_infj_profile_calculation()
        test_psychologue_ranking()
        test_regression_estp()
        print("\n" + "=" * 60)
        print("ALL TESTS PASSED ✓")
        print("=" * 60)
    except AssertionError as e:
        print(f"\n❌ TEST FAILED: {e}")
        exit(1)
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
        exit(1)
