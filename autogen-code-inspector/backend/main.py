from flask import Flask
from workflows.code_upload.routes import bp as upload_bp
from workflows.sql_analysis.routes import bp as sql_bp
from workflows.dll_inspection.routes import bp as dll_bp
from workflows.training.routes import bp as training_bp
from workflows.vectorization.routes import bp as vector_bp
from workflows.query_handling.routes import bp as query_bp
from workflows.file_processing.routes import bp as file_processing_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(upload_bp, url_prefix="/api")
    app.register_blueprint(sql_bp, url_prefix="/api")
    app.register_blueprint(dll_bp, url_prefix="/api")
    app.register_blueprint(training_bp, url_prefix="/api")
    app.register_blueprint(vector_bp, url_prefix="/api")
    app.register_blueprint(query_bp, url_prefix="/api")
    app.register_blueprint(file_processing_bp, url_prefix="/api")

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host="0.0.0.0", port=5000)
