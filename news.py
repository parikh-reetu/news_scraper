import sys
import requests
from CNN import getCNN
from MSNBC import getMSNBC
from TheBlaze import getTheBlaze
from TheWallStreetJournal import getTheWallStreetJournal
from FOXNews import getFOXNews

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

if numSources == 0:
    print('Please select at least one news source')

if CNN == 'on':
    print('CNN results: <br>')
    getCNN(search, numArticles)

if MSNBC == 'on':
    print('MSNBC results: <br>')
    getMSNBC(search,numArticles)

if TheBlaze == 'on':
    print('The Blaze results: <br>')
    getTheBlaze(search, numArticles)

if TheWallStreetJournal == 'on':
    print('The Wall Street Journal results: <br>')
    getTheWallStreetJournal(search, numArticles)

if FOXNews == 'on':
    print('FOX News results: <br>')
    getFOXNews(search, numArticles)


