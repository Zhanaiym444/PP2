import math
import itertools
import random


# выше 5.5
def is_above_55(movie):
    return movie["imdb"] > 5.5

# Вернуть imdb > 5.5
def high_rated_movies(movies):
    return [m for m in movies if m["imdb"] > 5.5]

#  фильмов по категории
def movies_by_category(movies, category):
    return [m for m in movies if m["category"] == category]

# Средний рейтинг списка фильмов
def average_imdb(movies):
    if not movies:
        return 0
    return sum(m["imdb"] for m in movies) / len(movies)

# Средний рейтинг по категории
def average_category_imdb(movies, category):
    category_movies = movies_by_category(movies, category)
    return average_imdb(category_movies)
