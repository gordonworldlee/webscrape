from bs4 import BeautifulSoup
import requests
import pandas as pd


books = []
for i in range(1, 51):
    html_link = 'https://books.toscrape.com/catalogue/page-' + str(i) + '.html'

    html_text = requests.get(html_link).text
    soup = BeautifulSoup(html_text, 'lxml')
    list = soup.find('ol', class_='row')
    list = list.find_all('li')
    for book in list:
        title = book.find('img')
        title = title['alt']

        star = book.find('p')
        star = star['class']
        star = star[1]

        price = book.find('p', class_ = 'price_color').text
        price = float(price[2:])
        books.append([title, price, star])

df = pd.DataFrame(books, columns=['Title', 'Price', 'Star Rating'])
df.to_csv('books.csv')
