"""
VALIDATION COMPLÈTE DU SYSTÈME DE PROFILAGE
============================================
Test exhaustif couvrant:
1. Les 16 types MBTI
2. Cohérence filières par groupe MBTI
3. Croisements MBTI ↔ DISC ↔ Ennéagramme ↔ Vertus
"""
import sys
sys.path.insert(0, '/app/backend')

from server import (
    compute_profile, score_job, METIERS, FILIERES,
    calculate_riasec_profile, calculate_vertus_profile,
    get_exploration_paths, score_filiere,
    MBTI_TO_VERTU_FALLBACK, ENNEA_TO_PROFILE
)

# ============================================================================
# DÉFINITION DES 16 PROFILS MBTI AVEC RÉPONSES TYPES
# ============================================================================

MBTI_TEST_ANSWERS = {
    # NF - Les Idéalistes (Intuition + Feeling)
    "INFJ": {
        "v1": "I", "v2": "I", "v3": "N", "v4": "N1,N2,S1,S2",
        "v5": "F", "v6": "F", "v7": "J", "v8": "J",
        "v9": "S,C,I,D", "v10": "S,C,I,D",
        "v11": "4,2,5,9", "v12": "2,4,9,5",
        "vv1": "humanite", "vv2": "transcendance", "vv3": "humanite",
        "vv4": "sagesse", "vv5": "humanite", "vv6": "transcendance"
    },
    "INFP": {
        "v1": "I", "v2": "I", "v3": "N", "v4": "N1,N2,S1,S2",
        "v5": "F", "v6": "F", "v7": "P", "v8": "P",
        "v9": "S,I,C,D", "v10": "S,I,C,D",
        "v11": "4,9,5,2", "v12": "4,9,2,5",
        "vv1": "transcendance", "vv2": "humanite", "vv3": "transcendance",
        "vv4": "humanite", "vv5": "transcendance", "vv6": "humanite"
    },
    "ENFJ": {
        "v1": "E", "v2": "E", "v3": "N", "v4": "N1,N2,S1,S2",
        "v5": "F", "v6": "F", "v7": "J", "v8": "J",
        "v9": "I,S,D,C", "v10": "I,S,D,C",
        "v11": "2,3,1,9", "v12": "2,3,9,1",
        "vv1": "humanite", "vv2": "justice", "vv3": "humanite",
        "vv4": "courage", "vv5": "humanite", "vv6": "justice"
    },
    "ENFP": {
        "v1": "E", "v2": "E", "v3": "N", "v4": "N1,N2,S1,S2",
        "v5": "F", "v6": "F", "v7": "P", "v8": "P",
        "v9": "I,D,S,C", "v10": "I,D,S,C",
        "v11": "7,4,2,9", "v12": "7,4,9,2",
        "vv1": "transcendance", "vv2": "humanite", "vv3": "transcendance",
        "vv4": "courage", "vv5": "transcendance", "vv6": "humanite"
    },
    
    # NT - Les Rationnels (Intuition + Thinking)
    "INTJ": {
        "v1": "I", "v2": "I", "v3": "N", "v4": "N1,N2,S1,S2",
        "v5": "T", "v6": "T", "v7": "J", "v8": "J",
        "v9": "C,D,I,S", "v10": "C,D,I,S",
        "v11": "5,1,3,8", "v12": "5,1,8,3",
        "vv1": "sagesse", "vv2": "temperance", "vv3": "sagesse",
        "vv4": "justice", "vv5": "sagesse", "vv6": "temperance"
    },
    "INTP": {
        "v1": "I", "v2": "I", "v3": "N", "v4": "N1,N2,S1,S2",
        "v5": "T", "v6": "T", "v7": "P", "v8": "P",
        "v9": "C,I,S,D", "v10": "C,I,S,D",
        "v11": "5,4,9,7", "v12": "5,4,7,9",
        "vv1": "sagesse", "vv2": "transcendance", "vv3": "sagesse",
        "vv4": "temperance", "vv5": "sagesse", "vv6": "transcendance"
    },
    "ENTJ": {
        "v1": "E", "v2": "E", "v3": "N", "v4": "N1,N2,S1,S2",
        "v5": "T", "v6": "T", "v7": "J", "v8": "J",
        "v9": "D,C,I,S", "v10": "D,C,I,S",
        "v11": "8,3,1,5", "v12": "8,3,5,1",
        "vv1": "justice", "vv2": "courage", "vv3": "justice",
        "vv4": "sagesse", "vv5": "justice", "vv6": "courage"
    },
    "ENTP": {
        "v1": "E", "v2": "E", "v3": "N", "v4": "N1,N2,S1,S2",
        "v5": "T", "v6": "T", "v7": "P", "v8": "P",
        "v9": "D,I,C,S", "v10": "D,I,C,S",
        "v11": "7,8,3,5", "v12": "7,8,5,3",
        "vv1": "transcendance", "vv2": "courage", "vv3": "transcendance",
        "vv4": "sagesse", "vv5": "transcendance", "vv6": "courage"
    },
    
    # SJ - Les Gardiens (Sensing + Judging)
    "ISTJ": {
        "v1": "I", "v2": "I", "v3": "S", "v4": "S1,S2,N1,N2",
        "v5": "T", "v6": "T", "v7": "J", "v8": "J",
        "v9": "C,S,D,I", "v10": "C,S,D,I",
        "v11": "1,6,5,3", "v12": "1,6,3,5",
        "vv1": "temperance", "vv2": "justice", "vv3": "temperance",
        "vv4": "sagesse", "vv5": "temperance", "vv6": "justice"
    },
    "ISFJ": {
        "v1": "I", "v2": "I", "v3": "S", "v4": "S1,S2,N1,N2",
        "v5": "F", "v6": "F", "v7": "J", "v8": "J",
        "v9": "S,C,I,D", "v10": "S,C,I,D",
        "v11": "2,6,1,9", "v12": "2,6,9,1",
        "vv1": "humanite", "vv2": "temperance", "vv3": "humanite",
        "vv4": "justice", "vv5": "humanite", "vv6": "temperance"
    },
    "ESTJ": {
        "v1": "E", "v2": "E", "v3": "S", "v4": "S1,S2,N1,N2",
        "v5": "T", "v6": "T", "v7": "J", "v8": "J",
        "v9": "D,C,S,I", "v10": "D,C,S,I",
        "v11": "1,8,3,6", "v12": "1,8,6,3",
        "vv1": "justice", "vv2": "temperance", "vv3": "justice",
        "vv4": "courage", "vv5": "justice", "vv6": "temperance"
    },
    "ESFJ": {
        "v1": "E", "v2": "E", "v3": "S", "v4": "S1,S2,N1,N2",
        "v5": "F", "v6": "F", "v7": "J", "v8": "J",
        "v9": "I,S,C,D", "v10": "I,S,C,D",
        "v11": "2,1,6,9", "v12": "2,1,9,6",
        "vv1": "humanite", "vv2": "temperance", "vv3": "humanite",
        "vv4": "justice", "vv5": "humanite", "vv6": "temperance"
    },
    
    # SP - Les Artisans (Sensing + Perceiving)
    "ISTP": {
        "v1": "I", "v2": "I", "v3": "S", "v4": "S1,S2,N1,N2",
        "v5": "T", "v6": "T", "v7": "P", "v8": "P",
        "v9": "C,D,S,I", "v10": "C,D,S,I",
        "v11": "5,9,6,7", "v12": "5,9,7,6",
        "vv1": "sagesse", "vv2": "courage", "vv3": "sagesse",
        "vv4": "temperance", "vv5": "sagesse", "vv6": "courage"
    },
    "ISFP": {
        "v1": "I", "v2": "I", "v3": "S", "v4": "S1,S2,N1,N2",
        "v5": "F", "v6": "F", "v7": "P", "v8": "P",
        "v9": "S,I,C,D", "v10": "S,I,C,D",
        "v11": "4,9,2,6", "v12": "4,9,6,2",
        "vv1": "transcendance", "vv2": "humanite", "vv3": "transcendance",
        "vv4": "temperance", "vv5": "transcendance", "vv6": "humanite"
    },
    "ESTP": {
        "v1": "E", "v2": "E", "v3": "S", "v4": "S1,S2,N1,N2",
        "v5": "T", "v6": "T", "v7": "P", "v8": "P",
        "v9": "D,I,S,C", "v10": "D,I,S,C",
        "v11": "7,8,3,9", "v12": "7,8,9,3",
        "vv1": "courage", "vv2": "transcendance", "vv3": "courage",
        "vv4": "justice", "vv5": "courage", "vv6": "transcendance"
    },
    "ESFP": {
        "v1": "E", "v2": "E", "v3": "S", "v4": "S1,S2,N1,N2",
        "v5": "F", "v6": "F", "v7": "P", "v8": "P",
        "v9": "I,S,D,C", "v10": "I,S,D,C",
        "v11": "7,2,9,4", "v12": "7,2,4,9",
        "vv1": "transcendance", "vv2": "humanite", "vv3": "transcendance",
        "vv4": "courage", "vv5": "transcendance", "vv6": "humanite"
    },
}

# ============================================================================
# DÉFINITION DES ATTENTES PAR GROUPE MBTI
# ============================================================================

# Filières attendues par groupe MBTI (ordre de priorité)
EXPECTED_FILIERES = {
    "NF": ["SSS", "EDU", "COM", "CRE"],  # Santé/Social, Éducation, Communication, Création
    "NT": ["TIC", "SCI", "FIN", "ING"],  # Tech, Sciences, Finance, Ingénierie
    "SJ": ["ADM", "JUR", "FIN", "SSS"],  # Administration, Juridique, Finance, Santé
    "SP": ["ART", "COM", "HRT", "LOG"],  # Artisanat, Commerce, Hôtellerie, Logistique
}

# Métiers typiques attendus par groupe MBTI
EXPECTED_TOP_JOBS = {
    "NF": ["Psychologue", "Éducateur", "Conseiller", "Formateur", "Coach", "Enseignant", "Médiateur"],
    "NT": ["Développeur", "Analyste", "Ingénieur", "Architecte", "Data", "Consultant", "Chercheur"],
    "SJ": ["Comptable", "Assistant", "Secrétaire", "Gestionnaire", "Agent administratif", "Juriste"],
    "SP": ["Chef de chantier", "Commercial", "Cuisinier", "Technicien", "Artisan", "Vendeur"],
}

# Vertus attendues par groupe MBTI
EXPECTED_VERTUS = {
    "NF": ["humanite", "transcendance"],
    "NT": ["sagesse", "justice"],
    "SJ": ["temperance", "justice"],
    "SP": ["courage", "transcendance"],
}

def get_mbti_group(mbti: str) -> str:
    """Retourne le groupe MBTI (NF, NT, SJ, SP)"""
    if len(mbti) < 4:
        return "?"
    if mbti[1] == "N" and mbti[2] == "F":
        return "NF"
    elif mbti[1] == "N" and mbti[2] == "T":
        return "NT"
    elif mbti[1] == "S" and mbti[2] == "J":
        return "SJ"
    elif mbti[1] == "S" and mbti[2] == "P":
        return "SP"
    return "?"


# ============================================================================
# TEST 1: VALIDATION DES 16 PROFILS MBTI
# ============================================================================

def test_all_16_mbti_profiles():
    """Vérifie que les réponses produisent le bon type MBTI"""
    print("\n" + "=" * 70)
    print("TEST 1: VALIDATION DES 16 PROFILS MBTI")
    print("=" * 70)
    
    results = []
    for expected_mbti, answers in MBTI_TEST_ANSWERS.items():
        profile = compute_profile(answers)
        actual_mbti = profile.get("mbti", "????")
        
        # Vérifier chaque lettre
        match = True
        details = []
        for i, (expected, actual) in enumerate(zip(expected_mbti, actual_mbti)):
            if expected != actual:
                match = False
                dimension = ["Énergie", "Perception", "Décision", "Structure"][i]
                details.append(f"{dimension}: attendu {expected}, obtenu {actual}")
        
        status = "✓" if match else "✗"
        results.append({
            "expected": expected_mbti,
            "actual": actual_mbti,
            "match": match,
            "details": details,
            "disc": profile.get("disc", "?"),
            "ennea": profile.get("ennea_dominant", "?")
        })
        
        if match:
            print(f"  {status} {expected_mbti} → {actual_mbti} (DISC: {profile.get('disc')}, Ennéa: {profile.get('ennea_dominant')})")
        else:
            print(f"  {status} {expected_mbti} → {actual_mbti} ERREUR: {', '.join(details)}")
    
    passed = sum(1 for r in results if r["match"])
    print(f"\nRésultat: {passed}/16 profils corrects")
    
    return results


# ============================================================================
# TEST 2: VALIDATION DES FILIÈRES PAR GROUPE MBTI
# ============================================================================

def test_filieres_by_mbti_group():
    """Vérifie que les filières recommandées correspondent au groupe MBTI"""
    print("\n" + "=" * 70)
    print("TEST 2: VALIDATION DES FILIÈRES PAR GROUPE MBTI")
    print("=" * 70)
    
    results = {}
    
    for mbti_type, answers in MBTI_TEST_ANSWERS.items():
        group = get_mbti_group(mbti_type)
        if group not in results:
            results[group] = {"types": [], "issues": []}
        
        profile = compute_profile(answers)
        user_riasec = calculate_riasec_profile(answers, profile)
        vertus_profile = calculate_vertus_profile(answers, mbti_type=profile.get("mbti"))
        
        # Obtenir les filières recommandées
        paths = get_exploration_paths(profile, user_riasec, vertus_profile)
        top_filieres = [p["filiere_id"] for p in paths[:3]]
        
        # Vérifier si au moins une filière attendue est dans le top 3
        expected = EXPECTED_FILIERES.get(group, [])
        found_expected = [f for f in top_filieres if f in expected]
        
        results[group]["types"].append({
            "mbti": mbti_type,
            "top_3": top_filieres,
            "expected": expected,
            "found": found_expected
        })
        
        if not found_expected:
            results[group]["issues"].append(f"{mbti_type}: Top 3 = {top_filieres}, attendu au moins un de {expected}")
    
    # Afficher les résultats par groupe
    for group in ["NF", "NT", "SJ", "SP"]:
        data = results.get(group, {"types": [], "issues": []})
        print(f"\n  Groupe {group} ({len(data['types'])} types):")
        print(f"    Filières attendues: {EXPECTED_FILIERES.get(group, [])}")
        
        for t in data["types"]:
            status = "✓" if t["found"] else "✗"
            print(f"    {status} {t['mbti']}: Top 3 = {t['top_3']}")
        
        if data["issues"]:
            print(f"    ⚠ Problèmes: {len(data['issues'])}")
    
    total_issues = sum(len(d["issues"]) for d in results.values())
    print(f"\nRésultat: {16 - total_issues}/16 profils avec filières cohérentes")
    
    return results


# ============================================================================
# TEST 3: VALIDATION DES MÉTIERS PAR GROUPE MBTI
# ============================================================================

def test_jobs_by_mbti_group():
    """Vérifie que les métiers recommandés correspondent au groupe MBTI"""
    print("\n" + "=" * 70)
    print("TEST 3: VALIDATION DES MÉTIERS PAR GROUPE MBTI")
    print("=" * 70)
    
    results = {}
    
    for mbti_type, answers in MBTI_TEST_ANSWERS.items():
        group = get_mbti_group(mbti_type)
        if group not in results:
            results[group] = {"types": [], "issues": []}
        
        profile = compute_profile(answers)
        user_riasec = calculate_riasec_profile(answers, profile)
        vertus_profile = calculate_vertus_profile(answers, mbti_type=profile.get("mbti"))
        
        # Scorer tous les métiers
        all_scores = []
        for job in METIERS:
            score_result = score_job(profile, job, user_riasec, vertus_profile)
            all_scores.append({
                "label": score_result["job_label"],
                "score": score_result["score"]
            })
        
        all_scores.sort(key=lambda x: x["score"], reverse=True)
        top_5_jobs = [j["label"] for j in all_scores[:5]]
        
        # Vérifier si au moins un métier attendu est dans le top 5
        expected_keywords = EXPECTED_TOP_JOBS.get(group, [])
        found = []
        for job in top_5_jobs:
            for keyword in expected_keywords:
                if keyword.lower() in job.lower():
                    found.append(job)
                    break
        
        results[group]["types"].append({
            "mbti": mbti_type,
            "top_5": top_5_jobs,
            "found": found
        })
        
        if not found:
            results[group]["issues"].append(f"{mbti_type}: Top 5 = {top_5_jobs}")
    
    # Afficher les résultats par groupe
    for group in ["NF", "NT", "SJ", "SP"]:
        data = results.get(group, {"types": [], "issues": []})
        print(f"\n  Groupe {group}:")
        print(f"    Métiers attendus (mots-clés): {EXPECTED_TOP_JOBS.get(group, [])[:4]}...")
        
        for t in data["types"]:
            status = "✓" if t["found"] else "✗"
            jobs_str = ", ".join(t["top_5"][:3])
            print(f"    {status} {t['mbti']}: {jobs_str}...")
        
        if data["issues"]:
            print(f"    ⚠ Problèmes: {len(data['issues'])}")
    
    total_issues = sum(len(d["issues"]) for d in results.values())
    print(f"\nRésultat: {16 - total_issues}/16 profils avec métiers cohérents")
    
    return results


# ============================================================================
# TEST 4: COHÉRENCE MBTI ↔ VERTUS
# ============================================================================

def test_mbti_vertu_coherence():
    """Vérifie que les vertus calculées correspondent au groupe MBTI"""
    print("\n" + "=" * 70)
    print("TEST 4: COHÉRENCE MBTI ↔ VERTUS")
    print("=" * 70)
    
    results = []
    
    for mbti_type, answers in MBTI_TEST_ANSWERS.items():
        group = get_mbti_group(mbti_type)
        profile = compute_profile(answers)
        vertus_profile = calculate_vertus_profile(answers, mbti_type=profile.get("mbti"))
        
        dominant_vertu = vertus_profile.get("dominant", "?")
        expected_vertus = EXPECTED_VERTUS.get(group, [])
        
        # Vérifier aussi le fallback MBTI
        fallback_vertu = MBTI_TO_VERTU_FALLBACK.get(mbti_type, ("?", "?"))[0]
        
        coherent = dominant_vertu in expected_vertus or dominant_vertu == fallback_vertu
        
        results.append({
            "mbti": mbti_type,
            "group": group,
            "dominant_vertu": dominant_vertu,
            "expected": expected_vertus,
            "fallback": fallback_vertu,
            "coherent": coherent
        })
        
        status = "✓" if coherent else "✗"
        print(f"  {status} {mbti_type} ({group}): vertu={dominant_vertu}, attendu={expected_vertus}, fallback={fallback_vertu}")
    
    passed = sum(1 for r in results if r["coherent"])
    print(f"\nRésultat: {passed}/16 profils avec vertus cohérentes")
    
    return results


# ============================================================================
# TEST 5: COHÉRENCE ENNÉAGRAMME ↔ VERTUS
# ============================================================================

def test_enneagram_vertu_mapping():
    """Vérifie le mapping Ennéagramme → Vertu"""
    print("\n" + "=" * 70)
    print("TEST 5: COHÉRENCE ENNÉAGRAMME ↔ VERTUS")
    print("=" * 70)
    
    print("\n  Mapping Ennéagramme → Vertu dans le système:")
    for ennea_num, data in ENNEA_TO_PROFILE.items():
        print(f"    Type {ennea_num} ({data['name']}): {data['vertu']} - Moteur: {data['moteur']}")
    
    # Vérifier que chaque type a un mapping cohérent
    expected_mappings = {
        1: "temperance",    # Perfectionniste → Tempérance (contrôle, modération)
        2: "humanite",      # Altruiste → Humanité (aide, compassion)
        3: "courage",       # Performeur → Courage (action, réussite)
        4: "transcendance", # Créatif → Transcendance (authenticité, sens)
        5: "sagesse",       # Analyste → Sagesse (connaissance, compréhension)
        6: "temperance",    # Loyal → Tempérance (prudence, sécurité)
        7: "transcendance", # Enthousiaste → Transcendance (variété, exploration)
        8: "justice",       # Leader → Justice (impact, équité)
        9: "humanite",      # Médiateur → Humanité (harmonie, paix)
    }
    
    issues = []
    for ennea_num, expected_vertu in expected_mappings.items():
        actual_vertu = ENNEA_TO_PROFILE.get(ennea_num, {}).get("vertu", "?")
        if actual_vertu != expected_vertu:
            issues.append(f"Type {ennea_num}: attendu {expected_vertu}, système={actual_vertu}")
    
    if issues:
        print(f"\n  ⚠ Différences détectées:")
        for issue in issues:
            print(f"    - {issue}")
    else:
        print(f"\n  ✓ Tous les mappings Ennéagramme → Vertu sont cohérents")
    
    print(f"\nRésultat: {9 - len(issues)}/9 mappings corrects")
    
    return issues


# ============================================================================
# TEST 6: DISCRIMINATION DES SCORES (éviter les scores trop homogènes)
# ============================================================================

def test_score_discrimination():
    """Vérifie que les scores discriminent suffisamment les profils"""
    print("\n" + "=" * 70)
    print("TEST 6: DISCRIMINATION DES SCORES")
    print("=" * 70)
    
    results = []
    
    for mbti_type, answers in MBTI_TEST_ANSWERS.items():
        profile = compute_profile(answers)
        user_riasec = calculate_riasec_profile(answers, profile)
        vertus_profile = calculate_vertus_profile(answers, mbti_type=profile.get("mbti"))
        
        all_scores = []
        for job in METIERS:
            score_result = score_job(profile, job, user_riasec, vertus_profile)
            all_scores.append(score_result["score"])
        
        all_scores.sort(reverse=True)
        
        top_score = all_scores[0]
        bottom_score = all_scores[-1]
        spread = top_score - bottom_score
        avg_top_5 = sum(all_scores[:5]) / 5
        avg_bottom_5 = sum(all_scores[-5:]) / 5
        
        # Bonne discrimination si écart > 30 entre top et bottom
        good_discrimination = spread >= 30
        
        results.append({
            "mbti": mbti_type,
            "top": top_score,
            "bottom": bottom_score,
            "spread": spread,
            "avg_top_5": avg_top_5,
            "avg_bottom_5": avg_bottom_5,
            "good": good_discrimination
        })
        
        status = "✓" if good_discrimination else "✗"
        print(f"  {status} {mbti_type}: Top={top_score}, Bottom={bottom_score}, Écart={spread}")
    
    passed = sum(1 for r in results if r["good"])
    print(f"\nRésultat: {passed}/16 profils avec bonne discrimination (écart >= 30)")
    
    return results


# ============================================================================
# RAPPORT FINAL
# ============================================================================

def generate_final_report(all_results):
    """Génère un rapport de synthèse"""
    print("\n" + "=" * 70)
    print("RAPPORT FINAL DE VALIDATION")
    print("=" * 70)
    
    # Test 1: MBTI
    mbti_passed = sum(1 for r in all_results["mbti"] if r["match"])
    print(f"\n  1. Calcul MBTI:         {mbti_passed}/16 ({'✓' if mbti_passed == 16 else '⚠'})")
    
    # Test 2: Filières
    filiere_issues = sum(len(d["issues"]) for d in all_results["filieres"].values())
    print(f"  2. Filières par groupe: {16 - filiere_issues}/16 ({'✓' if filiere_issues == 0 else '⚠'})")
    
    # Test 3: Métiers
    job_issues = sum(len(d["issues"]) for d in all_results["jobs"].values())
    print(f"  3. Métiers par groupe:  {16 - job_issues}/16 ({'✓' if job_issues == 0 else '⚠'})")
    
    # Test 4: Vertus
    vertu_passed = sum(1 for r in all_results["vertus"] if r["coherent"])
    print(f"  4. Cohérence vertus:    {vertu_passed}/16 ({'✓' if vertu_passed == 16 else '⚠'})")
    
    # Test 5: Ennéagramme
    ennea_issues = len(all_results["enneagram"])
    print(f"  5. Mapping Ennéagramme: {9 - ennea_issues}/9 ({'✓' if ennea_issues == 0 else '⚠'})")
    
    # Test 6: Discrimination
    discrim_passed = sum(1 for r in all_results["discrimination"] if r["good"])
    print(f"  6. Discrimination:      {discrim_passed}/16 ({'✓' if discrim_passed == 16 else '⚠'})")
    
    # Score global
    total_tests = 16 + 16 + 16 + 16 + 9 + 16  # 89 tests
    total_passed = mbti_passed + (16 - filiere_issues) + (16 - job_issues) + vertu_passed + (9 - ennea_issues) + discrim_passed
    
    print(f"\n  {'=' * 50}")
    print(f"  SCORE GLOBAL: {total_passed}/{total_tests} ({round(total_passed/total_tests*100)}%)")
    print(f"  {'=' * 50}")
    
    if total_passed == total_tests:
        print("\n  ✓ TOUS LES TESTS PASSENT - Système de profilage validé!")
    elif total_passed >= total_tests * 0.9:
        print("\n  ⚠ SYSTÈME GLOBALEMENT BON - Quelques ajustements mineurs nécessaires")
    else:
        print("\n  ✗ ATTENTION - Des problèmes significatifs ont été détectés")
    
    return total_passed, total_tests


# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("VALIDATION COMPLÈTE DU SYSTÈME DE PROFILAGE RE'ACTIF PRO")
    print("=" * 70)
    
    import logging
    logging.getLogger().setLevel(logging.WARNING)  # Réduire le bruit des logs
    
    all_results = {}
    
    # Exécuter tous les tests
    all_results["mbti"] = test_all_16_mbti_profiles()
    all_results["filieres"] = test_filieres_by_mbti_group()
    all_results["jobs"] = test_jobs_by_mbti_group()
    all_results["vertus"] = test_mbti_vertu_coherence()
    all_results["enneagram"] = test_enneagram_vertu_mapping()
    all_results["discrimination"] = test_score_discrimination()
    
    # Rapport final
    total_passed, total_tests = generate_final_report(all_results)
    
    # Exit code
    if total_passed >= total_tests * 0.9:
        exit(0)
    else:
        exit(1)
