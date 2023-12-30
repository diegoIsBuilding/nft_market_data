import config
from bs4 import BeautifulSoup
import requests
import time
import random
import json
    
def get_nfts_by_collection():
    collection_slug = 'boredapeyachtclub'
    url = f'https://api.reservoir.tools/collections/v7?slug={collection_slug}'

    headers = {
        "accept": "*/*",
        "x-api-key": config.blur_api_key
    }

    response = requests.get(url, headers=headers)

    print(response.text)