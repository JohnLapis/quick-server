from bottle import route, run, template
import subprocess


@route("/")
def index():
    poems = []
    all_poems = subprocess.run(
        ["node", "poem-scraper.js"], stdout=subprocess.PIPE
    ).stdout.decode()
    for poem in all_poems.split("<ENDPOEM>"):
        poem_lines = poem.strip().split("\n")
        poems.append(
            {
                "title": poem_lines[0],
                "text": poem_lines[2:],
            }
        )

    return template("templates/base.html", poems=poems)


if __name__ == '__main__':
    run(host="0.0.0.0")
