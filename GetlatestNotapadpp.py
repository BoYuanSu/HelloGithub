import os
print(os.popen("python --version").read())
from bs4 import BeautifulSoup
import requests
import urllib.request
urlNPpp = "https://notepad-plus-plus.org/download/"
res = requests.get(urlNPpp)
while res.status_code != 200:
    res = requests.get(uNPpp)

s1 = BeautifulSoup(res.text.encode("utf-8"), "html.parser")
href = s1.select("html.subpage a")
for h in href:
    if "Installer.exe" in h["href"]:
        urlexe = "https://notepad-plus-plus.org/" + (h["href"])

filename = "D:\\Desktop\\" + urlexe.split("/")[len(urlexe.split("/"))-1]
print(filename)
urllib.request.urlretrieve(urlexe, filename)
