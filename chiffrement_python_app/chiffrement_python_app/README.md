# 🔐 Interface de Chiffrement - Python Backend

Application web de chiffrement César et Vernam avec backend Python Flask.

## 📦 Structure du projet

```
chiffrement_python_app/
├── app.py                  # Serveur Flask
├── chiffrement.py          # Algorithmes de chiffrement (votre code Python)
├── requirements.txt        # Dépendances Python
├── templates/
│   └── index.html         # Interface web
└── static/
    ├── style.css          # Styles CSS
    └── script.js          # JavaScript frontend
```

## 🚀 Installation et Lancement

### Étape 1 : Installer les dépendances

```bash
pip install -r requirements.txt
```

OU si vous avez des problèmes :

```bash
pip install Flask --break-system-packages
```

### Étape 2 : Lancer le serveur

```bash
python app.py
```

OU

```bash
python3 app.py
```

### Étape 3 : Ouvrir dans le navigateur

Ouvrez votre navigateur à l'adresse :
```
http://127.0.0.1:5000
```

## ✅ Fonctionnalités

- ✅ **Chiffrement César** avec clé numérique
- ✅ **Déchiffrement César**
- ✅ **Chiffrement Vernam** avec clé alphabétique
- ✅ **Déchiffrement Vernam**
- ✅ **Affichage des étapes** de transformation
- ✅ **Validation des données**
- ✅ **Backend Python** utilisant votre code original

## 🎯 Exemples d'utilisation

### César
- Texte : `BONJOUR`
- Clé : `3`
- Résultat : `ERQMRXU`

### Vernam
- Texte : `HELLO`
- Clé : `WORLD`
- Résultat : `DSCWR`

## 🔧 Arrêter le serveur

Appuyez sur `Ctrl + C` dans le terminal.

## 📝 Notes

- Le serveur tourne sur le port 5000 par défaut
- Tous les calculs sont effectués par Python (votre code original)
- L'interface web communique avec Python via des requêtes HTTP (API REST)
