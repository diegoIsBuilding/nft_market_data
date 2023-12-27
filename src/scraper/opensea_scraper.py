import config
from bs4 import BeautifulSoup
import requests
import time
import random
import json


try: 
    
    def get_nfts_by_collection():
        collection_slug = 'boredapeyachtclub'
        next_set = ''
        url = f"https://api.opensea.io/api/v2/collection/{collection_slug}/nfts"
        ## url = "https://api.opensea.io/api/v2/collection/boredapeyachtclub/nfts?limit=200&next=LXBrPTIzMTQzNzAz"
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
   
        
    def get_an_nft(nft_data):
        #Value that need to be passed in are:
            #Identifier: the number must be less than 10000
            #Contract: passed in as 'address' in API url
            #chain: passed in as 'arbitrum' 
        chain = 'ethereum'
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
                time.sleep(5)
                print(response.text)
                
#Works with the try block
except requests.ConnectionError:
    print('Failed to connect to website')
except requests.Timeout:
    print('The request timed out')
except requests.RequestException as e:
    print(f'An error occurred while fetching the data: {e}')
except Exception as e:
    print(f'An unexpected error occurred: {e}')

nft_data = get_nfts_by_collection()
get_an_nft(nft_data)

