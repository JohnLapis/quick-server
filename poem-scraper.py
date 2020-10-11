import requests_html


session = requests_html.HTMLSession()
response = session.get("https://poemasinfantis.blogs.sapo.pt")
poems = response.html.find("#posts .posttext")
for poem in poems[2:5]:
    lines = poem.text.split("\n")
    title = lines.pop(0)
    text = "\n".join(lines[2:]).strip()
    print(title)
    print()
    print(text)
    print("=====")
