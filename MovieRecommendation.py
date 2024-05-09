from bs4 import BeautifulSoup
import random
import requests


status = True
while (status):
    print('How old the movie would you like to see: ')
    numb = input()

    while (int(numb) < 2015):
        print('How old the movie would you like to see: ')
        numb = input() 

    movies = []
    if (int(numb) <= 2016 or int(numb) >= 2021):
        html_link = 'https://editorial.rottentomatoes.com/guide/best-wide-release-' + numb + '/'
    else:
        html_link = 'https://editorial.rottentomatoes.com/guide/best-movies-' + numb + '-wide-release/'
    html_text = requests.get(html_link).text
    soup = BeautifulSoup(html_text, 'lxml')

    list = soup.find_all('div', class_ = 'row countdown-item')

    for movie in list:
        contents = movie.find('div', class_ = 'article_movie_title')
        name = contents.find('a').text
        movies.append(name)

    print('\n')
    print(f'Movie: {random.choice(movies)}')

    status = False


