import requests
from parser import parse

if __name__ == '__main__':
    url = "https://en.wikipedia.org/wiki/History_of_Mexico"
    response = requests.get(url)
    results = parse(response.text)
    print(results)

