import config
import requests

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
        contract = nft['contract']
        token_standard = nft['token_standard']
        image_url = nft['image_url']
        metadata_url = nft['metadata_url']
        opensea_url = nft['opensea_url']
        
        if int(identifier) <= 10000:
            nft_data.append({
              'identifer': identifier,
              'contract': contract,
              'token_standard': token_standard,
              'image_url': image_url,
              'metadata_url': metadata_url,
              'opensea_url': opensea_url
            })
    return(nft_data)
    
    
print(get_nfts_by_collection())

