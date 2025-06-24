from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from server.models import db, Appearance, Guest, Episode

appearance_bp = Blueprint("appearances", __name__)

@appearance_bp.route("/appearances", methods=["POST"])
@jwt_required()
def create_appearance():
    data = request.get_json()

    try:
        rating = int(data.get("rating"))
        guest_id = int(data.get("guest_id"))
        episode_id = int(data.get("episode_id"))
    except (TypeError, ValueError):
        return {"error": "Invalid or missing data."}, 400

    
    guest = Guest.query.get(guest_id)
    episode = Episode.query.get(episode_id)

    if not guest or not episode:
        return {"error": "Guest or episode not found."}, 404

    try:
        appearance = Appearance(
            rating=rating,
            guest_id=guest_id,
            episode_id=episode_id
        )
        db.session.add(appearance)
        db.session.commit()
        return jsonify(appearance.to_dict()), 201
    except Exception as e:
        return {"error": str(e)}, 400
