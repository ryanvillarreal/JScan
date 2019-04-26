#!/usr/bin/python3

# notes: http://scraping.pro/javascript-protected-content-scrape/
import requests,dryscrape,re
from bs4 import BeautifulSoup

# scrape through the JavaScript looking for more JS to grab.
def findJS(body):
    soup = BeautifulSoup(body, 'html.parser')
    scripts = soup.find_all('script', {"src": True})
    for line in scripts:
        urls = re.findall(r'(https?://\S+?(?=\">))', str(line))
        for url in urls:
            getSite(url)

# using a combo of BeautifulSoup and Dryscrape to make sure get all of the JS
def getSite(url):
    sess = dryscrape.Session()
    sess.set_attribute('auto_load_images', True)
    sess.visit(url)
    response = sess.body()
    f = open('test.txt', 'w')
    findJS(response)
    f.write(response)


if __name__ == "__main__":
    print ("main")
    getSite('https://google.com')
