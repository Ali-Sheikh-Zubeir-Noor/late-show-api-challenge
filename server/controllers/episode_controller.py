from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from server.models import db, Episode

episode_bp = Blueprint("episodes", __name__)

@episode_bp.route("/episodes", methods=["GET"])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([e.to_dict() for e in episodes]), 200


@episode_bp.route("/episodes/<int:id>", methods=["GET"])
def get_episode(id):
    episode = Episode.query.get(id)
    if not episode:
        return {"error": "Episode not found"}, 404

    data = episode.to_dict()
    data["appearances"] = [a.to_dict() for a in episode.appearances]
    return jsonify(data), 200


@episode_bp.route("/episodes/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_episode(id):
    episode = Episode.query.get(id)
    if not episode:
        return {"error": "Episode not found"}, 404

    db.session.delete(episode)
    db.session.commit()
    return {"message": "Episode deleted successfully."}, 200
