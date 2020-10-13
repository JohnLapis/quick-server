from flask import Flask, render_template
from scrapers import math_scraper


app = Flask(__name__)


@app.route("/")
def index():
    fact = math_scraper.main()
    return render_template("base.html", fact=fact)

@app.route("/<int:number>")
def number(number):
    fact = math_scraper.main(number)
    return render_template("base.html", fact=fact)


@app.route("/<name>")
def hello(name):
    return f"Oiiiii, {name}"
