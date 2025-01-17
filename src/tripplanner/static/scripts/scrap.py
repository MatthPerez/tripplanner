from bs4 import BeautifulSoup, Tag
import requests
import re


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

    if soup.find("div", class_="infobox"):
        lines = (
            soup.find("div", class_="infobox")
            .findAll("table")[2]
            .find("tbody")
            .findAll("tr")
        )

        result = []

        for line in lines:
            th = line.find("th")
            td = line.find("td")

            if th and td:
                result.append((th.text.strip(), td.text.strip()))

        return result

    else:
        return []


def extract_number(price_str):
    match = re.search(r"\d+", price_str)

    if match:
        return int(match.group())

    return 0


def verychic():
    url = "https://www.verychic.fr/search?thematic=LOVE"

    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()

    except requests.RequestException as e:
        return ["Erreur lors de la récupération des informations de AirBnb : " + str(e)]

    soup = BeautifulSoup(response.content, "html.parser")

    plans = []

    articles = soup.find("div", class_="blocks-grid gap").findAll("article")

    for article in articles:
        text = (
            article.find(
                "a",
                class_="infos",
            )
            .find("div")
            .find("span")
            .get_text(strip=True)
        )
        link = article.find("a").get("href")
        link = f"https://www.verychic.fr{link}"

        price = (
            article.find(
                "a",
                class_="infos",
            )
            .findAll("div")[1]
            .find("div")
            .find("div")
            .findAll("div")[2]
            .get_text(strip=True)
        )

        plans.append(
            {
                "text": text,
                "link": link,
                "price": price,
            }
        )

        sorted_plans = sorted(plans, key=lambda x: extract_number(x["price"]))

    return sorted_plans


def experiments():
    url = "https://www.globe-trotting.com/post/liste-experiences-a-vivre-voyage"

    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()

    except requests.RequestException as e:
        return [
            "Erreur lors de la récupération des informations de ce site : " + str(e)
        ]

    soup = BeautifulSoup(response.content, "html.parser")

    divs = soup.find_all(
        "img",
        {"data-pin-media": True},
    )

    links = soup.find_all("a", {"data-hook": "WebLink"})

    results = []

    for i in range(min(len(divs), len(links))):
        div = divs[i]
        link = links[i]
        pin_media = div["data-pin-media"]
        href = link.get("href", "")

        results.append(
            {
                "data_pin_media": pin_media,
                "link": href,
            }
        )

    return results
