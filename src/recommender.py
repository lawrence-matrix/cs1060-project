from typing import List, Dict, Optional

Movie = Dict[str, object]

MOVIES: List[Movie] = [
    {
        "title": "The Grand Budapest Hotel",
        "genres": ["Comedy", "Drama"],
        "year": 2014,
        "rating": 8.1,
        "moods": ["Lighthearted", "Stylish"],
    },
    {
        "title": "Inception",
        "genres": ["Action", "Sci-Fi", "Thriller"],
        "year": 2010,
        "rating": 8.8,
        "moods": ["Intense", "Mind-bending"],
    },
    {
        "title": "Hidden Figures",
        "genres": ["Biography", "Drama"],
        "year": 2016,
        "rating": 7.8,
        "moods": ["Inspiring", "Warm"],
    },
    {
        "title": "La La Land",
        "genres": ["Drama", "Romance", "Musical"],
        "year": 2016,
        "rating": 8.0,
        "moods": ["Romantic", "Musical"],
    },
    {
        "title": "The Matrix",
        "genres": ["Action", "Sci-Fi"],
        "year": 1999,
        "rating": 8.7,
        "moods": ["Thrilling", "Philosophical"],
    },
]


def load_movies() -> List[Movie]:
    return MOVIES.copy()


def filter_by_genre(movies: List[Movie], genre: str) -> List[Movie]:
    if not genre:
        return movies
    genre_lower = genre.strip().lower()
    return [movie for movie in movies if any(g.lower() == genre_lower for g in movie["genres"])]


def filter_by_year(movies: List[Movie], year_min: Optional[int], year_max: Optional[int]) -> List[Movie]:
    filtered = movies
    if year_min is not None:
        filtered = [movie for movie in filtered if movie["year"] >= year_min]
    if year_max is not None:
        filtered = [movie for movie in filtered if movie["year"] <= year_max]
    return filtered


def filter_by_mood(movies: List[Movie], mood: str) -> List[Movie]:
    if not mood:
        return movies
    mood_lower = mood.strip().lower()
    return [movie for movie in movies if any(m.lower() == mood_lower for m in movie["moods"])]


def sort_recommendations(movies: List[Movie]) -> List[Movie]:
    return sorted(movies, key=lambda movie: (-movie["rating"], -movie["year"]))


def recommend(
    genre: str = "",
    mood: str = "",
    year_min: Optional[int] = None,
    year_max: Optional[int] = None,
    limit: int = 5,
) -> List[Movie]:
    movies = load_movies()
    movies = filter_by_genre(movies, genre)
    movies = filter_by_mood(movies, mood)
    movies = filter_by_year(movies, year_min, year_max)
    movies = sort_recommendations(movies)
    return movies[:limit]
