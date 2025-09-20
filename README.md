<p align="center">
  <a href="https://github.com/Patricklalaina/index_file_extractor" target="_blank">
    <img alt="IndexOf Downloader" src="https://img.shields.io/badge/index_file_extractor-%F0%9F%93%82-blue?style=flat-square" />
  </a>
</p>

# 📂 Extracteur de fichiers depuis "Index of/"

Un script Python permettant de télécharger automatiquement des fichiers
depuis des répertoires listés en mode **Index of/** sur des sites web.

## 🚀 Fonctionnalités

-   Exploration automatique des pages **Index of/**.\
-   Extraction et téléchargement de fichiers.\
-   Affichage d'une **barre de progression** grâce à `tqdm`.\

## 📦 Installation

### 1. Cloner le dépôt

``` bash
git clone https://github.com/Patricklalaina/index_file_extractor.git
cd index_file_extractor
```

### 2. Créer un environnement virtuel (optionnel mais recommandé)

``` bash
python3 -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
```

### 3. Installer les dépendances

``` bash
pip3 install -r requirements.txt
```

### 4. Fichier `requirements.txt`

Ce fichier contient :

    beautifulsoup4
    requests
    tqdm

(`os` et `sys` sont inclus nativement avec Python.)

## 🖥️ Utilisation

``` bash
python3 index.py <url_index_of>
```

### Exemple

``` bash
python index.py http://example.com/files/
```

➡️ Tous les fichiers disponibles dans l'index seront téléchargés dans
le dossier courant.

## ⚠️ Avertissement

Ce projet est conçu à des fins éducatives.\
⚠️ **N'utilisez pas cet outil pour télécharger du contenu sans
autorisation légale**.

------------------------------------------------------------------------

👨‍💻 Développé avec ❤️ en Python.
