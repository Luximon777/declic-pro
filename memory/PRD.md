# DE'CLIC PRO - PRD

## Projet
Plateforme d'orientation professionnelle guidant les utilisateurs à travers un questionnaire multi-modèles (MBTI, DISC, Ennéagramme, RIASEC, Archéologie des Compétences) pour déterminer leur profil de personnalité et recommander des métiers compatibles.

**URL**: https://declicpro-eval.preview.emergentagent.com

---

## Ce qui a été implémenté

### Février 2026 - Session actuelle (24/02/2026)
- ✅ **Intégration TABLEAU CK** : Données du fichier TABLEAU CK.ods intégrées dans le moteur de scoring
  - Nouveau dictionnaire `TABLEAU_CK` avec hiérarchie complète par vertu
  - `ARCHEOLOGIE_COMPETENCES` enrichi avec compétences sociales, pro transférables, qualités CK
  - `VERTUS` enrichi avec sous-vertus, valeurs universelles, compétences sociales/pro
  - `score_archeologie` utilise les compétences sociales et pro transférables CK
- ✅ **Redesign UI (reactif.pro)** : Nouvelle identité visuelle alignée sur reactif.pro
  - Palette : bleu marine #1e3a5f (fond), bleu #4f6df5 (accent), #6c5ce7 (secondaire)
  - Police : Outfit + Plus Jakarta Sans
  - Remplacement complet des couleurs orange par bleu dans CSS et JSX

### Décembre 2025 - Session 4 (09/12/2025)
- ✅ Ajustement poids MBTI 20% → 35%
- ✅ Tests de régression 89/89 (100%)
- ✅ Filtre niveau d'études (6 niveaux)
- ✅ ENTJ ajouté aux métiers techniques

### Mars 2026 - Sessions précédentes
- ✅ Intégration IA Claude Sonnet 4.5 pour fiches métiers
- ✅ Cache MongoDB pour fiches IA
- ✅ Mapping MBTI → Vertu corrigé
- ✅ Bug fix vertu par défaut
- ✅ Archéologie des compétences bidirectionnelle
- ✅ UX/UI Designer reclassifié (Sagesse)
- ✅ Pénalisation MBTI incompatibles
- ✅ Score filières basé sur métiers contenus

---

## Architecture Technique

### Stack
- **Frontend**: React 18 + Tailwind CSS + Shadcn/UI
- **Backend**: FastAPI (Python)
- **Base de données**: MongoDB
- **IA**: Claude Sonnet 4.5 via Emergent LLM Key

### Structure fichiers clés
```
/app/
├── backend/
│   ├── server.py           # ~7400 lignes - API + logique scoring
│   ├── esco_api.py
│   ├── france_travail_api.py
│   └── tests/
│       ├── test_full_profiling_validation.py
│       └── test_infj_psychologue.py
├── frontend/src/
│   ├── App.js              # ~3700 lignes
│   └── App.css             # ~8000 lignes (redesigné)
├── tableau_ck.ods          # Données source TABLEAU CK
├── tableau_ck1.xlsx        # Version enrichie
└── archeologie_competences.ods
```

### Collections MongoDB
- `test_results` : Résultats avec code d'accès
- `ai_job_cache` : Cache fiches IA

---

## Endpoints API

- `POST /api/job-match` - Matching métiers (retourne access_code)
- `POST /api/explore` - Exploration filières
- `POST /api/retrieve-results` - Récupérer résultats via code
- `GET /api/questionnaire` - Questions du questionnaire

---

## Prochaines tâches (P1)

- [ ] Refactoring backend server.py (>7400 lignes) → modulariser
- [ ] Refactoring frontend App.js (>3700 lignes) → composants
- [ ] Export PDF de la carte d'identité Pro
- [ ] Partage sur réseaux sociaux

---

## Backlog (P2)

- API France Travail (bloquée - erreur 403 externe)
- Dashboard administrateur
- Notifications email
- Historique des questionnaires
- Système de badges/gamification
- Espace Entreprise RH
- Espace Partenaires Sociaux

---

## Conformité RGPD/AI Act
- ✅ Questionnaire anonyme (pas d'identité obligatoire)
- ✅ Données séparées
- ✅ Code d'accès pour récupération résultats
