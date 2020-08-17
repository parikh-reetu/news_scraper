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

def getMSNBC(search, numArticles):

    splitSearch = search.split()
    url1 = 'https://www.msnbc.com/search/?q='
    url2 = '#gsc.tab=0&gsc.q='
    url3 = '&gsc.page=1'
    plusAddIn = ''
    percentAddIn = ''
    for word in splitSearch:
        plusAddIn += word + '+'
        percentAddIn += word + '%20'
    url = url1 + plusAddIn + url2 + percentAddIn + url3

    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--headless")

    driver=webdriver.Chrome(executable_path ='/Users/reetuparikh/Downloads/chromedriver', options=chrome_options)
    driver.get(url)

    time.sleep(1)

    soup = BeautifulSoup(driver.page_source, 'lxml')

    articles = soup.find_all(class_='gsc-webResult gsc-result')

    for article in articles[:numArticles]:
        image = article.find(class_='gsc-table-result')
        if image:
            image = image.find('img').get('src')
            print("<img src='"+ image + "' width='200' height='100'>")

        title = article.find(class_='gs-title').get_text()
        link = article.find(class_='gs-title').find('a').get('href')
        print("<a href='" + link + "'>" + title + "</a>")

        print("<br><br><br><hr><br><br><br>")
