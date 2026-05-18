import json
from flask import Flask
from src.app import app


def test_home_page_loads():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Movie Recommender" in response.data


def test_recommend_form_returns_results():
    client = app.test_client()
    response = client.post(
        "/recommend",
        data={"genre": "Drama", "mood": "Inspiring", "year_min": "2010", "year_max": "2020"},
    )
    assert response.status_code == 200
    assert b"Top matches" in response.data


def test_api_recommend_endpoint_returns_json():
    client = app.test_client()
    response = client.get("/api/recommend?genre=Action&mood=Intense")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert isinstance(data, list)
    assert data[0]["title"] == "Inception"
