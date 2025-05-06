from flask import Blueprint, request, jsonify
from .services import handle_zip_upload

bp = Blueprint("code_upload", __name__)

@bp.route("/upload", methods=["POST"])
def upload_code():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    try:
        output_path = handle_zip_upload(file)
        return jsonify({"message": "Upload successful", "extracted_to": output_path})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
