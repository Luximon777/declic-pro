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
│       ├── App.js (routeur principal)
│       └── pages/
│           ├── HomePage.jsx
│           ├── QuestionnairePage.jsx
│           └── CarteIdentitePage.jsx
└── backend/
    └── server.py (API FastAPI)
```

## Personas utilisateurs
1. **Jeunes diplômés** - Cherchent à découvrir leur orientation professionnelle
2. **Professionnels en reconversion** - Veulent identifier leurs compétences transférables
3. **Conseillers RH** - Utilisent l'outil pour accompagner les candidats

## Fonctionnalités principales (Core Requirements)

### Page d'accueil
- Hero section avec titre gradient "DE'CLIC PRO"
- 2 boutons CTA : "Commencer le questionnaire" et "Voir ma carte d'identité Pro"
- 4 feature pills : Soft Skills, Valeurs, Potentiel, Métiers
- Section "Votre parcours en 4 étapes" avec cartes animées

### Page Questionnaire (/questionnaire)
- 8 questions réparties en catégories (soft_skills, values, potential, career)
- Options de réponse avec radio buttons stylisés
- Barre de progression animée
- Navigation Précédent/Suivant
- Soumission automatique et redirection vers résultats

### Page Carte d'identité Pro (/carte-identite)
- Section Soft Skills avec badges
- Section Valeurs avec tags colorés
- Section Potentiel avec barres de progression
- Section Métiers compatibles avec % de match
- Boutons partage et téléchargement

### API Backend
- `POST /api/profile` - Créer un profil professionnel
- `GET /api/profile/{id}` - Récupérer un profil
- `POST /api/matching-jobs` - Obtenir les métiers compatibles
- `GET /api/jobs` - Liste de tous les métiers

## Ce qui a été implémenté
- [x] Page d'accueil complète avec design glassmorphism (3 mars 2026)
- [x] Questionnaire interactif avec 8 questions (3 mars 2026)
- [x] Carte d'identité Pro avec profil personnalisé (3 mars 2026)
- [x] API de création de profil MongoDB (3 mars 2026)
- [x] Algorithme de matching métiers (3 mars 2026)
- [x] Animations et transitions CSS (3 mars 2026)
- [x] Design responsive mobile/desktop (3 mars 2026)

## Backlog priorisé

### P0 (Critique) - Fait ✅
- Toutes les fonctionnalités core sont implémentées

### P1 (Important)
- [ ] Export PDF de la carte d'identité Pro
- [ ] Partage sur réseaux sociaux
- [ ] Historique des questionnaires complétés
- [ ] Authentification utilisateur

### P2 (Nice to have)
- [ ] Dashboard administrateur
- [ ] Statistiques d'utilisation
- [ ] Personnalisation des questions
- [ ] Intégration IA pour analyse plus poussée
- [ ] Mode sombre/clair switch

## Prochaines tâches
1. Implémenter l'export PDF de la carte d'identité
2. Ajouter la fonctionnalité de partage social
3. Créer un système d'authentification utilisateur
4. Sauvegarder l'historique des profils
