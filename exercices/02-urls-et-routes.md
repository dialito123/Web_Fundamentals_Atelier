# 🟢 Exercice 2 — Les URL et les routes

⏱️ ~15 minutes · [⬅️ Exercice précédent](01-premier-deploiement.md) · [Exercice suivant ➡️](03-html.md)

## 🎯 Ce que vous allez découvrir

Chaque page d'un site possède une **adresse** unique : son **URL**. Décortiquons-en une :

```
https://alice42.pythonanywhere.com/presentation
└─┬─┘   └──────────┬────────────┘└─────┬─────┘
protocole    nom de domaine         chemin
             (le serveur)       (la page demandée)
```

Côté serveur, Flask associe chaque **chemin** à une fonction Python. C'est ce qu'on appelle une **route**.

## 🛠️ À faire

1. Dans `flask_app.py`, sous le commentaire `Ajoutez vos nouvelles routes ci-dessous 👇`, ajoutez :
   ```python
   @app.get("/presentation")
   def presentation():
       return "Je m'appelle Harris et je suis étudiante en informatique."
   ```
   ⚠️ Respectez bien les **4 espaces** au début de la ligne `return` : en Python, c'est important !
2. Faites un *commit*, attendez le ✅, puis visitez `https://votre-username.pythonanywhere.com/presentation`.
3. Ajoutez vous-même une troisième route, `/loisirs`, qui affiche vos loisirs.

## 👀 À observer

- Visitez une page qui **n'existe pas**, par exemple `/blabla`. Que vous répond le serveur ?
- Essayez `/Presentation` (avec une majuscule). Est-ce la même page ?
- Essayez `/presentation/` (avec un `/` à la fin). Que se passe-t-il ?

## 📝 Questions (à noter dans `CARNET.md`)

1. Dans l'URL `https://www.google.com/maps`, quel est le nom de domaine ? Quel est le chemin ?
2. Que veut dire le message *Not Found* ? Qui l'a envoyé : votre navigateur ou le serveur ?
3. Que se passe-t-il si deux fonctions portent le même nom dans `flask_app.py` ? (Indice : essayez, puis lisez l'Error log.)
