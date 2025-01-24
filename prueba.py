import re
from colorama import Fore
import requests

website = "http://www.vulnhub.com/"
resultado = requests.get(website)
content = resultado.text

patron = r"/entry/[\w-]*"
maquinas_repetidas = re.findall(patron, str(content))

sin_duplicados = list(dict.fromkeys(maquinas_repetidas)) #sin_duplicados = list(set(maquinas_repetidas))

print(sin_duplicados)

maquinas_final=[]

for i in sin_duplicados:
    nombre_maquinas = i.replace("/entry/", "")
    maquinas_final.append(nombre_maquinas)
    print(nombre_maquinas)


maquinas_noob = "noob-1"
existe_noob = False

for a in maquinas_final:
    if a == maquinas_noob:
        existe_noob = True
        break

if existe_noob:
    print("\n" + Fore.GREEN + "No hay ninguna maquina nueva")
else:
    print("\n" + Fore.RED + "Hay una nueva maquina")
