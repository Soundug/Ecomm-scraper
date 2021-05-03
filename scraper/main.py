from bs4 import BeautifulSoup
import requests
import csv
import io

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/58.0.3029.110 Safari/537.3'}

url = input('Enter the url you want to scrape data from: ')

response = requests.get(url, headers=headers).text

soup = BeautifulSoup(response, 'lxml')

Names = []
Prices = []
Ratings = []
Reviews = []

for i in soup.find_all('a', class_='a-link-normal a-text-normal'):
    string = i.text
    Names.append(string.strip())

for i in soup.find_all('span', class_='a-price-whole'):
    Prices.append(i.text)

for i in soup.find_all('span', class_='a-icon-alt'):
    Ratings.append(i.text)

for i in soup.find_all('span', attrs={'id': 'acrCustomerReviewText'}):
    string = i.text
    Reviews.append(string.strip())

'''
def get_rating(soup):
    try:
        Ratings = soup.find('i', attrs={'class':'a-icon a-icon-star a-star-4-5'}).string.strip()
    except:
        try:
            Ratings = soup.find('span', attrs={'class':'a-icon-alt'}).string.strip()
        except AttributeError:
            Ratings = ''
    return Ratings
'''

'''
def get_review_count(soup):
    try:
        Reviews = soup.find('span', attrs={'id':'acrCustomerReviewText'}).string.strip()
    except AttributeError:
        Reviews = ''

    return Reviews
    Reviews.append(text)
'''

filename = 'Laptops.csv'

with open(filename, 'w', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Sr No', 'Names', 'Prices', 'Ratings'])

    for i in range(len(Names)):
        writer.writerow([Names[i], Prices[i], Ratings[i]])
