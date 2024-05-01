from bs4 import BeautifulSoup
import requests
import re

URL = "https://www.empireonline.com/movies/features/best-movies-2/"
LIST_OF_MOVIES = []

response = requests.get(URL)
web = response.text

soup = BeautifulSoup(web, "html.parser")
all_movies = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__BfenH")
for movies in all_movies:
    LIST_OF_MOVIES.append(movies.getText())

def extract_numbers(text):
    match = re.search(r'\d+', text)
    if match:
        return int(match.group())
    return 0


sorted_movies = sorted(LIST_OF_MOVIES, key=extract_numbers)
with open("movies.txt", "w") as file:
    for movie in sorted_movies:
        print(movie + "\n")
        file.write(movie + "\n")

# response = requests.get(URL)
# website_html = response.text
#
# soup = BeautifulSoup(website_html, "html.parser")
#
# all_movies = soup.find_all(name="h3", class_="title")
#
# movie_titles = [movie.getText() for movie in all_movies]
# movies = movie_titles[::-1]
#
# with open("movies.txt", mode="w") as file:
#     for movie in movies:
#         file.write(f"{movie}\n")