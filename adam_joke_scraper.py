import requests
from bs4 import BeautifulSoup
from pprint import pprint
import time
import random

joke_url = 'http://www.laughfactory.com/jokes/popular-jokes/all-time/{randomno}'

def scrape():
    randomno = random.randint(1,276)
    resp = requests.get(joke_url.format(randomno=randomno), timeout=5)
    page_content = BeautifulSoup(resp.content, 'html.parser')
    all_jokes = page_content.findAll('p', id=lambda x: x and x.startswith('joke_'))
    random_joke = random.choice(all_jokes).text
    print(random_joke)
    return random_joke


if __name__ == '__main__':
    scrape()
