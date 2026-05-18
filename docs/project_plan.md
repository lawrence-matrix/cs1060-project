# Movie Recommender System Design

## Problem Statement

Many viewers struggle to choose a movie that matches their mood, preferred genre, or release era. This project creates a lightweight recommender web app that helps casual movie watchers discover movies based on simple preferences.

## Target Personas

- **Casual viewer**: wants fast movie suggestions for a weekend stream, with low technical expectations.
- **Indecisive planner**: wants a recommendation based on mood or genre and is okay with a short list.
- **API integrator**: a basic developer who wants to call a recommendation endpoint from another service.

## Core Features

- Browse recommendations by genre and mood.
- Filter by earliest and latest release year.
- Search through a small curated movie catalog.
- Use both a browser UI and a simple API endpoint.
- Provide test coverage for recommendation logic and the web interface.

## Technology Stack

- Python 3
- Flask for web server and API
- Jinja templates for HTML views
- Pytest for unit and integration tests

## User Journey 1: Casual viewer selects a mood-based recommendation

1. The user opens the home page.
2. They choose a mood, such as `Intense`.
3. They optionally set a year range and click `Recommend`.
4. The app shows a short ranked list of movies matching the mood.
5. If no results match, the app displays a friendly message and suggests trying a broader mood or genre.

## User Journey 2: API client requests a genre-based suggestion

1. A client sends a GET request to `/api/recommend?genre=Drama&year_min=2010`.
2. The backend validates the year values and applies filters.
3. The endpoint returns JSON with up to 5 matching movie records.
4. The client displays or logs the returned titles.

## End User Documentation Plan

The user guide will explain:
- How to open the app in a browser.
- How to select genre, mood, and year range.
- How to interpret the recommendation result list.
- How to use the `/api/recommend` endpoint.

## Test Plan

- Unit tests for
  - `load_movies`
  - `filter_by_genre`
  - `filter_by_mood`
  - `filter_by_year`
  - `sort_recommendations`
- Integration tests for
  - submitting the recommendation form
  - calling `/api/recommend`

## Threat Model

### Stakeholders
- Viewer: wants relevant movie suggestions.
- Web user: wants easy navigation and clear error messages.
- Reviewer/grader: wants reliable, working journeys.

### Anti-stakeholders
- Malicious user: may send malformed query values.
- Competitor: may try to overload or confuse the service.

### Identified threats
1. Invalid year values cause failure.
2. Empty recommendation results confuse users.
3. API returns too much information from internal logic.

### Mitigation
- Parse and ignore invalid year inputs safely.
- Show friendly fallback instructions when no matches are found.
- Keep the API response limited to title, genres, year, rating, and mood.

## Ethics Analysis

### Value conflict example
- The system could favor popular or higher-rated movies to maximize engagement, but that may reduce exposure for smaller films and limit fairness.
- We choose a simple, transparent ranking by rating and year rather than hidden engagement metrics.

### Adversary misuse
- A bad actor could call the API repeatedly with many malformed parameters.
- Mitigation: validate inputs and keep the service lightweight.

### Additional concerns
- Users may rely on recommendations for mood-sensitive viewing. The app avoids content spoilers by only returning title-level metadata.
