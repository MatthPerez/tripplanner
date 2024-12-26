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

# def airbnb(city, start_date, end_date):
#     url = f"https://www.airbnb.fr/s/{city}/homes?refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&monthly_start_date={start_date|format("y-m-d")}&monthly_length=3&monthly_end_date={end_date|format("y-m-d")}&price_filter_input_type=0&channel=EXPLORE&date_picker_type=calendar&checkin={start_date|format("y-m-d")}&checkout={end_date|format("y-m-d")}&source=structured_search_input_header&search_type=filter_change"
    
#     try:
#         response = requests.get(url)
#         response.raise_for_status()
#     except requests.RequestException as e:
#         return [
#             "Erreur lors de la récupération des informations de Wikipédia : " + str(e)
#         ]

#     soup = BeautifulSoup(response.content, "html.parser")
    
#     houses = soup.findAll("div", class_="g1qv1ctd").find_all("div").get_text(strip=True)
    
#     return houses
    
    