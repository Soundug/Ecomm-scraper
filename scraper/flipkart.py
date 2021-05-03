import requests
from bs4 import BeautifulSoup
import lxml
import time
import webbrowser as wb
import pandas as pd

URL = "https://www.flipkart.com/search?q=Laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"

response = requests.get(URL)
soup = BeautifulSoup(response.content, 'lxml')

# store data in lists
nm = soup.find_all('div', {'class': '_4rR01T'})
# print(name)

pr = soup.find_all('div', {'class': '_30jeq3 _1_WHN1'})
# print(price)

rt = soup.find_all('div', {'class': '_3LWZlK'})
# print(rating)

specs = soup.find_all('ul', {'class': '_1xgFaf'})
# print(specs)

# lists for storing data
Name = []
Price = []
Rating = []
Specs = []

for i in nm:
    Name.append(i.text)

for i in pr:
    Price.append(i.text)

for i in rt:
    Rating.append(i.text)

for i in specs:
    Specs.append(i.text)

# initialize data of lists
data = (Name, Price, Rating, Specs)
# create dataframe
df = pd.DataFrame(data, columns=['Name', 'Price', 'Rating', 'Specs'])
print(df)

df.to_csv('file1.csv')