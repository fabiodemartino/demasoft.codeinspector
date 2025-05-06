from flask import Blueprint, request, jsonify
from .services import trigger_training

bp = Blueprint("training", __name__)

@bp.route("/train", methods=["POST"])
def train():
    try:
        config = request.get_json()
        result = trigger_training(config)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
