# DE'CLIC PRO - PRD (Product Requirements Document)

## Énoncé du problème original
Créer le site DE'CLIC PRO - Intelligence Professionnelle, une plateforme de découverte de potentiel professionnel avec un parcours personnalisé pour identifier les soft skills, valeurs et métiers compatibles.

## Architecture

### Stack technique
- **Frontend**: React 19 + Tailwind CSS + React Router
- **Backend**: FastAPI (Python)
- **Base de données**: MongoDB
- **Hébergement**: Emergent Platform

### Structure
```
/app
├── frontend/
│   └── src/
│       ├── App.js (routeur principal avec questionnaire visuel et résultats)
│       └── pages/
│           ├── HomePage.jsx
│           ├── QuestionnairePage.jsx
│           └── CarteIdentitePage.jsx
└── backend/
    └── server.py (API FastAPI avec algorithme de matching)
```

## Personas utilisateurs
1. **Jeunes diplômés** - Cherchent à découvrir leur orientation professionnelle
2. **Professionnels en reconversion** - Veulent identifier leurs compétences transférables
3. **Conseillers RH** - Utilisent l'outil pour accompagner les candidats

## Fonctionnalités principales (Core Requirements)

### Page d'accueil
- Logo DE'CLIC PRO avec gradient orange-vert
- 2 cartes CTA : "Je cherche mon job" et "Je cherche encore..."
- Phrase sur le questionnaire anonyme et gratuit
- Footer avec logos partenaires (Alt&Act, Ubuntoo, RE'ACTIF PRO, AI Act)

### Questionnaire (/questionnaire)
- Questions visuelles avec images
- Questions de classement (ranking 1-4)
- Barre de progression animée
- Champ date de naissance
- Navigation Précédent/Suivant

### Page Résultats
- Profil de personnalité (DISC, Ennéagramme, MBTI)
- Cadran d'Ofman (zones de vigilance)
- Liste des métiers compatibles avec scores
- Narratif personnalisé généré par IA

### API Backend
- `POST /api/job-match` - Matching métier avec profil
- `POST /api/explore` - Exploration des filières
- `GET /api/questionnaire/visual` - Questions visuelles
- `GET /api/metiers` - Liste des métiers

## Ce qui a été implémenté

### Décembre 2025
- [x] Bug fix critique: Algorithme de recherche de métiers (12 déc 2025)
  - Correction de `search_job_by_query` pour normaliser le texte (accents, parenthèses)
  - Correction de l'endpoint `/api/job-match` pour préserver la pertinence de recherche
- [x] Nouveau métier: "Chargé(e) de recrutement" (M033) ajouté à la base de données
  - Profil DISC: I, S (Influence, Stabilité)
  - Ennéagramme compatible: 2, 3, 7
  - MBTI compatible: ENFJ, ENFP, ESFJ, ENTJ
  - Variantes de recherche: recruteur, talent acquisition, chasseur de têtes

### Mars 2026 (sessions précédentes)
- [x] Page d'accueil complète avec design glassmorphism
- [x] Thème sombre avec gradients orange-vert
- [x] Questionnaire interactif avec questions visuelles
- [x] Carte d'identité Pro avec profil personnalisé
- [x] API de création de profil MongoDB
- [x] Algorithme de matching métiers (DISC + Ennéagramme + MBTI + environnement)
- [x] Animations et transitions CSS
- [x] Design responsive mobile/desktop

## Backlog priorisé

### P0 (Critique) - Fait ✅
- Toutes les fonctionnalités core sont implémentées
- Bug de matching métiers corrigé

### P1 (Important)
- [ ] Export PDF de la carte d'identité Pro
- [ ] Partage sur réseaux sociaux
- [ ] Historique des questionnaires complétés
- [ ] Authentification utilisateur

### P2 (Nice to have)
- [ ] Dashboard administrateur
- [ ] Statistiques d'utilisation
- [ ] Intégration API France Travail (actuellement mockée)
- [ ] Personnalisation des questions
- [ ] Intégration IA avancée pour analyse plus poussée

## Prochaines tâches
1. Implémenter l'export PDF de la carte d'identité
2. Ajouter la fonctionnalité de partage social
3. Créer un système d'authentification utilisateur
4. Configurer l'API France Travail pour enrichir les données métiers

## Notes techniques

### Algorithme de recherche de métiers
Le système utilise une fonction `normalize_text` pour:
- Supprimer les accents (normalisation Unicode NFD)
- Supprimer les caractères spéciaux (parenthèses, etc.)
- Ignorer les mots vides (de, du, le, la, etc.)

L'endpoint `/api/job-match` préserve la pertinence de recherche pour `best_match` tout en affichant les alternatives triées par compatibilité de profil dans `other_matches`.

### Scoring des métiers
Basé sur 6 critères pondérés:
- Motivation (Ennéagramme): 25%
- Style DISC: 20%
- Personnalité MBTI: 15%
- Environnement de travail: 20%
- Compétences: 15%
- Contraintes: 5%
