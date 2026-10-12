from flask import Flask, render_template
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
    fagliste = ["Python", "Flask", "HTML", "CSS"]
    return render_template(
        "plan.html",
        fag = fagliste
        )

@app.route("/kontakt")
def kontakt():
    return "kontaktinfo skal vises her"

if __name__ == "__main__":
    app.run(debug=True)