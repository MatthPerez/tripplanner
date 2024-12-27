from bs4 import BeautifulSoup
import requests


def kayak():
    url = "https://www.kayak.fr/news/category/idees-de-voyage/voyage-en-france/"

    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, "html.parser")

    cards = soup.find_all("div", class_="is-travel-vertical-default")

    elements = []

    if cards:
        for card in cards:
            href_value = None
            text_content = None

            href_card = card.find("a", class_="post-card-thumbnail-link")

            if href_card:
                href_value = href_card.get("href")

            text_card = card.find("div", class_="post-card__body").find(
                "div", class_="post-card__body-title"
            )

            if text_card:
                text_content = text_card.get_text(strip=True)

            if href_value or text_content:
                element = {
                    "href": href_value,
                    "text": text_content if text_content else "Pas de texte",
                }
                elements.append(element)

    # print(elements)

    return elements


from bs4 import BeautifulSoup
import requests


def wikipedia(city):
    url = f"https://fr.wikipedia.org/wiki/{city}"

    try:
        response = requests.get(url)
        response.raise_for_status()

    except requests.RequestException as e:
        return [
            "Erreur lors de la récupération des informations de Wikipédia : " + str(e)
        ]

    soup = BeautifulSoup(response.content, "html.parser")

    paragraphs = (
        soup.find("div", class_="mw-content-ltr mw-parser-output").findAll("p")
        if soup.find("div", class_="mw-parser-output")
        else []
    )

    paragraphs = [p.text for p in paragraphs if len(p.text.strip()) > 0]

    return paragraphs


def staycation(gps):
    url = f"https://www.staycation.co/fr/collections/staycation-au-vert?coords={gps}"

    try:
        response = requests.get(url)
        response.raise_for_status()

    except requests.RequestException as e:
        return [
            "Erreur lors de la récupération des informations de Staycation : " + str(e)
        ]

    soup = BeautifulSoup(response.content, "html.parser")

    plans = []

    items = soup.find_all("li", class_="CardsGrid_item__jEkAl")

    for item in items:
        link = item.find("a")
        if link:
            href = link.get("href")

            divs = link.find_all("div")
            if len(divs) >= 3:
                third_div = divs[
                    2
                ]
                text = third_div.text.strip()
                plans.append({"link": href, "text": text})

    print(plans)

    return plans
