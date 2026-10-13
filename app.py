from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/profil")
def profil():
    
    return render_template(
        "om.html",
        navn="Alice",
        alder=18,
        klasse="2imi",
        fag="Informasjonsteknologi",
        favorittspråk="Engelsk",
        skole="Kuben",

        poeng = random.randint(0, 100)
        )

@app.route("/plan")
def plan():
    spillliste = ["Cyberpunk: 2077", "Fallout 4", "Terraria", "BG3", "Subnautica"]
    return render_template(
        "plan.html",
        spill = spillliste
        )

@app.route("/registrering", methods=["GET", "POST"])
def registrering():

    if request.method == "POST":
        navn = request.form["navn"]
        epost = request.form["epost"]
        alder = request.form["alder"]
        kommentar = request.form["kommentar"]

        return render_template(
            "resultat.html",
            navn=navn,
            epost=epost,
            alder=alder,
            kommentar=kommentar
        )

    return render_template("registrering.html")


@app.route("/kurs")
def kurs():
    kursliste = ["Python", "Flask", "Javascript", "Linux"]

    if request.method == "POST":
        kursliste = request.form["kurs"]

    return render_template("kurs.html", kursliste=kursliste)


if __name__ == "__main__":
    app.run(debug=True)