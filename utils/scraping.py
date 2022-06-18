from bs4 import BeautifulSoup as bs
import requests
from schemas.foods import Recipes


def scraping_data(recipe_name):
    base_url = "https://cookpad.com"

    res = requests.get(f"{base_url}/search/{recipe_name}")

    recipes = []
    soup = bs(res.text, "html.parser")
    for i in range(5):
        for recipe in soup.select(f"#recipe_{i}"):
            title = recipe.div.img.get('alt')
            thumbnail = recipe.div.img.get('src')
            url = recipe.h2.a.get('href')
        recipes.append(
            Recipes(
                title=title,
                recipe_thumbnail=thumbnail,
                recipe_url=f"{base_url}{url}"
            )
        )
    return recipes
