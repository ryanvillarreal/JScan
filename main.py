#!/usr/bin/python3

# notes: http://scraping.pro/javascript-protected-content-scrape/
import requests,dryscrape,re, os.path
from urlparse import urlparse
from bs4 import BeautifulSoup


# Make the folder for the site based on user input
def domain_name(site):
    parsed_uri = urlparse(site)
    parsed_domain = '{uri.netloc}'.format(uri=parsed_uri)
    return parsed_domain

# scrape through the JavaScript looking for more JS to grab.
def findJS(body):
    soup = BeautifulSoup(body, 'html.parser')
    scripts = soup.find_all('script', {"src": True})
    for line in scripts:
	print line
        urls = re.findall(r'(https?://\S+?(?=\">))', str(line))
        for url in urls:
            getSite(url)

# using a combo of BeautifulSoup and Dryscrape to make sure get all of the JS
def getSite(url):
    sess = dryscrape.Session()
    sess.set_attribute('auto_load_images', True)
    sess.visit(url)
    response = sess.body()

    # parsing uri for filename
    parsed_uri = urlparse(url)
    filename = os.path.basename(parsed_uri.path)
    fullpath = os.path.join(dir, filename)

    # python won't let me write the file names into the domain directory.
    print fullpath
    f = open(fullpath, 'w')
    findJS(response)
    f.write(response)


if __name__ == "__main__":
    site = raw_input("Site to crawl? ")
    dir = './' + domain_name(site) + '/'

    # Setup Folder Structure
    if not os.path.exists(dir):
        os.makedirs(dir)

    # Process Data
    getSite(site)
