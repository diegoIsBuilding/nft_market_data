import config
from bs4 import BeautifulSoup
import requests
import random
import json

def get_nfts_by_collection():
    collection_slug = 'boredapeyachtclub'
    url = f"https://api.opensea.io/api/v2/collection/{collection_slug}/nfts"
    headers = {
        "accept": "application/json",
        "x-api-key": config.api_key
    }
    
    response = requests.get(url, headers=headers)
    collection_data = response.json()
    nft_data = []
    
    for nft in collection_data['nfts']:
        identifier = nft['identifier']
        address = nft['contract']
        if int(identifier) <= 10000:
            nft_data.append({
              'identifer': identifier,
              'contract': address 
            })
    return(nft_data)

def get_nft_addresses():
    addresses = []
    
    for address in addresses:
        
        collection_contract = ''
        nft_id = ''
        url = f'https://opensea.io/assets/ethereum/{collection_contract}/{nft_id}'
    
    
def get_an_nft(nft_data):
    #Value that need to be passed in are:
        #Identifier: the number must be less than 10000
        #Contract: passed in as 'address' in API url
        #chain: passed in as 'arbitrum' 
    chain = 'arbitrum'
    headers = {
        "accept": "application/json",
        "x-api-key": config.api_key
    }
    for nft in nft_data:
        identifier = nft['identifer']
        address = nft['contract']
        
        if int(identifier) <= 10000:
            url = f"https://api.opensea.io/api/v2/chain/{chain}/contract/{address}/nfts/{identifier}"
            response = requests.get(url, headers=headers)
            print(response.text)

    
nft_data = get_nfts_by_collection()
print(nft_data)

