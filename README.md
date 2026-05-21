# CS1060 Movie Recommender Project

A small movie recommender system built for a CS1060 final project. The app provides a simple web-based story for users to discover movie recommendations using genre, mood, and year preferences.

## What is included

- `src/app.py`: Flask web application and API.
- `src/recommender.py`: core recommendation logic.
- `src/templates/`: HTML templates for user-facing pages.
- `tests/`: unit and integration tests.
- `docs/project_plan.md`: project design, user journeys, threat model, and ethics analysis.
- `requirements.txt`: Python dependencies.

## Run the app

1. Install dependencies:
   ```bash
   python3 -m pip install -r requirements.txt
   ```
2. Start the app:
   ```bash
   python3 src/app.py

   cd /workspaces/cs1060-project
   python3 -m src.app

   ```
3. Visit `http://127.0.0.1:5000` in your browser.

## Run tests

```bash
python3 -m pytest
```

## Notes

The app is intentionally lightweight for a final project demo. It includes user journeys, an API endpoint, a testable backend, and documentation for instructors.
