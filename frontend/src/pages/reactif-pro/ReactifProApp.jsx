import React, { useState, useEffect } from 'react';
import { 
  User, Building2, Users, ArrowRight, Shield, Key, 
  LayoutDashboard, FileText, Target, Settings, LogOut,
  ChevronLeft, Eye, EyeOff, Check, AlertCircle, Loader2,
  Layers, Compass, Network, Globe, Map, TrendingUp,
  Briefcase, Heart, Award, Zap, CheckCircle2, Sparkles
} from 'lucide-react';
import { Button } from '../../components/ui/button';
import { Input } from '../../components/ui/input';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '../../components/ui/card';
import './ReactifPro.css';

const API_URL = process.env.REACT_APP_BACKEND_URL;

// ============================================================================
// LANDING PAGE RE'ACTIF PRO - NOUVELLE VERSION
// ============================================================================
const ReactifProLanding = ({ onSelectAccess }) => {
  const [activeTab, setActiveTab] = useState('presentation');

  return (
    <div className="reactif-landing-new">
      {/* Header */}
      <header className="reactif-header-new">
        <div className="reactif-header-content">
          <img src="/reactif-pro-logo-full.png" alt="RE'ACTIF PRO" className="reactif-logo-new" />
          <div className="reactif-header-text">
            <h1>RE'ACTIF PRO</h1>
            <p>Intelligence Professionnelle</p>
          </div>
        </div>
      </header>

      {/* Main Layout: Content + Sidebar */}
      <div className="reactif-main-layout">
        {/* Left Content - Tabs */}
        <div className="reactif-content-area">
          {/* Navigation Tabs */}
          <nav className="reactif-tabs">
            <button 
              className={`reactif-tab ${activeTab === 'presentation' ? 'active' : ''}`}
              onClick={() => setActiveTab('presentation')}
            >
              Présentation
            </button>
            <button 
              className={`reactif-tab ${activeTab === 'outils' ? 'active' : ''}`}
              onClick={() => setActiveTab('outils')}
            >
              Nos Outils
            </button>
          </nav>

          {/* Tab Content */}
          <div className="reactif-tab-content">
            {activeTab === 'presentation' && <PresentationTab />}
            {activeTab === 'outils' && <OutilsTab />}
          </div>
        </div>

        {/* Right Sidebar - Access Cards */}
        <aside className="reactif-sidebar-access">
          <h2>Accès à la plateforme</h2>
          
          {/* Accès Particulier */}
          <Card 
            className="sidebar-access-card access-pro"
            onClick={() => onSelectAccess('pro')}
            data-testid="access-pro"
          >
            <CardHeader>
              <div className="sidebar-access-icon pro">
                <User size={24} />
              </div>
              <CardTitle>Accès Particulier</CardTitle>
            </CardHeader>
            <CardContent>
              <p>Espace personnel confidentiel sous pseudonyme</p>
              <Button className="sidebar-access-btn pro-btn">
                Accéder <ArrowRight size={16} />
              </Button>
            </CardContent>
          </Card>

          {/* Accès Entreprises RH */}
          <Card 
            className="sidebar-access-card access-rh"
            onClick={() => onSelectAccess('rh')}
            data-testid="access-rh"
          >
            <CardHeader>
              <div className="sidebar-access-icon rh">
                <Building2 size={24} />
              </div>
              <CardTitle>Entreprises RH</CardTitle>
            </CardHeader>
            <CardContent>
              <p>Espace dédié aux professionnels RH</p>
              <Button className="sidebar-access-btn rh-btn" disabled>
                Bientôt disponible
              </Button>
            </CardContent>
          </Card>

          {/* Accès Partenaires Sociaux */}
          <Card 
            className="sidebar-access-card access-partners"
            onClick={() => onSelectAccess('partners')}
            data-testid="access-partners"
          >
            <CardHeader>
              <div className="sidebar-access-icon partners">
                <Users size={24} />
              </div>
              <CardTitle>Partenaires Sociaux</CardTitle>
            </CardHeader>
            <CardContent>
              <p>Consultation et collaboration</p>
              <Button className="sidebar-access-btn partners-btn" disabled>
                Bientôt disponible
              </Button>
            </CardContent>
          </Card>

          {/* Privacy Badge */}
          <div className="sidebar-privacy-badge">
            <Shield size={16} />
            <span>Données protégées</span>
          </div>
        </aside>
      </div>
    </div>
  );
};

// ============================================================================
// TAB: PRÉSENTATION
// ============================================================================
const PresentationTab = () => {
  return (
    <div className="presentation-content">
      <div className="presentation-hero">
        <h2>Plateforme d'accompagnement professionnel personnalisé</h2>
        <p className="presentation-intro">
          RE'ACTIF PRO est une solution innovante qui combine l'intelligence artificielle 
          et l'accompagnement humain pour garantir votre <strong>employabilité tout au long de la vie</strong>.
        </p>
      </div>

      {/* Logos partenaires */}
      <div className="partners-logos">
        <img src="/logo-altact.png" alt="Alt&Act" className="partner-logo" />
        <img src="/logo-ubuntoo.png" alt="Ubuntoo" className="partner-logo" />
        <img src="/reactif-pro-logo-full.png" alt="RE'ACTIF PRO" className="partner-logo" />
        <img src="/logo-ia-act.jpeg" alt="AI Act" className="partner-logo" />
      </div>

      {/* Points clés */}
      <div className="presentation-features">
        <div className="feature-card">
          <div className="feature-icon"><Target size={24} /></div>
          <h3>Job Matching Intelligent</h3>
          <p>Au-delà des compétences déclarées, vers le potentiel réel</p>
        </div>
        <div className="feature-card">
          <div className="feature-icon"><Shield size={24} /></div>
          <h3>IA Éthique & Explicable</h3>
          <p>Transparence des algorithmes et protection des données</p>
        </div>
        <div className="feature-card">
          <div className="feature-icon"><Users size={24} /></div>
          <h3>Accompagnement Hybride</h3>
          <p>Technologie au service de l'humain, jamais en substitut</p>
        </div>
        <div className="feature-card">
          <div className="feature-icon"><TrendingUp size={24} /></div>
          <h3>Vision Évolutive</h3>
          <p>Projection des trajectoires professionnelles possibles</p>
        </div>
      </div>

      {/* Différenciation */}
      <div className="presentation-differentiation">
        <h3><Award size={20} /> Notre différenciation</h3>
        <ul>
          <li><CheckCircle2 size={16} /> Sortir du matching déclaratif</li>
          <li><CheckCircle2 size={16} /> Intégrer la dimension axiologique (sens, valeurs)</li>
          <li><CheckCircle2 size={16} /> Identifier les écarts avec micro-actions correctives</li>
          <li><CheckCircle2 size={16} /> Valoriser le potentiel plutôt que le passé</li>
        </ul>
        <p className="differentiation-conclusion">
          <Zap size={16} /> Le job matching devient un <strong>outil d'orientation active</strong> et non plus seulement de placement.
        </p>
      </div>
    </div>
  );
};

// ============================================================================
// TAB: NOS OUTILS
// ============================================================================
const OutilsTab = () => {
  return (
    <div className="outils-content">
      {/* NIVEAU 1 - FONDATION */}
      <div className="outils-level">
        <div className="level-header level-1">
          <div className="level-icon"><Layers size={24} /></div>
          <div className="level-info">
            <span className="level-tag">NIVEAU 1</span>
            <h3>FONDATION</h3>
            <p>Vision & Cadre Structurant</p>
          </div>
        </div>

        <div className="outils-grid">
          <div className="outil-card">
            <div className="outil-header">
              <User size={20} />
              <h4>Profil Utilisateur Dynamique</h4>
            </div>
            <p>Le dispositif repose sur un profil enrichi intégrant :</p>
            <ul>
              <li><Briefcase size={14} /> Compétences techniques</li>
              <li><Users size={14} /> Soft skills</li>
              <li><Heart size={14} /> Valeurs et motivations</li>
              <li><TrendingUp size={14} /> Potentiel d'adaptation</li>
              <li><Target size={14} /> Secteur de "gravité professionnelle"</li>
            </ul>
          </div>

          <div className="outil-card">
            <div className="outil-header">
              <Network size={20} />
              <h4>Logique d'Écosystème</h4>
            </div>
            <p>Le matching positionne la personne dans :</p>
            <ul>
              <li><Globe size={14} /> Un écosystème métiers</li>
              <li><Building2 size={14} /> Des secteurs compatibles</li>
              <li><Map size={14} /> Des trajectoires possibles</li>
              <li><Sparkles size={14} /> Des métiers émergents ou hybrides</li>
            </ul>
          </div>

          <div className="outil-card accent-blue">
            <div className="outil-header">
              <Eye size={20} />
              <h4>Observatoire des Compétences Prédictif</h4>
            </div>
            <p>Le job matching est connecté à :</p>
            <ul className="check-list">
              <li><CheckCircle2 size={14} /> Observatoire dynamique des compétences</li>
              <li><CheckCircle2 size={14} /> Analyse des usages réels sur le terrain</li>
              <li><CheckCircle2 size={14} /> Identification des compétences hybrides</li>
              <li><CheckCircle2 size={14} /> Anticipation des besoins futurs</li>
            </ul>
          </div>

          <div className="outil-card">
            <div className="outil-header">
              <Compass size={20} />
              <h4>Parcours d'accompagnement hybride</h4>
            </div>
            <ul className="check-list">
              <li><CheckCircle2 size={14} /> Accompagnement humain + technologie</li>
              <li><CheckCircle2 size={14} /> Diagnostic global complet</li>
              <li><CheckCircle2 size={14} /> Analyse des freins et leviers</li>
              <li><CheckCircle2 size={14} /> Plan d'action individualisé</li>
            </ul>
          </div>
        </div>
      </div>

      {/* NIVEAU 2 - DISPOSITIFS OPÉRATIONNELS */}
      <div className="outils-level">
        <div className="level-header level-2">
          <div className="level-icon"><Settings size={24} /></div>
          <div className="level-info">
            <span className="level-tag">NIVEAU 2</span>
            <h3>DISPOSITIFS OPÉRATIONNELS</h3>
            <p>Outils & Méthodes</p>
          </div>
        </div>

        <div className="outils-grid grid-3">
          <div className="outil-card">
            <div className="outil-header">
              <User size={20} />
              <h4>Dispositif VSI</h4>
            </div>
            <p className="outil-subtitle">Valoriser Son Identité</p>
            <ul className="check-list">
              <li><CheckCircle2 size={14} /> Diagnostic compétences visibles/invisibles</li>
              <li><CheckCircle2 size={14} /> Travail sur posture et identité</li>
              <li><CheckCircle2 size={14} /> Développement de la confiance</li>
              <li><CheckCircle2 size={14} /> Consolidation du projet</li>
            </ul>
          </div>

          <div className="outil-card">
            <div className="outil-header">
              <Users size={20} />
              <h4>Ateliers & Programmes</h4>
            </div>
            <p className="outil-subtitle">Formations collectives</p>
            <ul className="check-list">
              <li><CheckCircle2 size={14} /> Développement des soft skills</li>
              <li><CheckCircle2 size={14} /> Simulation d'entretiens</li>
              <li><CheckCircle2 size={14} /> Narration professionnelle</li>
              <li><CheckCircle2 size={14} /> Outils numériques</li>
            </ul>
          </div>

          <div className="outil-card">
            <div className="outil-header">
              <Map size={20} />
              <h4>Cartographie Interactive</h4>
            </div>
            <p className="outil-subtitle">Visualisation des parcours</p>
            <ul className="check-list">
              <li><CheckCircle2 size={14} /> Visualisation profil ↔ métiers</li>
              <li><CheckCircle2 size={14} /> Identification de passerelles</li>
              <li><CheckCircle2 size={14} /> Compétences transférables</li>
              <li><CheckCircle2 size={14} /> Projection sectorielle</li>
            </ul>
          </div>
        </div>
      </div>

      {/* NIVEAU 3 - IMPACT & ÉCOSYSTÈME */}
      <div className="outils-level">
        <div className="level-header level-3">
          <div className="level-icon"><Globe size={24} /></div>
          <div className="level-info">
            <span className="level-tag">NIVEAU 3</span>
            <h3>IMPACT & ÉCOSYSTÈME</h3>
            <p>Dimension Collective</p>
          </div>
        </div>

        <div className="outils-grid">
          <div className="outil-card wide accent-green">
            <div className="outil-header">
              <Network size={20} />
              <h4>Réseau RE'ACTIF PRO</h4>
            </div>
            <p>Une communauté active de professionnels, conseillers et partenaires engagés dans la transformation du marché de l'emploi.</p>
            <div className="outil-stats">
              <div className="stat"><span className="stat-value">3</span><span className="stat-label">Espaces dédiés</span></div>
              <div className="stat"><span className="stat-value">IA</span><span className="stat-label">Éthique & explicable</span></div>
              <div className="stat"><span className="stat-value">100%</span><span className="stat-label">Anonyme</span></div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

// ============================================================================
// AUTHENTIFICATION - CONNEXION / INSCRIPTION
// ============================================================================
const AuthPage = ({ onBack, onAuthSuccess }) => {
  const [isLogin, setIsLogin] = useState(true);
  const [showPassword, setShowPassword] = useState(false);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  
  // Champs du formulaire
  const [pseudo, setPseudo] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [emailRecovery, setEmailRecovery] = useState('');
  const [accessCode, setAccessCode] = useState('');
  const [consentCgu, setConsentCgu] = useState(false);
  const [consentPrivacy, setConsentPrivacy] = useState(false);
  const [consentMarketing, setConsentMarketing] = useState(false);

  const handleLogin = async (e) => {
    e.preventDefault();
    setError('');
    setLoading(true);

    try {
      const response = await fetch(`${API_URL}/api/reactif/auth/login`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ pseudo, password })
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.detail || 'Erreur de connexion');
      }

      // Stocker le token et les infos utilisateur
      localStorage.setItem('reactif_token', data.token);
      localStorage.setItem('reactif_user', JSON.stringify(data.user));
      onAuthSuccess(data.user);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const handleRegister = async (e) => {
    e.preventDefault();
    setError('');

    // Validations
    if (password !== confirmPassword) {
      setError('Les mots de passe ne correspondent pas');
      return;
    }
    if (password.length < 8) {
      setError('Le mot de passe doit contenir au moins 8 caractères');
      return;
    }
    if (!consentCgu || !consentPrivacy) {
      setError('Vous devez accepter les CGU et la politique de confidentialité');
      return;
    }

    setLoading(true);

    try {
      const response = await fetch(`${API_URL}/api/reactif/auth/register`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          pseudo,
          password,
          email_recovery: emailRecovery || null,
          access_code: accessCode || null,
          consent_cgu: consentCgu,
          consent_privacy: consentPrivacy,
          consent_marketing: consentMarketing
        })
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.detail || 'Erreur lors de l\'inscription');
      }

      // Stocker le token et les infos utilisateur
      localStorage.setItem('reactif_token', data.token);
      localStorage.setItem('reactif_user', JSON.stringify(data.user));
      onAuthSuccess(data.user);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="reactif-auth-page">
      <Button variant="ghost" onClick={onBack} className="auth-back-btn">
        <ChevronLeft size={20} /> Retour
      </Button>

      <div className="auth-container">
        <div className="auth-header">
          <User size={40} className="auth-icon" />
          <h2>{isLogin ? 'Connexion' : 'Créer un compte'}</h2>
          <p className="auth-subtitle">
            {isLogin 
              ? 'Connecte-toi avec ton pseudonyme' 
              : 'Crée ton espace personnel confidentiel'}
          </p>
        </div>

        {!isLogin && (
          <div className="auth-reassurance">
            <Shield size={16} />
            <p>
              Tu peux utiliser ce service sous pseudonyme.<br/>
              Ton identité civile n'est pas requise pour créer un compte.<br/>
              Seules les données strictement nécessaires sont collectées.
            </p>
          </div>
        )}

        {error && (
          <div className="auth-error">
            <AlertCircle size={16} />
            <span>{error}</span>
          </div>
        )}

        <form onSubmit={isLogin ? handleLogin : handleRegister} className="auth-form">
          {/* Pseudonyme */}
          <div className="form-group">
            <label htmlFor="pseudo">Pseudonyme *</label>
            <Input
              id="pseudo"
              type="text"
              value={pseudo}
              onChange={(e) => setPseudo(e.target.value)}
              placeholder="Ton pseudonyme"
              required
              minLength={3}
              maxLength={50}
              data-testid="input-pseudo"
            />
          </div>

          {/* Mot de passe */}
          <div className="form-group">
            <label htmlFor="password">Mot de passe *</label>
            <div className="password-input-wrapper">
              <Input
                id="password"
                type={showPassword ? 'text' : 'password'}
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                placeholder="Ton mot de passe"
                required
                minLength={8}
                data-testid="input-password"
              />
              <button 
                type="button" 
                className="password-toggle"
                onClick={() => setShowPassword(!showPassword)}
              >
                {showPassword ? <EyeOff size={18} /> : <Eye size={18} />}
              </button>
            </div>
          </div>

          {/* Champs supplémentaires pour l'inscription */}
          {!isLogin && (
            <>
              {/* Confirmation mot de passe */}
              <div className="form-group">
                <label htmlFor="confirmPassword">Confirmer le mot de passe *</label>
                <Input
                  id="confirmPassword"
                  type={showPassword ? 'text' : 'password'}
                  value={confirmPassword}
                  onChange={(e) => setConfirmPassword(e.target.value)}
                  placeholder="Confirme ton mot de passe"
                  required
                  minLength={8}
                  data-testid="input-confirm-password"
                />
              </div>

              {/* Email de récupération (facultatif) */}
              <div className="form-group optional">
                <label htmlFor="emailRecovery">
                  Email de récupération <span className="optional-badge">Facultatif</span>
                </label>
                <Input
                  id="emailRecovery"
                  type="email"
                  value={emailRecovery}
                  onChange={(e) => setEmailRecovery(e.target.value)}
                  placeholder="Pour récupérer ton accès si besoin"
                  data-testid="input-email"
                />
              </div>

              {/* Code d'accès DE'CLIC PRO (facultatif) */}
              <div className="form-group optional">
                <label htmlFor="accessCode">
                  Code d'accès DE'CLIC PRO <span className="optional-badge">Facultatif</span>
                </label>
                <Input
                  id="accessCode"
                  type="text"
                  value={accessCode}
                  onChange={(e) => setAccessCode(e.target.value.toUpperCase())}
                  placeholder="XXXX-XXXX"
                  maxLength={9}
                  data-testid="input-access-code"
                />
                <p className="form-hint">
                  <Key size={12} /> Si tu as passé le test DE'CLIC PRO, entre ton code pour récupérer tes résultats
                </p>
              </div>

              {/* Consentements */}
              <div className="consent-section">
                <label className="consent-checkbox">
                  <input
                    type="checkbox"
                    checked={consentCgu}
                    onChange={(e) => setConsentCgu(e.target.checked)}
                    required
                    data-testid="consent-cgu"
                  />
                  <span>J'accepte les <a href="/cgu" target="_blank">Conditions Générales d'Utilisation</a> *</span>
                </label>

                <label className="consent-checkbox">
                  <input
                    type="checkbox"
                    checked={consentPrivacy}
                    onChange={(e) => setConsentPrivacy(e.target.checked)}
                    required
                    data-testid="consent-privacy"
                  />
                  <span>J'ai lu et j'accepte la <a href="/privacy" target="_blank">Politique de Confidentialité</a> *</span>
                </label>

                <label className="consent-checkbox optional">
                  <input
                    type="checkbox"
                    checked={consentMarketing}
                    onChange={(e) => setConsentMarketing(e.target.checked)}
                    data-testid="consent-marketing"
                  />
                  <span>J'accepte de recevoir des informations sur les services RE'ACTIF PRO</span>
                </label>
              </div>
            </>
          )}

          <Button 
            type="submit" 
            className="auth-submit-btn"
            disabled={loading}
            data-testid="auth-submit"
          >
            {loading ? (
              <><Loader2 size={18} className="animate-spin" /> Chargement...</>
            ) : (
              isLogin ? 'Se connecter' : 'Créer mon compte'
            )}
          </Button>
        </form>

        <div className="auth-switch">
          {isLogin ? (
            <p>Pas encore de compte ? <button onClick={() => setIsLogin(false)}>Créer un compte</button></p>
          ) : (
            <p>Déjà un compte ? <button onClick={() => setIsLogin(true)}>Se connecter</button></p>
          )}
        </div>
      </div>
    </div>
  );
};

// ============================================================================
// DASHBOARD - ESPACE PERSONNEL
// ============================================================================
const Dashboard = ({ user, onLogout }) => {
  const [activeSection, setActiveSection] = useState('overview');

  const handleLogout = () => {
    localStorage.removeItem('reactif_token');
    localStorage.removeItem('reactif_user');
    onLogout();
  };

  return (
    <div className="reactif-dashboard">
      {/* Sidebar */}
      <aside className="dashboard-sidebar">
        <div className="sidebar-header">
          <img src="/reactif-pro-logo-full.png" alt="RE'ACTIF PRO" className="sidebar-logo" />
          <div className="user-info">
            <User size={20} />
            <span className="user-pseudo">{user?.pseudo || 'Utilisateur'}</span>
          </div>
        </div>

        <nav className="sidebar-nav">
          <button 
            className={`nav-item ${activeSection === 'overview' ? 'active' : ''}`}
            onClick={() => setActiveSection('overview')}
          >
            <LayoutDashboard size={18} /> Tableau de bord
          </button>
          <button 
            className={`nav-item ${activeSection === 'parcours' ? 'active' : ''}`}
            onClick={() => setActiveSection('parcours')}
          >
            <FileText size={18} /> Mes parcours
          </button>
          <button 
            className={`nav-item ${activeSection === 'results' ? 'active' : ''}`}
            onClick={() => setActiveSection('results')}
          >
            <Target size={18} /> Mes résultats
          </button>
          <button 
            className={`nav-item ${activeSection === 'settings' ? 'active' : ''}`}
            onClick={() => setActiveSection('settings')}
          >
            <Settings size={18} /> Paramètres
          </button>
        </nav>

        <div className="sidebar-footer">
          <button className="logout-btn" onClick={handleLogout}>
            <LogOut size={18} /> Déconnexion
          </button>
        </div>
      </aside>

      {/* Main Content */}
      <main className="dashboard-main">
        {activeSection === 'overview' && (
          <DashboardOverview user={user} />
        )}
        {activeSection === 'parcours' && (
          <DashboardParcours user={user} />
        )}
        {activeSection === 'results' && (
          <DashboardResults user={user} />
        )}
        {activeSection === 'settings' && (
          <DashboardSettings user={user} onLogout={handleLogout} />
        )}
      </main>
    </div>
  );
};

// ============================================================================
// DASHBOARD SECTIONS
// ============================================================================
const DashboardOverview = ({ user }) => {
  return (
    <div className="dashboard-section overview">
      <h1>Bienvenue, {user?.pseudo} !</h1>
      <p className="section-subtitle">Voici un aperçu de ton espace professionnel</p>

      <div className="overview-cards">
        <Card className="overview-card">
          <CardHeader>
            <CardTitle>Profil complété</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="progress-circle">
              <span className="progress-value">{user?.profile_completion || 0}%</span>
            </div>
          </CardContent>
        </Card>

        <Card className="overview-card">
          <CardHeader>
            <CardTitle>Tests réalisés</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="stat-value">{user?.tests_completed || 0}</div>
          </CardContent>
        </Card>

        <Card className="overview-card">
          <CardHeader>
            <CardTitle>Projets en cours</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="stat-value">{user?.active_projects || 0}</div>
          </CardContent>
        </Card>
      </div>

      <div className="quick-actions">
        <h2>Actions rapides</h2>
        <div className="actions-grid">
          <Button className="action-btn">
            Passer le test DE'CLIC PRO
          </Button>
          <Button className="action-btn" variant="outline">
            Créer un projet professionnel
          </Button>
          <Button className="action-btn" variant="outline">
            Importer un résultat
          </Button>
        </div>
      </div>
    </div>
  );
};

const DashboardParcours = ({ user }) => {
  return (
    <div className="dashboard-section parcours">
      <h1>Mes parcours</h1>
      <p className="section-subtitle">Suivi de tes questionnaires et parcours</p>
      
      <div className="empty-state">
        <FileText size={48} />
        <p>Aucun parcours pour le moment</p>
        <Button>Commencer un nouveau parcours</Button>
      </div>
    </div>
  );
};

const DashboardResults = ({ user }) => {
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchResults();
  }, []);

  const fetchResults = async () => {
    try {
      const token = localStorage.getItem('reactif_token');
      const response = await fetch(`${API_URL}/api/reactif/user/results`, {
        headers: { 'Authorization': `Bearer ${token}` }
      });
      if (response.ok) {
        const data = await response.json();
        setResults(data.results || []);
      }
    } catch (err) {
      console.error('Erreur chargement résultats:', err);
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return (
      <div className="dashboard-section results loading">
        <Loader2 size={32} className="animate-spin" />
        <p>Chargement des résultats...</p>
      </div>
    );
  }

  return (
    <div className="dashboard-section results">
      <h1>Mes résultats</h1>
      <p className="section-subtitle">Résultats de tes tests et analyses</p>
      
      {results.length === 0 ? (
        <div className="empty-state">
          <Target size={48} />
          <p>Aucun résultat pour le moment</p>
          <p className="hint">Passe le test DE'CLIC PRO ou importe tes résultats avec un code d'accès</p>
          <Button>Passer le test DE'CLIC PRO</Button>
        </div>
      ) : (
        <div className="results-list">
          {results.map((result, idx) => (
            <Card key={idx} className="result-card">
              <CardHeader>
                <CardTitle>{result.title || 'Résultat DE\'CLIC PRO'}</CardTitle>
                <CardDescription>{new Date(result.created_at).toLocaleDateString('fr-FR')}</CardDescription>
              </CardHeader>
              <CardContent>
                <p>MBTI: {result.content?.profile_summary?.mbti}</p>
                <Button variant="outline" size="sm">Voir le détail</Button>
              </CardContent>
            </Card>
          ))}
        </div>
      )}
    </div>
  );
};

const DashboardSettings = ({ user, onLogout }) => {
  return (
    <div className="dashboard-section settings">
      <h1>Paramètres</h1>
      <p className="section-subtitle">Gère ton compte et tes préférences</p>

      <div className="settings-cards">
        <Card className="settings-card">
          <CardHeader>
            <CardTitle>Informations du compte</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="info-row">
              <span className="label">Pseudonyme</span>
              <span className="value">{user?.pseudo}</span>
            </div>
            <div className="info-row">
              <span className="label">Email de récupération</span>
              <span className="value">{user?.email_recovery || 'Non renseigné'}</span>
            </div>
            <div className="info-row">
              <span className="label">Membre depuis</span>
              <span className="value">{user?.created_at ? new Date(user.created_at).toLocaleDateString('fr-FR') : 'N/A'}</span>
            </div>
          </CardContent>
        </Card>

        <Card className="settings-card">
          <CardHeader>
            <CardTitle>Confidentialité</CardTitle>
          </CardHeader>
          <CardContent>
            <Button variant="outline">Télécharger mes données</Button>
            <Button variant="outline" className="danger">Supprimer mon compte</Button>
          </CardContent>
        </Card>
      </div>
    </div>
  );
};

// ============================================================================
// APP PRINCIPALE RE'ACTIF PRO
// ============================================================================
const ReactifProApp = () => {
  const [currentView, setCurrentView] = useState('landing'); // landing, auth, dashboard
  const [selectedAccess, setSelectedAccess] = useState(null);
  const [user, setUser] = useState(null);

  // Vérifier si l'utilisateur est déjà connecté
  useEffect(() => {
    const token = localStorage.getItem('reactif_token');
    const savedUser = localStorage.getItem('reactif_user');
    
    if (token && savedUser) {
      try {
        setUser(JSON.parse(savedUser));
        setCurrentView('dashboard');
      } catch (e) {
        localStorage.removeItem('reactif_token');
        localStorage.removeItem('reactif_user');
      }
    }
  }, []);

  const handleSelectAccess = (access) => {
    setSelectedAccess(access);
    if (access === 'pro') {
      setCurrentView('auth');
    }
    // Les autres accès sont désactivés pour l'instant
  };

  const handleAuthSuccess = (userData) => {
    setUser(userData);
    setCurrentView('dashboard');
  };

  const handleLogout = () => {
    setUser(null);
    setCurrentView('landing');
  };

  const handleBackToLanding = () => {
    setCurrentView('landing');
    setSelectedAccess(null);
  };

  return (
    <div className="reactif-pro-app">
      {currentView === 'landing' && (
        <ReactifProLanding onSelectAccess={handleSelectAccess} />
      )}
      {currentView === 'auth' && (
        <AuthPage 
          onBack={handleBackToLanding} 
          onAuthSuccess={handleAuthSuccess}
        />
      )}
      {currentView === 'dashboard' && (
        <Dashboard 
          user={user} 
          onLogout={handleLogout}
        />
      )}
    </div>
  );
};

export default ReactifProApp;
