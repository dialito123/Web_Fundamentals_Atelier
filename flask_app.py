from flask import Flask, render_template, request

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
        loisirs=["Jeux vidéo", "Musique", "Réseaux / Sécurité"]
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
        return "Erreur : les paramètres 'a' et 'b' doivent être des nombres entiers.", 400

    if op == "fois":
        return f"{a} × {b} = {a * b}"
    elif op == "moins":
        return f"{a} - {b} = {a - b}"
    elif op == "div":
        return f"{a} ÷ {b} = {a / b}" if b != 0 else "Erreur : division par zéro impossible."
    else:
        return f"{a} + {b} = {a + b}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
