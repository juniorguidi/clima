import requests, time, os
from bs4 import BeautifulSoup

def clima_google(pesquisa):
    url = f"https://www.google.com/search?&q={pesquisa}"
    r = requests.get(url)
    s = BeautifulSoup(r.text, "html.parser")
    clima = s.find("div", class_="BNeawe").text

    return(clima)

def main(localizacao):
    os.system('cls')
    pesquisa = clima_google(f"clima em {localizacao}")
    print(pesquisa)
    time.sleep(5)


if __name__ == "__main__":
    try:
        localizacao = input("Qual sua localização? ")
        while True:
            main(localizacao)
    except (KeyboardInterrupt):
        print ("Encerrando...")