from flask import Flask, jsonify, request
import GoogleOrganicSerp
import YouTubeOrganic
import YouTubeSerp

app = Flask(__name__)

@app.route("/api/google-organic-serp", methods=["POST"])
def google_organic_serp():
    data = request.json
    # Process data using GoogleOrganicSerp.py
    result = GoogleOrganicSerp.get_google_organic_results(data)
    return jsonify(result)

@app.route("/api/youtube-organic-serp", methods=["POST"])
def youtube_organic_serp():
    data = request.json
    # Process data using YouTubeOrganic.py
    result = YouTubeOrganic.get_youtube_organic_results(data)
    return jsonify(result)

@app.route("/api/youtube-serp", methods=["POST"])
def youtube_serp():
    data = request.json
    # Process data using YouTubeSerp.py
    result = YouTubeSerp.get_youtube_results(data)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)

from flask_cors import CORS

CORS(app)
