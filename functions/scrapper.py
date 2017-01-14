from time import sleep

import requests
from bs4 import BeautifulSoup


class Scrape(object):
    def __init__(self, search, sub):
        self.search = search
        self.sub = sub

    def scrape(self):
        try:
            sleep(5)
            print('Please wait while we process your code')
            url = 'https://www.google.co.in/search?q=' + self.search + '%20wikipedia%20' + self.sub + '&rct=j'
            html = requests.get(url).text
            soup = BeautifulSoup(html, 'html.parser')
            soup = soup.find('cite')
            url2 = soup.text
            print('finalizing output...')
            sleep(5)
            html2 = requests.get(url2).text
            soup2 = BeautifulSoup(html2, 'html.parser')
            soup2 = soup2.find('p')
            return soup2.text
        except Exception as exception:
            print(exception)