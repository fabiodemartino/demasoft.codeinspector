from flask import Blueprint, request, jsonify
from .services import process_file_upload

bp = Blueprint("file_processing", __name__)

@bp.route("/upload", methods=["POST"])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    try:
        result = process_file_upload(file)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
