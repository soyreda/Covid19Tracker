import requests
from bs4 import BeautifulSoup



url = 'https://www.worldometers.info/coronavirus/'
response = requests.get(url)
source = response.text


soup = BeautifulSoup(source, 'html.parser')

titles = []
numbers = []

#Looping through covid 19 cases over the world
for number in soup.find_all('div', id='maincounter-wrap'):
    titles.append(number.h1.text)
    numbers.append(number.div.span.text)

i = 0
for title in titles:
    print("{0} {1}".format(title, numbers[i]))
    i += 1



