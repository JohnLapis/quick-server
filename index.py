from flask import Flask, render_template
import markdown, subprocess


# app = Flask(__name__)

# @app.route("/")
def index():
    poems = []
    all_poems = subprocess.run(["node", "poem-scraper.js"], stdout=subprocess.PIPE).stdout.decode()
    for poem in all_poems.split("<ENDPOEM>"):
        poem_lines = poem.strip().split("\n")
        poems.append({
            "title": poem_lines[0],
            "text": "\n".join(poem_lines[2:]),
        })

    # return render_template("index.html", body=markdown("index.md"), poems=poems)
    for i in poems:
        print(i)


index()