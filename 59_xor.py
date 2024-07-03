 import requests

url = 'https://projecteuler.net/resources/documents/0054_poker.txt'
lines = requests.get(url).text.splitlines()
