from flask import Blueprint, request, jsonify
from .services import query_vector_db

bp = Blueprint("query_handling", __name__)

@bp.route("/query", methods=["POST"])
def query():
    try:
        data = request.get_json()
        if not data or "query" not in data:
            return jsonify({"error": "Missing 'query' in request"}), 400

        results = query_vector_db(data["query"])
        return jsonify(results)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
