import sys
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from csv import writer
import webbrowser 
import time
from selenium.webdriver.chrome.options import Options
import json

# search = sys.argv[1]

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}

def getTheWallStreetJournal(search, numArticles):
    splitSearch = search.split()
    url1 = 'https://www.wsj.com/search/term.html?KEYWORDS='
    url2 = '&mod=searchresults_viewallresults'
    for word in splitSearch:
        url1 += word + '%20'
    url = url1 +url2

    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--headless")

    driver=webdriver.Chrome(executable_path ='/Users/reetuparikh/Downloads/chromedriver', options=chrome_options)
    driver.get(url)

    time.sleep(1)

    soup = BeautifulSoup(driver.page_source, 'lxml')

    articles = soup.find_all(class_='item-container headline-item')

    article_dict = {"source":"The Wall Street Journal"}
    count = 1

    for article in articles[:numArticles]:
        each_article = {}
        image = article.find(class_='headline-image')
        if image:
            image = image.find_next('img').get('data-src')
            #format picture size
            each_article['image'] = image
            print("<img src='" + image + "' width='200' height='100'>")

        title = article.find(class_='headline').find_next('a').get_text()
        each_article['title'] = title
        link1 = 'https://www.wsj.com' 
        link2 = article.find(class_='headline').find_next('a').get('href')
        link = link1+ link2
        each_article['link'] = link
        print("<a href='" + link + "'>" + title + "</a>")
        article_dict[count] = each_article
        count += 1
        print("<br><br><br><hr><br><br><br>")

    with open('public/articles.json') as json_file: 
        data = json.load(json_file) 
        data.append(article_dict)
    write_json(data)


def write_json(data, filename='public/articles.json'): 
    with open(filename,'w') as json_file: 
        json.dump(data, json_file, indent=4)

search = sys.argv[1]
numArticles = sys.argv[2]
start_time = time.time()
getTheWallStreetJournal(search, numArticles)
print("--- %s seconds ---" % (time.time() - start_time))
