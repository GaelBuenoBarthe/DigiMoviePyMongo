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
git clone <URL_DU_DEPOT>
cd <NOM_DU_DEPOT>
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
### 6.