import config
from bs4 import BeautifulSoup
import requests
import time
import random
import json
    
def get_nfts_by_collection(next_cursor=None):
        collection_slug = 'boredapeyachtclub'
        url = f"https://api.opensea.io/api/v2/collection/{collection_slug}/nfts"
        
        if next_cursor:
            url += f'?next={next_cursor}'
        
        headers = {
            "accept": "application/json",
            "x-api-key": config.opensea_api_key
        }
        
        response = requests.get(url, headers=headers)
        collection_data = response.json()
        nft_data = []
        
        for nft in collection_data['nfts']:
            identifier = nft['identifier']
            address = nft['contract']
            if int(identifier) <= 10000:
                nft_data.append({
                'identifier': identifier,
                'contract': address 
                })
                
        next_set = collection_data.get('next', None)
        return(nft_data, next_set)
        
def get_an_nft(identifier, address):
            
    chain = 'ethereum'
    url = f"https://api.opensea.io/api/v2/chain/{chain}/contract/{address}/nfts/{identifier}"
    headers = {
        "accept": "application/json",
        "x-api-key": config.opensea_api_key
    }
        
    response = requests.get(url, headers=headers)
    nft = response.json().get('nft', {})
    nft_info = {
            'collection': nft.get('collection', ''),
            'image_url': nft.get('image_url', ''),
            'metadata_url': nft.get('metadata_url', ''),
            'opensea_url': nft.get('opensea_url', ''),
            'creator': nft.get('creator', ''),
            'traits': [],
            'owners': []
        }
    for traits in nft.get('traits', []):
        nft_info['traits'].append({
            'trait_type': traits.get('trait_type', ''),
            'trait_count': traits.get('trait_count', 0),
            'value': traits.get('value', '')
    })
            
    for owner in nft.get('owners', []):
        nft_info['owners'].append({
            'owner_address': owner.get('address', ''),
            'quantity': owner.get('quantity', 0)
    })

        time.sleep(5)  # Wait for 5 seconds to prevent rate limiting
        print(nft_info)
        return(nft_info)

try:
    
    nft_data, next_set = get_nfts_by_collection()
    for nft in nft_data:
        get_an_nft(nft['identifier'], nft['contract'])

except requests.ConnectionError:
    print('Failed to connect to website')
except requests.Timeout:
    print('The request timed out')
except requests.RequestException as e:
    print(f'An error occurred while fetching the data: {e}')
except Exception as e:
    print(f'An unexpected error occurred: {e}')


