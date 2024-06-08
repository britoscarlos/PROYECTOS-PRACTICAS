import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style

website = "https://es.wikipedia.org"
resultado = requests.get(website)
content = resultado.text
print(content)
