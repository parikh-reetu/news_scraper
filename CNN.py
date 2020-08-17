import sys
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from csv import writer
import webbrowser 
import time
from selenium.webdriver.chrome.options import Options

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}

def getCNN(search, numArticles):
    splitSearch = search.split()
    url = "https://www.cnn.com/search?size=10&q="
    for word in splitSearch:
        url += word + '%20'

    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--headless")

    driver=webdriver.Chrome(executable_path ='/Users/reetuparikh/Downloads/chromedriver', options=chrome_options)
    driver.get(url)

    time.sleep(1)

    soup = BeautifulSoup(driver.page_source, 'lxml')

    articles = soup.find_all(class_='cnn-search__result cnn-search__result--article')

    for article in articles[:numArticles]:
        image = article.find(class_='cnn-search__result-thumbnail')
        if image:
            image = image.find('img').get('src')
            print("<img src='https:" + image + "'>")

        title = article.find(class_='cnn-search__result-headline')
        print(title)

        print("<br><br><br><hr><br><br><br>")
