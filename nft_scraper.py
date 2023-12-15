from bs4 import BeautifulSoup
import requests

opensea_url = 'https://opensea.io'
opensea_html = requests.get(opensea_url).text
bs = BeautifulSoup(opensea_html, 'lxml')
h1 = bs.find_all('h1')

print(f' Checking... {opensea_html}')
print(f' Checking html... {bs}')
print(h1)
