# ---------------------------------------------------------------
#  Mon premier site Web avec Flask
# ---------------------------------------------------------------
#  Ce fichier est le "cerveau" de votre site : c'est lui qui
#  reçoit les demandes des navigateurs et qui fabrique les réponses.
#
#  Vous allez le compléter petit à petit, exercice après exercice.
#  Les consignes sont dans le dossier "exercices/".
# ---------------------------------------------------------------
from flask import Flask, render_template, request

app = Flask(__name__)


# Une "route" associe une adresse (URL) à une fonction Python.
# Ici : quand quelqu'un visite la page d'accueil "/",
# Flask exécute la fonction accueil() et renvoie son résultat au navigateur.
@app.get("/")
def accueil():
    return render_template("accueil.html")


# ---------------------------------------------------------------
#  Ajoutez vos nouvelles routes ci-dessous 👇
# ---------------------------------------------------------------
@app.get("/bonjour/<prenom>")
def bonjour(prenom):
    # Pour éviter l'injection XSS, on utilise render_template qui échappe le code automatiquement
    return render_template("bonjour.html", prenom=prenom)


@app.get("/calcul")
def calcul():
    op = request.args.get("op", "plus")
    try:
        a = int(request.args.get("a", 0))
        b = int(request.args.get("b", 0))
    except ValueError:
        return "Erreur : les paramètres 'a' et 'b' doivent être des nombres entiers.", 400

    if op == "fois":
        return f"{a} × {b} = {a * b}"
    elif op == "moins":
        return f"{a} - {b} = {a - b}"
    elif op == "div":
        return f"{a} ÷ {b} = {a / b}" if b != 0 else "Erreur : division par zéro impossible."
    else:
        return f"{a} + {b} = {a + b}"
# ---------------------------------------------------------------
#  Ne pas modifier : utile seulement pour lancer le site
#  sur votre propre ordinateur (python flask_app.py)
# ---------------------------------------------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
