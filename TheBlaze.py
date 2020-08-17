import sys
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from csv import writer
import webbrowser 
import time
from selenium.webdriver.chrome.options import Options

# search = sys.argv[1]

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}

def getTheBlaze(search, numArticles):
            
    splitSearch = search.split()
    url = 'https://www.theblaze.com/search/?q='
    for word in splitSearch:
        url += word + '+'

    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--headless")

    driver=webdriver.Chrome(executable_path ='/Users/reetuparikh/Downloads/chromedriver', options=chrome_options)
    driver.get(url)

    time.sleep(1)

    soup = BeautifulSoup(driver.page_source, 'lxml')

    articles = soup.find_all(class_='row px10')

    for article in articles[:numArticles]:
        image = article.find(class_='widget__image crop-16x9')
        if image:
            image = image.get('data-runner-img-hd')
            print("<img src='"+ image + "' width='200' height='100'>")

        title = article.find(class_='widget__head').find_next('a').get('aria-label')
        link = article.find(class_='widget__head').find_next('a').get('href')
        print("<a href='" + link + "'>" + title + "</a>")

        print("<br><br><br>________________________________________________________________<br><br><br>")
