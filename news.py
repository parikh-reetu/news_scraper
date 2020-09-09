import sys
# sys.path.insert(1, '/Users/reetuparikh/Desktop/nodeLogin/sources')

# sys.path.append('/Desktop/nodeLogin/sources')
import requests

from cnn import getCNN
from msnbc import getMSNBC
from the_blaze import getTheBlaze
from wsj import getTheWallStreetJournal
from fox_news import getFOXNews
import json
import os                                                                       

search = sys.argv[1]

if len(search) == 0:
    print('Please enter your search')

CNN = sys.argv[2]
MSNBC = sys.argv[3]
TheBlaze = sys.argv[4]
TheWallStreetJournal = sys.argv[5]
FOXNews = sys.argv[6]

list = [CNN, MSNBC, TheBlaze, TheWallStreetJournal, FOXNews]
numSources = list.count('on')
numArticles = 15 // numSources
numArticles = 3

json_list = []

if numSources == 0:
    print('Please select at least one news source')


if CNN == 'on':
    print('CNN results: <br>')
    json_list.append(getCNN(search, numArticles))

if MSNBC == 'on':
    print('MSNBC results: <br>')
    json_list.append(getMSNBC(search, numArticles))

if TheBlaze == 'on':
    print('The Blaze results: <br>')
    json_list.append(getTheBlaze(search, numArticles))

if TheWallStreetJournal == 'on':
    print('The Wall Street Journal results: <br>')
    json_list.append(getTheWallStreetJournal(search, numArticles))

if FOXNews == 'on':
    print('FOX News results: <br>')
    json_list.append(getFOXNews(search, numArticles))

# t1 = Thread(target=runCNN)
# t1.start()
# t2 = Thread(target=runMSNBC)
# t2.start()
# t3 = Thread(target=runTheBlaze)
# t3.start()
# t4 = Thread(target=runTheWallStreetJournal)
# t4.start()
# t5 = Thread(target=runFOXNewws)
# t5.start()
# time.sleep(30)

with open('public/articles.json', 'w') as json_file:
    json.dump(json_list, json_file)


# threading.Thread(target=runCNN, args=(1,)).start()
# threading.Thread(target=runMSNBC, args=(1,)).start()
# threading.Thread(target=runTheBlaze, args=(1,)).start()
# threading.Thread(target=runTheWallStreetJournal, args=(1,)).start()
# threading.Thread(target=runFOXNewws, args=(1,)).start()
# time.sleep(15)

# p1 = Process(target=runCNN, args=10)              
# p2 = Process(target=runMSNBC(), args=(10))
# p3 = Process(target=runTheBlaze(), args=(10))
# p4 = Process(target=runTheWallStreetJournal(), args=(10))
# p5 = Process(target=runFOXNewws(), args=(10))
# p1.start() 
# p1.join
# p2.start()
# p2.join
# p3.start()
# p3.join
# p4.start()
# p4.join
# p5.start()
# p5.join


