import requests
from bs4 import BeautifulSoup

headers = requests.utils.default_headers()
headers.update({ 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})


url = "https://www.example.it"
req = requests.get(url, headers)
soup = BeautifulSoup(req.content, 'html.parser')

aTags = soup.find_all('a')

emails = []

for tag in atags:
  tagToString = str(tag)
  if tagToString.find('path') != -1:
    agencyReq = requests.get(tag.get('href'), headers)
    agencySoup = BeautifulSoup(agencyReq.content, 'html.parser')
    details = agencySoup.find_all('li')
    for detail in details:
      if str(detail.getText()).find('@') != -1:
        emails.append(str(detail.getText()).strip())

print(emails)