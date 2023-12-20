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
        address = nft['contract']
        if int(identifier) <= 10000:
            nft_data.append(identifier)
            nft_data.append(address)
    return(nft_data)
    
    
def get_an_nft():
    #Value that need to be passed in are:
        #Identifier: the number must be less than 10000
        #Contract: passed in as 'address' in API url
        #chain: passed in as 'arbitrum' 
    url = "https://api.opensea.io/api/v2/chain/chain/contract/address/nfts/identifier"

    headers = {
        "accept": "application/json",
        "x-api-key": "7e5607e1681f45e78e55bc50eb9770b7"
    }

    response = requests.get(url, headers=headers)

    print(response.text)

    
nft_data = get_nfts_by_collection()

