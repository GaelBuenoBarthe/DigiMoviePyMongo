# Movie Database Project

## Description
Ce projet permet de créer et de remplir une base de données MongoDB avec des informations sur des films, des réalisateurs et des acteurs. Il utilise des scripts Python pour importer des données à partir d'un fichier CSV et effectuer des agrégations pour obtenir des statistiques sur les réalisateurs et les acteurs.

## Prérequis
- Python 3.x
- MongoDB

## Installation

### 1. Cloner le dépôt
Clonez ce dépôt sur votre machine locale :

```bash
git clone https://github.com/GaelBuenoBarthe/DigiMoviePyMongo.git
cd DigiMoviePyMongo
```
### 2. Créer un environnement virtuel
Créez un environnement virtuel pour isoler les dépendances du projet :
    
```bash
python -m venv venv
```
### 3. Activer l'environnement virtuel
Sur Windows :
venv\Scripts\activate
Sur macOS et Linux :
source venv/bin/activate

### 4. Installer les dépendances
Installez les dépendances nécessaires à partir du fichier requirements.txt :
    
```bash
pip install -r requirements.txt
```

### 5. Remplissage de la base de données
Configurer MongoDB
Assurez-vous que MongoDB est installé et en cours d'exécution sur votre machine.

. Exécuter le script load_data.py
Utilisez le script load_data.py pour lire les données du fichier CSV et les insérer dans la base de données MongoDB :
    
```bash
python load_data.py
```
### 6. Utilisation de main.py
Le script main.py permet d'accéder aux différentes fonctions du projet. Voici comment l'utiliser :  
1. Lancer main.py
Pour lancer le script main.py, exécutez :
        
```bash
python main.py
``` 
2. Interface disponible
    1. Agrégations des films :  
Cette option permet d'accéder aux différentes agrégations et statistiques sur les films, comme le top 5 des films les mieux notés.
    
    2. Agrégations des réalisateurs :  
Cette option permet d'accéder aux différentes agrégations et statistiques sur les réalisateurs, comme le top 5 des réalisateurs les mieux notés, ceux avec la plus longue durée moyenne des films, ou ceux ayant réalisé le plus de films.

    3. Créer ou modifier un film :  
Cette option permet de créer un nouveau film ou de modifier les informations d'un film existant dans la base de données.

    4. Créer ou modifier un réalisateur :  
Cette option permet de créer un nouveau réalisateur ou de modifier les informations d'un réalisateur existant dans la base de données.

    5. Agrégations des acteurs :  
Cette option permet d'accéder aux différentes agrégations et statistiques sur les acteurs, comme le top 15 des acteurs ayant joué dans le plus de films.

    6. Tapez 'exit' pour quitter :
Cette option permet de quitter le menu principal et de terminer l'exécution du script.