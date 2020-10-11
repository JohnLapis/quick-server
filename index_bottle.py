from bottle import route, run, template
import subprocess, jinja2


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

    with open("templates/index.html", "rb") as f:
        template = jinja2.Template(f.read())

    html = template.render(poems=poems)

    return template(html)


if __name__ == '__main__':
    run()
