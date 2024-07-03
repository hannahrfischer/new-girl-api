# app/resources.py

from flask import Flask, jsonify, request
import random

app = Flask(__name__)

# Import the episodes data
from .models import episodes

@app.route('/api/v1/episodes', methods=['GET'])
def get_episodes():
    season = request.args.get('season')
    episode = request.args.get('episode')
    
    if season and episode:
        season = int(season)
        episode = int(episode)
        episode_data = next((ep for ep in episodes if ep["season"] == season and ep["episode"] == episode), None)
        if episode_data:
            return jsonify(episode_data)
        else:
            return jsonify({"error": "Episode not found"}), 404
    return jsonify(episodes)

@app.route('/api/v1/episodes/<int:season>/<int:episode>', methods=['GET'])
def get_episode(season, episode):
    episode_data = next((ep for ep in episodes if ep["season"] == season and ep["episode"] == episode), None)
    if episode_data:
        return jsonify(episode_data)
    else:
        return jsonify({"error": "Episode not found"}), 404

@app.route('/api/v1/episodes/random', methods=['GET'])
def get_random_episode():
    random_episode = random.choice(episodes)
    return jsonify(random_episode)

if __name__ == '__main__':
    app.run(debug=True)
