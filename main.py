import DontShare as cb
import ccxt
import requests
import re

signals = []
url = 'http://localhost:8000/getmessage/'

def get_messages(url):
    response = requests.get(url)
    return response.text
 
while True:
    print(type(get_messages(url)))
    print(get_messages(url))



