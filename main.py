import re
import requests
from bs4 import BeautifulSoup
from googlesearch import search

# this scraper will only return data from quizlet.com!

def main():
  query = input('Paste your text here and press [enter]: ').lower()

  while query != '':
    query = '"' + query + '"'
    google_search = search(query, tld='co.in', num=1, stop=1, pause=0)
    url = ''
    response = ''

    for result in google_search: 
      split_url = result.split('/')[:4]
      url = '/'.join(split_url) + '/' + 'print'

    req = requests.get(url)
    soup = BeautifulSoup(req.content, features='html.parser')
    query = query.replace('"', '')
    response = find_by_column('left copy', query, soup)
    
    if answer_not_found(response):
      response = find_by_column('right copy', query, soup)
      if answer_not_found(response):
        idklol()
  
    query = input('Paste your text here and press [enter]: ').lower()

def find_by_column(column, query, soup):
  tags = soup.findAll('span', {'class': column})
  for each in tags:
    raw_text = each.text.lower().strip()
    quoted_text = '"' + raw_text + '"'
    if query in raw_text or query in quoted_text:
      print(each.parent.text)
      return each.parent.text
  
def answer_not_found(string):
  return string == '' or string == [] or string == None

def idklol():
  print("¯\\_(ツ)_/¯")

main()
