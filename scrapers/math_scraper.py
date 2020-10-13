import requests_html, sys


def main(number=None):
    session = requests_html.HTMLSession()
    if number is None:
        response = session.get(f"http://numbersapi.com/random?json")
    else:
        response = session.get(f"http://numbersapi.com/{number}?json")
    json = response.json()
    return {"number": json["number"], "text": json["text"]}


if __name__ == '__main__':
    if len(sys.argv) > 1:
        number = int(sys.argv[1])
        print(main(number))
    else:
        print(main())
