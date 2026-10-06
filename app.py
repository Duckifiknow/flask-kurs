from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template ("index.html")

@app.route("/profil")
def profil():
    return "Her skal profiler vises"

@app.route("/prosjekter")
def prosjekter():
    return "her skal prosjekter vises"

@app.route("/kontakt")
def kontakt():
    return "kontaktinfo skal vises her"

if __name__ == "__main__":
    app.run(debug=True)