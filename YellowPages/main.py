import csv
import re
from time import sleep

import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    with open('RadiologenGelbeSeitenNew.csv', 'w', newline='') as outcsv:
        writer = csv.writer(outcsv)
        writer.writerow(["Name", "Adresse", "Telefon", "E-Mail"])
        for page in range(0, 33):
            main_url = 'https://www.gelbeseiten.de/Suche/Radiologen/Bundesweit/Seite-{x}'.format(
                x=page)  # müssen wieder 33 seiten sein
            req = requests.get(main_url)
            soup = BeautifulSoup(req.text, "html.parser")
            articles = soup.find_all('article')
            for article in articles:
                Name = "Keine Angabe"
                Adresse = "Keine Angabe"
                Telefon = "Keine Angabe"
                EMail = "Keine Angabe"
                h2 = article.findChildren("h2", recursive=True)[0]
                if h2:
                    title = h2.getText()
                    Name = title

                addressElement = article.findChildren("address", recursive=True)[0]
                if addressElement:
                    address = addressElement.find('p', {"data-wipe-name": "Adresse"})
                    if address:
                        Adresse = re.sub(' +', ' ', address.getText().replace("\n", "").replace("\t", " "))[1:]
                    phone = addressElement.find('p', {"data-wipe-name": "Kontaktdaten"})
                    if phone:
                        Telefon = phone.getText()

                detailButton = article.find('a', {"class": "contains-icon-details gs-btn"}, href=True)
                if detailButton or detailButton is None:
                    # neu, da nicht alle details richtig aufgelöst werden können
                    if detailButton is None:
                        href = "https://www.gelbeseiten.de/gsbiz/" + article.find('div', {"target": "_self"})[
                            "data-realid"]
                    else:
                        href = detailButton['href']

                    req2 = requests.get(href)
                    soup = BeautifulSoup(req2.text, "html.parser")
                    contactElements = soup.find('section', {"id": "kontaktdaten"})
                    if contactElements:
                        listItems = contactElements.find_all('li')
                        for item in listItems:
                            item_children = item.findChildren('span', recursive=True)
                            if item_children:
                                item_text = item_children[0].getText()
                                if "@" in item_text:
                                    EMail = item_text
                writer.writerow([Name, Adresse, Telefon, EMail])
            print("sleeping")
            sleep(10)
            print("woke up")
            print("Page {} of 32".format(page))
