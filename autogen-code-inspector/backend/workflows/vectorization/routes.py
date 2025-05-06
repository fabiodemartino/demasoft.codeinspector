from flask import Blueprint, request, jsonify
from .services import vectorize_documents

bp = Blueprint("vectorization", __name__)

@bp.route("/vectorize", methods=["POST"])
def vectorize():
    try:
        data = request.get_json()
        if not data or "documents" not in data:
            return jsonify({"error": "Missing 'documents' in request"}), 400

        results = vectorize_documents(data["documents"])
        return jsonify(results)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
