import "@/App.css";
import { useState } from "react";
import { BrowserRouter, Routes, Route, Link, useNavigate } from "react-router-dom";
import { Sparkles, Heart, TrendingUp, Briefcase, ChevronRight, User, ArrowLeft, ArrowRight, CheckCircle } from "lucide-react";

// ============================================================================
// DE'CLIC PRO LOGO SVG
// ============================================================================
const DeclicProLogo = ({ size = 80 }) => (
  <svg width={size} height={size} viewBox="0 0 100 100">
    {/* Outer ellipse */}
    <ellipse cx="50" cy="50" rx="40" ry="45" fill="none" stroke="#2dd4bf" strokeWidth="2" opacity="0.6"/>
    
    {/* Center node */}
    <circle cx="50" cy="50" r="8" fill="#f97316"/>
    
    {/* Top node */}
    <circle cx="50" cy="15" r="6" fill="#3b82f6"/>
    <line x1="50" y1="21" x2="50" y2="42" stroke="#3b82f6" strokeWidth="2"/>
    
    {/* Bottom node */}
    <circle cx="50" cy="85" r="6" fill="#22c55e"/>
    <line x1="50" y1="79" x2="50" y2="58" stroke="#22c55e" strokeWidth="2"/>
    
    {/* Left top node */}
    <circle cx="20" cy="35" r="5" fill="#a855f7"/>
    <line x1="25" y1="38" x2="43" y2="47" stroke="#a855f7" strokeWidth="2"/>
    
    {/* Right top node */}
    <circle cx="80" cy="35" r="5" fill="#06b6d4"/>
    <line x1="75" y1="38" x2="57" y2="47" stroke="#06b6d4" strokeWidth="2"/>
    
    {/* Left bottom node */}
    <circle cx="20" cy="65" r="5" fill="#eab308"/>
    <line x1="25" y1="62" x2="43" y2="53" stroke="#eab308" strokeWidth="2"/>
    
    {/* Right bottom node */}
    <circle cx="80" cy="65" r="5" fill="#10b981"/>
    <line x1="75" y1="62" x2="57" y2="53" stroke="#10b981" strokeWidth="2"/>
  </svg>
);

// ============================================================================
// LANDING PAGE
// ============================================================================
const HomePage = () => {
  const features = [
    { icon: <Heart className="w-5 h-5" />, label: "Soft Skills", color: "from-orange-500 to-orange-400", border: "border-orange-500/50" },
    { icon: <Briefcase className="w-5 h-5" />, label: "Métiers", color: "from-blue-500 to-blue-400", border: "border-blue-500/50" },
    { icon: <Sparkles className="w-5 h-5" />, label: "Valeurs", color: "from-cyan-500 to-teal-400", border: "border-cyan-500/50" },
    { icon: <TrendingUp className="w-5 h-5" />, label: "Potentiel", color: "from-emerald-500 to-green-400", border: "border-emerald-500/50" },
  ];

  const steps = [
    { number: 1, title: "Questionnaire", description: "Répondez à des questions sur vos préférences, valeurs et comportements" },
    { number: 2, title: "Analyse", description: "Notre algorithme analyse vos réponses pour identifier vos forces" },
    { number: 3, title: "Carte d'identité Pro", description: "Découvrez votre profil complet : soft skills, valeurs, potentiel" },
    { number: 4, title: "Matching Métiers", description: "Explorez les métiers compatibles avec votre profil" }
  ];

  return (
    <div className="min-h-screen bg-[#0a1628]" data-testid="home-page">
      {/* Hero Section */}
      <section className="relative px-6 pt-16 pb-20 max-w-7xl mx-auto">
        <div className="grid lg:grid-cols-2 gap-12 items-center">
          {/* Left Content */}
          <div className="space-y-8">
            {/* Logo and Title */}
            <div className="flex items-center gap-4">
              <DeclicProLogo size={80} />
              <div>
                <h1 className="text-4xl md:text-5xl font-extrabold">
                  <span className="gradient-text-declic">DE'CLIC PRO</span>
                </h1>
                <p className="text-gray-400 text-sm tracking-widest mt-1">L'APPLY RE'ACTIF PRO</p>
              </div>
            </div>

            <div className="space-y-4">
              <h2 className="text-2xl md:text-3xl font-bold text-white">
                Découvrez votre potentiel professionnel
              </h2>
              <p className="text-gray-400 text-lg leading-relaxed">
                Un parcours personnalisé pour identifier vos soft skills, vos valeurs et les métiers qui vous correspondent.
              </p>
            </div>

            <p className="text-lg">
              <span className="text-orange-500 font-bold">TOTALEMENT ANONYME</span>
              <span className="text-gray-400"> et </span>
              <span className="text-green-500 font-bold">GRATUIT</span>
              <span className="text-gray-400"> en moins de 5 mn.</span>
            </p>

            {/* CTA Buttons */}
            <div className="flex flex-col sm:flex-row gap-4">
              <Link 
                to="/questionnaire" 
                className="btn-gradient-declic px-8 py-4 rounded-xl font-semibold text-white inline-flex items-center justify-center gap-2"
                data-testid="start-questionnaire-btn"
              >
                <Sparkles className="w-5 h-5" />
                Commencer le questionnaire
              </Link>
              <Link 
                to="/carte-identite" 
                className="btn-dark px-8 py-4 rounded-xl font-semibold text-gray-300 inline-flex items-center justify-center gap-2"
                data-testid="view-identity-card-btn"
              >
                <User className="w-5 h-5" />
                Voir ma carte d'identité Pro
              </Link>
            </div>
          </div>

          {/* Right Side - Feature Badges */}
          <div className="relative flex justify-center lg:justify-end">
            <div className="flex flex-col gap-4">
              {features.map((feature, index) => (
                <div 
                  key={index}
                  className={`feature-badge bg-gradient-to-r ${feature.color} ${feature.border}`}
                  style={{ 
                    marginLeft: index === 0 ? '60px' : index === 1 ? '120px' : index === 2 ? '100px' : '40px',
                    animationDelay: `${index * 0.2}s`
                  }}
                  data-testid={`feature-${feature.label.toLowerCase().replace(' ', '-')}`}
                >
                  {feature.icon}
                  <span className="font-semibold">{feature.label}</span>
                </div>
              ))}
            </div>
          </div>
        </div>
      </section>

      {/* Separator */}
      <div className="max-w-6xl mx-auto px-6">
        <div className="h-px bg-gradient-to-r from-transparent via-gray-700 to-transparent" />
      </div>

      {/* Steps Section */}
      <section className="relative px-6 py-20 max-w-4xl mx-auto" data-testid="steps-section">
        <h2 className="text-3xl md:text-4xl font-bold text-center mb-16 text-white">
          Votre parcours en 4 étapes
        </h2>

        <div className="space-y-6">
          {steps.map((step, index) => (
            <div 
              key={step.number}
              className="step-card"
              data-testid={`step-${step.number}`}
            >
              <div className="step-number-declic">
                {step.number}
              </div>
              <div className="flex-1">
                <h3 className="text-xl font-semibold text-white mb-1">{step.title}</h3>
                <p className="text-gray-400">{step.description}</p>
              </div>
              <CheckCircle className="w-6 h-6 text-gray-600" />
            </div>
          ))}
        </div>
      </section>

      {/* CTA Section */}
      <section className="relative px-6 py-16 max-w-4xl mx-auto text-center" data-testid="cta-section">
        <div className="cta-card">
          <h2 className="text-2xl md:text-3xl font-bold text-white mb-4">
            Prêt à découvrir votre potentiel ?
          </h2>
          <p className="text-gray-400 text-lg mb-8">
            Le questionnaire prend environ 5 minutes. Vos réponses sont confidentielles.
          </p>
          <Link 
            to="/questionnaire" 
            className="btn-gradient-declic px-10 py-4 rounded-xl font-semibold text-white inline-flex items-center justify-center gap-2 text-lg"
            data-testid="cta-start-btn"
          >
            Démarrer maintenant
            <ChevronRight className="w-5 h-5" />
          </Link>
        </div>
      </section>

      {/* Footer */}
      <footer className="relative px-6 py-8 text-center text-gray-500 text-sm">
        <p>© 2026 DE'CLIC PRO - Intelligence Professionnelle</p>
      </footer>
    </div>
  );
};

// ============================================================================
// QUESTIONNAIRE PAGE
// ============================================================================
const questions = [
  {
    id: 1,
    category: "soft_skills",
    question: "Face à un problème complexe, quelle est votre première réaction ?",
    options: [
      { value: "analytical", label: "Je décompose le problème en parties plus petites", trait: "Esprit analytique" },
      { value: "creative", label: "Je cherche des solutions innovantes et originales", trait: "Créativité" },
      { value: "collaborative", label: "Je consulte mes collègues pour avoir différents avis", trait: "Collaboration" },
      { value: "decisive", label: "Je prends rapidement une décision et j'agis", trait: "Prise de décision" }
    ]
  },
  {
    id: 2,
    category: "soft_skills",
    question: "Comment préférez-vous communiquer dans un contexte professionnel ?",
    options: [
      { value: "written", label: "Par écrit, pour être précis et garder une trace", trait: "Communication écrite" },
      { value: "verbal", label: "À l'oral, pour des échanges plus dynamiques", trait: "Communication orale" },
      { value: "visual", label: "Avec des supports visuels et des présentations", trait: "Communication visuelle" },
      { value: "listening", label: "J'écoute d'abord avant de m'exprimer", trait: "Écoute active" }
    ]
  },
  {
    id: 3,
    category: "values",
    question: "Qu'est-ce qui vous motive le plus au travail ?",
    options: [
      { value: "impact", label: "Avoir un impact positif sur la société", trait: "Impact social" },
      { value: "growth", label: "Apprendre et progresser continuellement", trait: "Développement personnel" },
      { value: "autonomy", label: "Être autonome et gérer mes propres projets", trait: "Autonomie" },
      { value: "recognition", label: "Être reconnu pour mon travail et mes compétences", trait: "Reconnaissance" }
    ]
  },
  {
    id: 4,
    category: "values",
    question: "Quel environnement de travail vous correspond le mieux ?",
    options: [
      { value: "structured", label: "Un cadre structuré avec des processus clairs", trait: "Structure" },
      { value: "flexible", label: "Un environnement flexible et adaptable", trait: "Flexibilité" },
      { value: "innovative", label: "Une culture d'innovation et d'expérimentation", trait: "Innovation" },
      { value: "collaborative", label: "Une équipe soudée avec une forte entraide", trait: "Esprit d'équipe" }
    ]
  },
  {
    id: 5,
    category: "potential",
    question: "Comment gérez-vous la pression et les deadlines serrées ?",
    options: [
      { value: "calm", label: "Je reste calme et méthodique", trait: "Gestion du stress" },
      { value: "energized", label: "La pression me stimule et me rend plus productif", trait: "Résilience" },
      { value: "organized", label: "Je m'organise et priorise les tâches", trait: "Organisation" },
      { value: "delegating", label: "Je délègue et mobilise mon équipe", trait: "Leadership" }
    ]
  },
  {
    id: 6,
    category: "potential",
    question: "Face au changement, comment réagissez-vous ?",
    options: [
      { value: "embracing", label: "J'accueille le changement comme une opportunité", trait: "Adaptabilité" },
      { value: "cautious", label: "Je prends le temps d'analyser avant de m'adapter", trait: "Prudence" },
      { value: "proactive", label: "J'initie souvent le changement moi-même", trait: "Proactivité" },
      { value: "supportive", label: "J'aide les autres à s'adapter au changement", trait: "Empathie" }
    ]
  },
  {
    id: 7,
    category: "career",
    question: "Quel type de tâches vous épanouit le plus ?",
    options: [
      { value: "strategic", label: "Définir des stratégies et planifier à long terme", trait: "Vision stratégique" },
      { value: "operational", label: "Exécuter et concrétiser des projets", trait: "Sens opérationnel" },
      { value: "relational", label: "Développer des relations et négocier", trait: "Relationnel" },
      { value: "technical", label: "Résoudre des problèmes techniques complexes", trait: "Expertise technique" }
    ]
  },
  {
    id: 8,
    category: "career",
    question: "Comment envisagez-vous votre évolution professionnelle ?",
    options: [
      { value: "management", label: "Évoluer vers des responsabilités managériales", trait: "Leadership" },
      { value: "expertise", label: "Devenir expert reconnu dans mon domaine", trait: "Expertise" },
      { value: "entrepreneurship", label: "Créer ma propre activité ou entreprise", trait: "Entrepreneuriat" },
      { value: "versatility", label: "Diversifier mes compétences et expériences", trait: "Polyvalence" }
    ]
  }
];

const QuestionnairePage = () => {
  const [currentQuestion, setCurrentQuestion] = useState(0);
  const [answers, setAnswers] = useState({});
  const [isComplete, setIsComplete] = useState(false);
  const navigate = useNavigate();

  const progress = ((currentQuestion + 1) / questions.length) * 100;
  const question = questions[currentQuestion];

  const handleAnswer = (value) => {
    const selectedOption = question.options.find(opt => opt.value === value);
    setAnswers(prev => ({
      ...prev,
      [question.id]: { value, trait: selectedOption.trait, category: question.category }
    }));
  };

  const handleNext = () => {
    if (currentQuestion < questions.length - 1) {
      setCurrentQuestion(prev => prev + 1);
    } else {
      // Save to localStorage
      const profile = {
        soft_skills: Object.values(answers).filter(a => a.category === 'soft_skills').map(a => a.trait),
        values: Object.values(answers).filter(a => a.category === 'values').map(a => a.trait),
        potentials: Object.values(answers).filter(a => a.category === 'potential' || a.category === 'career').map(a => a.trait),
      };
      localStorage.setItem('profile', JSON.stringify(profile));
      setIsComplete(true);
    }
  };

  const handlePrevious = () => {
    if (currentQuestion > 0) {
      setCurrentQuestion(prev => prev - 1);
    }
  };

  if (isComplete) {
    return (
      <div className="min-h-screen bg-[#0a1628] flex items-center justify-center px-6" data-testid="questionnaire-complete">
        <div className="text-center space-y-8 max-w-lg">
          <div className="w-24 h-24 mx-auto rounded-full bg-gradient-to-br from-green-400 to-emerald-500 flex items-center justify-center">
            <CheckCircle className="w-12 h-12 text-white" />
          </div>
          <h1 className="text-4xl font-bold text-white">Questionnaire terminé !</h1>
          <p className="text-gray-400 text-lg">
            Votre profil professionnel a été généré avec succès.
          </p>
          <Link
            to="/carte-identite"
            className="btn-gradient-declic px-8 py-4 rounded-xl font-semibold text-white inline-flex items-center justify-center gap-2"
            data-testid="view-results-btn"
          >
            Voir mes résultats
            <ChevronRight className="w-5 h-5" />
          </Link>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-[#0a1628]" data-testid="questionnaire-page">
      {/* Header */}
      <header className="px-6 py-6 flex items-center justify-between max-w-4xl mx-auto">
        <Link to="/" className="flex items-center gap-2 text-gray-400 hover:text-white transition-colors" data-testid="back-home-link">
          <ArrowLeft className="w-5 h-5" />
          <span>Retour</span>
        </Link>
        <span className="text-gray-400 text-sm">
          Question {currentQuestion + 1} sur {questions.length}
        </span>
      </header>

      {/* Progress Bar */}
      <div className="max-w-4xl mx-auto px-6 mb-12">
        <div className="h-2 bg-gray-800 rounded-full overflow-hidden">
          <div 
            className="progress-bar-declic h-full rounded-full transition-all duration-500"
            style={{ width: `${progress}%` }}
            data-testid="progress-bar"
          />
        </div>
      </div>

      {/* Question Card */}
      <main className="max-w-3xl mx-auto px-6 pb-20">
        <div className="question-card-declic" data-testid={`question-${question.id}`}>
          <div className="mb-8">
            <span className="text-sm text-orange-400 font-medium uppercase tracking-wider">
              {question.category === 'soft_skills' && 'Compétences'}
              {question.category === 'values' && 'Valeurs'}
              {question.category === 'potential' && 'Potentiel'}
              {question.category === 'career' && 'Carrière'}
            </span>
            <h2 className="text-2xl md:text-3xl font-bold text-white mt-2">
              {question.question}
            </h2>
          </div>

          <div className="space-y-4">
            {question.options.map((option) => (
              <button
                key={option.value}
                onClick={() => handleAnswer(option.value)}
                className={`answer-option-declic w-full text-left ${
                  answers[question.id]?.value === option.value ? 'selected' : ''
                }`}
                data-testid={`option-${option.value}`}
              >
                <div className="flex items-center gap-4">
                  <div className={`w-6 h-6 rounded-full border-2 flex items-center justify-center transition-all ${
                    answers[question.id]?.value === option.value 
                      ? 'border-orange-500 bg-orange-500' 
                      : 'border-gray-600'
                  }`}>
                    {answers[question.id]?.value === option.value && (
                      <div className="w-2 h-2 bg-white rounded-full" />
                    )}
                  </div>
                  <span className="text-gray-200">{option.label}</span>
                </div>
              </button>
            ))}
          </div>

          {/* Navigation */}
          <div className="flex justify-between mt-10 pt-6 border-t border-gray-700">
            <button
              onClick={handlePrevious}
              disabled={currentQuestion === 0}
              className="px-6 py-3 rounded-xl font-medium text-gray-400 hover:text-white disabled:opacity-30 disabled:cursor-not-allowed transition-colors flex items-center gap-2"
              data-testid="prev-question-btn"
            >
              <ArrowLeft className="w-4 h-4" />
              Précédent
            </button>
            <button
              onClick={handleNext}
              disabled={!answers[question.id]}
              className="btn-gradient-declic px-8 py-3 rounded-xl font-semibold text-white flex items-center gap-2 disabled:opacity-50 disabled:cursor-not-allowed"
              data-testid="next-question-btn"
            >
              {currentQuestion === questions.length - 1 ? (
                <>Terminer <CheckCircle className="w-4 h-4" /></>
              ) : (
                <>Suivant <ArrowRight className="w-4 h-4" /></>
              )}
            </button>
          </div>
        </div>
      </main>
    </div>
  );
};

// ============================================================================
// CARTE IDENTITE PAGE
// ============================================================================
const defaultProfile = {
  soft_skills: ["Esprit analytique", "Communication orale", "Organisation", "Adaptabilité"],
  values: ["Impact social", "Flexibilité", "Développement personnel", "Esprit d'équipe"],
  potentials: ["Gestion du stress", "Proactivité", "Vision stratégique", "Expertise"],
};

const defaultJobs = [
  { title: "Chef de projet", compatibility: 92, sector: "Management" },
  { title: "Consultant", compatibility: 88, sector: "Conseil" },
  { title: "Product Manager", compatibility: 85, sector: "Tech" },
  { title: "Responsable RH", compatibility: 82, sector: "Ressources Humaines" },
  { title: "Entrepreneur", compatibility: 78, sector: "Entrepreneuriat" }
];

const CarteIdentitePage = () => {
  const storedProfile = localStorage.getItem('profile');
  const profile = storedProfile ? JSON.parse(storedProfile) : defaultProfile;

  const getPotentialScore = (index) => {
    const scores = [95, 88, 82, 75];
    return scores[index] || 70;
  };

  return (
    <div className="min-h-screen bg-[#0a1628] pb-20" data-testid="carte-identite-page">
      {/* Header */}
      <header className="px-6 py-6 flex items-center justify-between max-w-6xl mx-auto">
        <Link to="/" className="flex items-center gap-2 text-gray-400 hover:text-white transition-colors" data-testid="back-home-link">
          <ArrowLeft className="w-5 h-5" />
          <span>Retour</span>
        </Link>
      </header>

      <main className="max-w-6xl mx-auto px-6">
        {/* Title */}
        <div className="text-center mb-12">
          <h1 className="text-4xl md:text-5xl font-bold">
            <span className="gradient-text-declic">Carte d'identité Pro</span>
          </h1>
          <p className="text-gray-400 mt-4">Votre profil professionnel personnalisé</p>
        </div>

        <div className="grid lg:grid-cols-2 gap-8">
          {/* Left Column */}
          <div className="space-y-6">
            {/* Soft Skills */}
            <div className="card-declic" data-testid="soft-skills-section">
              <div className="flex items-center gap-3 mb-6">
                <div className="p-3 rounded-xl bg-gradient-to-br from-orange-500 to-amber-400">
                  <Heart className="w-6 h-6 text-white" />
                </div>
                <h2 className="text-2xl font-bold text-white">Soft Skills</h2>
              </div>
              <div className="flex flex-wrap gap-3">
                {profile.soft_skills.map((skill, index) => (
                  <span key={index} className="skill-badge-declic" data-testid={`skill-${index}`}>
                    {skill}
                  </span>
                ))}
              </div>
            </div>

            {/* Values */}
            <div className="card-declic" data-testid="values-section">
              <div className="flex items-center gap-3 mb-6">
                <div className="p-3 rounded-xl bg-gradient-to-br from-cyan-500 to-teal-400">
                  <Sparkles className="w-6 h-6 text-white" />
                </div>
                <h2 className="text-2xl font-bold text-white">Valeurs</h2>
              </div>
              <div className="flex flex-wrap gap-3">
                {profile.values.map((value, index) => (
                  <span key={index} className="value-badge-declic" data-testid={`value-${index}`}>
                    {value}
                  </span>
                ))}
              </div>
            </div>

            {/* Potential */}
            <div className="card-declic" data-testid="potential-section">
              <div className="flex items-center gap-3 mb-6">
                <div className="p-3 rounded-xl bg-gradient-to-br from-emerald-500 to-green-400">
                  <TrendingUp className="w-6 h-6 text-white" />
                </div>
                <h2 className="text-2xl font-bold text-white">Potentiel</h2>
              </div>
              <div className="space-y-4">
                {profile.potentials.map((potential, index) => (
                  <div key={index} data-testid={`potential-${index}`}>
                    <div className="flex justify-between mb-2">
                      <span className="text-gray-300">{potential}</span>
                      <span className="text-emerald-400 font-semibold">{getPotentialScore(index)}%</span>
                    </div>
                    <div className="h-2 bg-gray-700 rounded-full overflow-hidden">
                      <div 
                        className="h-full bg-gradient-to-r from-emerald-500 to-green-400 rounded-full transition-all duration-1000"
                        style={{ width: `${getPotentialScore(index)}%` }}
                      />
                    </div>
                  </div>
                ))}
              </div>
            </div>
          </div>

          {/* Right Column - Jobs */}
          <div className="space-y-6">
            <div className="card-declic" data-testid="jobs-section">
              <div className="flex items-center gap-3 mb-6">
                <div className="p-3 rounded-xl bg-gradient-to-br from-blue-500 to-indigo-400">
                  <Briefcase className="w-6 h-6 text-white" />
                </div>
                <h2 className="text-2xl font-bold text-white">Métiers compatibles</h2>
              </div>
              
              <div className="space-y-4">
                {defaultJobs.map((job, index) => (
                  <div key={index} className="job-card-declic" data-testid={`job-${index}`}>
                    <div className="flex justify-between items-start mb-3">
                      <div>
                        <h3 className="text-lg font-semibold text-white">{job.title}</h3>
                        <span className="text-gray-500 text-sm">{job.sector}</span>
                      </div>
                      <span className={`px-3 py-1 rounded-full text-sm font-semibold ${
                        job.compatibility >= 85 ? 'bg-emerald-500/20 text-emerald-400' : 'bg-amber-500/20 text-amber-400'
                      }`}>
                        {job.compatibility}% match
                      </span>
                    </div>
                    <div className="h-2 bg-gray-700 rounded-full overflow-hidden">
                      <div 
                        className="h-full bg-gradient-to-r from-blue-500 to-indigo-400 rounded-full"
                        style={{ width: `${job.compatibility}%` }}
                      />
                    </div>
                  </div>
                ))}
              </div>
            </div>

            {/* CTA */}
            <div className="card-declic text-center" data-testid="cta-card">
              <h3 className="text-xl font-bold text-white mb-3">Pas encore répondu au questionnaire ?</h3>
              <p className="text-gray-400 mb-6">Découvrez votre véritable profil professionnel</p>
              <Link 
                to="/questionnaire"
                className="btn-gradient-declic px-8 py-3 rounded-xl font-semibold text-white inline-block"
                data-testid="start-questionnaire-link"
              >
                Faire le questionnaire
              </Link>
            </div>
          </div>
        </div>
      </main>
    </div>
  );
};

// ============================================================================
// APP
// ============================================================================
function App() {
  return (
    <div className="App min-h-screen">
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/questionnaire" element={<QuestionnairePage />} />
          <Route path="/carte-identite" element={<CarteIdentitePage />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
