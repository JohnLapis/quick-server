from flask import Flask, render_template
import subprocess


app = Flask(__name__)


@app.route("/")
def index():
    poems = []
    all_poems = subprocess.run(
        ["node", "poem-scraper.js"], stdout=subprocess.PIPE
    ).stdout.decode()
    for poem in all_poems.split("====="):
        poem_lines = poem.strip().split("\n")
        poems.append(
            {
                "title": poem_lines[0],
                "text": poem_lines[2:],
            }
        )

    return render_template("base.html", poems=poems)
