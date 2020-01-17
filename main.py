import requests
from bs4 import BeautifulSoup
from googlesearch import search

# this scraper will only return data from quizlet.com!

def main():
  query = input('Paste your text here and press [enter]: ').lower()

  while query != '':
    google_search = search(query, tld='co.in', num=1, stop=1, pause=1)
    url = ''
    answer = ''

    for result in google_search: 
      split_url = result.split('/')[:4]
      url = '/'.join(split_url) + '/' + 'print'

    req = requests.get(url)

    soup = BeautifulSoup(req.content, features='html.parser')

    left_spans = soup.findAll('span', {'class': 'left copy'})

    for each in left_spans:
      raw_text = each.text.lower().strip()
      quoted_text = '"' + raw_text + '"'
      if query in raw_text or query in quoted_text:
        print(each.parent.text)
        answer = each.parent.text
    
    if answer == '':
      right_spans = soup.findAll('span', {'class': 'right copy'})
      for each in right_spans:
        raw_text = each.text.lower().strip()
        quoted_text = '"' + raw_text + '"'
        if query in raw_text or query in quoted_text:
          print(each.parent.text)
          answer = each.parent.text
    
    if answer == '':
      idklol()
  
    query = input('Paste your text here and press [enter]: ').lower()

def idklol():
  print("¯\\_(ツ)_/¯")

main()
