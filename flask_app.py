from flask import Flask, render_template, request, redirect, abort

app = Flask(__name__)


@app.get("/")
def accueil():
    return render_template("accueil.html")


@app.get("/presentation")
def presentation():
    return render_template(
        "presentation.html",
        prenom="Harris",
        nom="Diallo",
        loisirs=["Jeux vidéo", "Musique", "Réseaux / Sécurité"],
    )


@app.get("/bonjour/<prenom>")
def bonjour(prenom):
    return render_template("bonjour.html", prenom=prenom)


@app.get("/calcul")
def calcul():
    op = request.args.get("op", "plus")
    try:
        a = int(request.args.get("a", 0))
        b = int(request.args.get("b", 0))
    except ValueError:
        return (
            "Erreur : les paramètres 'a' et 'b' doivent être des nombres entiers.",
            400,
        )

    if op == "fois":
        return f"{a} × {b} = {a * b}"
    elif op == "moins":
        return f"{a} - {b} = {a - b}"
    elif op == "div":
        return (
            f"{a} ÷ {b} = {a / b}"
            if b != 0
            else "Erreur : division par zéro impossible."
        )
    else:
        return f"{a} + {b} = {a + b}"


# --- Exercice 8 : Formulaires (GET et POST) ---
@app.get("/formulaire")
def formulaire():
    return render_template("formulaire.html")


@app.route("/salut", methods=["GET", "POST"])
def salut():
    if request.method == "POST":
        prenom = request.form.get("prenom", "inconnu")
        ville = request.form.get("ville", "nulle part")
        couleur = request.form.get("couleur", "black")
    else:
        prenom = request.args.get("prenom", "inconnu")
        ville = request.args.get("ville", "nulle part")
        couleur = request.args.get("couleur", "black")

    return f"""
    <h1 style="color: {couleur};">Bonjour {prenom}, qui vient de {ville} !</h1>
    <p>Données reçues en méthode <strong>{request.method}</strong>.</p>
    <p><a href="/formulaire">Retour au formulaire</a></p>
    """
# 3xx : une redirection
@app.get("/home")
def home():
    return redirect("/")


# 4xx : un accès interdit
@app.get("/secret")
def secret():
    abort(403)


# Une page d'erreur 404 personnalisée
@app.errorhandler(404)
def page_introuvable(erreur):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
