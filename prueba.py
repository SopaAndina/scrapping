import re
from colorama import Fore
import requests

website = "http://www.vulnhub.com/"
resultado = requests.get(website)
content = resultado.text

print(content)