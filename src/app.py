from flask import Flask, render_template, request, jsonify
from src.recommender import recommend

app = Flask(__name__, template_folder="templates")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/recommend", methods=["POST"])
def recommend_route():
    genre = request.form.get("genre", "")
    mood = request.form.get("mood", "")
    year_min = request.form.get("year_min", "")
    year_max = request.form.get("year_max", "")

    def parse_year(value):
        try:
            return int(value)
        except (ValueError, TypeError):
            return None

    recommendations = recommend(
        genre=genre,
        mood=mood,
        year_min=parse_year(year_min),
        year_max=parse_year(year_max),
        limit=5,
    )

    return render_template(
        "results.html",
        recommendations=recommendations,
        genre=genre,
        mood=mood,
        year_min=year_min,
        year_max=year_max,
    )


@app.route("/api/recommend", methods=["GET"])
def api_recommend():
    genre = request.args.get("genre", "")
    mood = request.args.get("mood", "")
    year_min = request.args.get("year_min")
    year_max = request.args.get("year_max")

    def parse_year(value):
        try:
            return int(value)
        except (ValueError, TypeError):
            return None

    recommendations = recommend(
        genre=genre,
        mood=mood,
        year_min=parse_year(year_min),
        year_max=parse_year(year_max),
        limit=5,
    )
    return jsonify(recommendations)


if __name__ == "__main__":
    app.run(debug=True)
