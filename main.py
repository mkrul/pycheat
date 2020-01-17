import requests
from bs4 import BeautifulSoup
from googlesearch import search

# enter some text
# search for that text in google, with quotes
# go to that link
# text gets downcased
# loop over each div on page, downcase the contents, compare to text that was passed in
# # once there is a match return the div contents of the parent div

def main():
  try:
    query = input('Paste your text here and press [enter]:').lower()
    google_search = search(query, tld='co.in', num=1, stop=1, pause=1)
    url = ''

    for result in google_search: 
      split_url = result.split('/')[:4]
      url = '/'.join(split_url) + '/' + 'print'

      print(url)

    req = requests.get(url)

    soup = BeautifulSoup(req.content, features='html.parser')

    spans = soup.findAll('span', {'class': 'left copy'})

    for each in spans:
      text = '"' + each.text.lower().strip() + '"'
      if query in text:
        print(each.parent.text)

  except:
    idklol()

def idklol():
  print("¯\\_(ツ)_/¯")

main()
