# Fort Boyard Game
Fort Boyard Simulator 
Projet EFREI TI101 - Programmation en Python

## 1. Présentation Générale

### Contributeurs
- Jacky Zhang
- Amadéo Berthelot

### Description
Pour un projet d’école en programmation Python, on a créé un mini-jeu inspiré de Fort Boyard. Le but étant de réussir différentes épreuves pour gagner des clés et accéder à la salle au trésor.

### Fonctionnalités Principales
- Epreuve du Père Fouras, enigmes de mathématiques, de logique et de hasard.
- Fonctions principales gérant le déroulement du jeu


### Technologies Utilisées
- *Langages de programmation : Python 
- *Bibliothèques : time, random, json et math
- *Outils :pyCharm, github

### Installation

#### Prérequis :
Python 3.9+, pip 

#### Instructions pour cloner le dépôt Git
ouvrir le cmd (ou terminal)

git clone https://github.com/amadeo-dev/pyfort-Zhang-Berthelot-c.git  

cd Fort-Boyard-Simulator

## 2. Documentation Technique
### Algorithme du jeu :
Une fontion principale (main.py) gère le déroulement du jeu :
1. Elle demande de composer une équime de max 3 personnes
2. Demande le nom, profession et role de chaque joueur
3. Demande quel epreuve le joueur souhaite réaliser et la lance
4. Elle comptabilise combien de clés ont étés récoltées et si les joueurs sont victorieux
   
### Détails des fonctions implémentées :

Le projet se sépare en trois groupe de fonctions :
- chaque jeu à une fonction qui ne prend rien en parametre mais retourne un bolléen (vrai -> le joueur a gagné et inversement)
- les fonctions 'utiles', où on retrouve la création d'équipe ainsi que le menu des epreuves 
- la fonction principale jeu() qui renvoie permet de créer son équipe et choisir l'épreuve et renvoie "L'équipe remporte" ou "L'équipe perd"

### Gestion des Entrées et Erreurs :

Le code est conçu pour gérer les entrées utilisateur avec robustesse :
* Les choix de menu et saisies des joueurs sont validés pour éviter les entrées incorrectes. Par exemple, le menu des épreuves refuse tout choix en dehors des options disponibles.
* Pour les jeux nécessitant des positions (comme le morpion), les entrées sont vérifiées pour s’assurer qu’elles sont dans les limites autorisées.

## 3. Journal de Bord
### Chronologie du Projet :
On a avancé à notre rythme pendant les séances de projet python, pas de problèmes rencontrés

### Répartition des Tâches:
 Nous nous sommes répartis le travail en plusieurs taches, pour plus de simplicité nous avons chacun réaliser 2 ou 3 mini-jeux en plus duquel on a fait soit la fonction_utiles soit la main fonction.
## 4. Tests et Validation
### Stratégies de Test :
On a tester séparement chaque fonction au fur et à mesure, et une fois le projet finalisé c'est l'ensemble du jeu que nous avons finaliser.  
Pour accélerer le processus de test nous remplacions directement les 'input' par une valeur

§ Capturesd'écranmontrantlestestsenaction.
