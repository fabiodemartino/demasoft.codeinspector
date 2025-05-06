from flask import Blueprint, request, jsonify
from .services import inspect_dll

bp = Blueprint("dll_inspection", __name__)

@bp.route("/inspect-dll", methods=["POST"])
def inspect_uploaded_dll():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']
    if not file.filename.endswith('.dll'):
        return jsonify({"error": "Only .dll files are supported"}), 400

    try:
        result = inspect_dll(file)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
