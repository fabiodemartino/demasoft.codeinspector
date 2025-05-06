from flask import Blueprint, request, jsonify
from .sql_parser import parse_sql_script

bp = Blueprint("sql_analysis", __name__)

@bp.route("/analyze-sql", methods=["POST"])
def analyze_sql():
    content = request.get_json()
    script = content.get("script", "")
    try:
        result = parse_sql_script(script)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 400
