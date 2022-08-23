import requests
from bs4 import BeautifulSoup
from pprint import pprint

res = requests.get('https://news.ycombinator.com/')
soup = BeautifulSoup(res.text,'html.parser')
links = soup.select('.titlelink')
subtext = soup.select('.subtext')

def sort_stories(hnlist):
    return sorted(hnlist, key=lambda x:x['votes'],reverse=True)

def create_custom_hn(links,subtext):
    hn = []
    for idx,item in enumerate(links):
        title = item.getText()
        href = item.get('href',None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99 :
                hn.append({'title': title, 'href': href,'votes': points})
    return sort_stories(hn)

pprint(create_custom_hn(links,subtext))

