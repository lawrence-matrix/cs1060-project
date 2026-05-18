import pytest
from src.recommender import filter_by_genre, filter_by_mood, filter_by_year, sort_recommendations, recommend, load_movies


def test_load_movies_returns_list():
    movies = load_movies()
    assert isinstance(movies, list)
    assert movies


def test_filter_by_genre_matches():
    movies = load_movies()
    result = filter_by_genre(movies, "Drama")
    assert all("Drama" in movie["genres"] for movie in result)
    assert result


def test_filter_by_mood_matches():
    movies = load_movies()
    result = filter_by_mood(movies, "Intense")
    assert len(result) == 1
    assert result[0]["title"] == "Inception"


def test_filter_by_year_range():
    movies = load_movies()
    result = filter_by_year(movies, 2015, 2016)
    assert all(2015 <= movie["year"] <= 2016 for movie in result)
    assert any(movie["title"] == "La La Land" for movie in result)


def test_sort_recommendations_orders_by_rating_and_year():
    movies = [
        {"title": "A", "rating": 7.0, "year": 2022},
        {"title": "B", "rating": 8.5, "year": 2015},
        {"title": "C", "rating": 8.5, "year": 2020},
    ]
    sorted_movies = sort_recommendations(movies)
    assert [movie["title"] for movie in sorted_movies] == ["C", "B", "A"]


def test_recommend_returns_up_to_limit():
    result = recommend(limit=2)
    assert len(result) == 2


def test_recommend_combines_filters():
    result = recommend(genre="Sci-Fi", mood="Thrilling")
    assert len(result) == 1
    assert result[0]["title"] == "The Matrix"
