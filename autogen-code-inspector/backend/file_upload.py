import os
import logging
from flask import Flask, request, jsonify
from flask_cors import CORS  # Import Flask-CORS

app = Flask(__name__)
# Get the frontend origin from env or default
frontend_origin = os.getenv("FRONTEND_ORIGIN", "http://localhost:3000")

CORS(app, origins=[frontend_origin])
 
# Set up logging
logging.basicConfig(level=logging.DEBUG)  # You can change the level to ERROR for production
logger = logging.getLogger(__name__)

# Get the volume path from the environment variable
VOLUME_PATH = os.getenv("VOLUME_PATH", "/default/path")  # Provide a default value if not set
UPLOAD_FOLDER = os.path.join(VOLUME_PATH, 'uploads')

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        # Check if the 'file' part is present in the request
        if 'file' not in request.files:
            logger.error("No file part in the request.")
            return jsonify({"error": "No file part"}), 400
        
        file = request.files['file']

        # Check if the file has a filename
        if file.filename == '':
            logger.error("No selected file.")
            return jsonify({"error": "No selected file"}), 400
        
        # Save the file
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)

        # Log successful upload
        logger.info(f"File uploaded successfully: {file.filename}")

        return jsonify({"message": "File uploaded successfully!"})

    except Exception as e:
        # Log the exception
        logger.exception(f"An error occurred while uploading the file: {str(e)}")
        return jsonify({"error": "An internal server error occurred during file upload."}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
