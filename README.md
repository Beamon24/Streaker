🌟 Streaker : Suivi Minimaliste d'Habitudes  
🎯 Aperçu du Projet  
Streaker est une application mobile minimaliste développée en Python pour aider les utilisateurs à 
construire et maintenir de bonnes habitudes (les "streaks" ou séries).  

L'objectif principal est de fournir une interface utilisateur native simple (grâce à Toga) permettant de :   
  1- Enregistrer rapidement de nouvelles habitudes.  
  2- Marquer chaque habitude comme complétée quotidiennement.  
  3- Visualiser la série (streak) de succès consécutifs.  
  
Technologie Frontend: Toga (BeeWare)  
Langage Backend: Python 3.x  
État du Développement: En cours (Phase de structure d'interface et de connexion au modèle)  
Tuto apprendre BeeWare : https://youtu.be/FhDJniaFQ0M?si=x-dFG77PmGX_avn9  

🛠️ Stack Technique  
Langage : Python 3.x  
Framework Mobile : BeeWare (avec Toga pour l'interface utilisateur native).  
Outil de Packaging/Déploiement : Briefcase (Fait partie de BeeWare).  
Base de Données (Futures versions) : SQLite (gestion par le Développeur A).  

💻 Instructions de Lancement (Pour les Développeurs)  
Pour lancer et travailler sur ce projet, vous devez avoir Python 3.x et Git installés.   
Il est fortement recommandé d'utiliser un environnement virtuel.  

1. Cloner le Dépôt  
  git clone [URL_DE_VOTRE_DEPOT]  
  cd streaker  

2. Configuration de l'Environnement  
Crée et active l'environnement virtuel (méthode Linux/WSL)  
  python3 -m venv venv  
  source venv/bin/activate  
(Si vous êtes sur Windows PowerShell : .\venv\Scripts\activate)  

3. Installation des Dépendances  
Installez Briefcase pour la gestion du projet :  
  pip install briefcase  

4. Lancement sur le Bureau (Développement Rapide)  
Ceci lance l'application directement sur votre PC pour un développement rapide de l'interface :  
  briefcase run  

5. Lancement sur Android (Compilation APK)  
Briefcase gère la compilation vers Android. Assurez-vous d'avoir le SDK et le NDK Android installés  
(Briefcase vous guidera).  
Crée le projet Android  
  briefcase create android  
  
Construit l'APK  
  briefcase build android  
  
Installe et lance sur un émulateur ou un appareil connecté  
  briefcase run android  

🤝 Collaboration (Développeurs Alexis & Beamon24)  
Ce projet suit une séparation claire des responsabilités :  
  Développeur Alexis (Backend/Modèle) : Responsable de la logique de la base de données (SQLite),   
  du stockage des entrées/sorties, et du calcul du "Streak" (série consécutive de succès).  
  
  Développeur Beamon24 (Frontend/Vue) : Responsable de l'interface utilisateur (Toga),   
  de la gestion des layouts (dispositions), des boutons, de la saisie utilisateur,   
  et de la mise à jour dynamique de l'affichage.  
  
Points de Synchronisation Clés :  
  1. Ajout d'Habitude : Le Dév. Front appelle la fonction d'ajout du Dév. Back,   
  qui enregistre les données, avant de mettre à jour l'interface.  
  
  2. Affichage : Le Dév. Front interroge le Dév. Back pour obtenir la liste des habitudes   
  et leur état (y compris la valeur du streak) avant de rendre l'interface.  
