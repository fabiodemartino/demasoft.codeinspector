import os
import zipfile
from werkzeug.utils import secure_filename
import shutil
from io import BytesIO

# Default upload directory
UPLOAD_DIR = "/tmp/uploads"
ALLOWED_EXTENSIONS = {'zip'}

def allowed_file(filename):
    """Check if the uploaded file is a valid .zip file"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def process_file_upload(file, upload_dir=None):
    """Process the uploaded file, ensuring it is a valid .zip file."""
    if not allowed_file(file.filename):
        raise ValueError("File type not allowed. Only .zip files are supported.")

    # If a custom upload directory is provided, use it
    upload_dir = upload_dir or UPLOAD_DIR

    filename = secure_filename(file.filename)
    save_path = os.path.join(upload_dir, filename)

    os.makedirs(upload_dir, exist_ok=True)
    file.save(save_path)

    extracted_files = extract_zip(save_path, upload_dir)
    return {"message": "File uploaded and extracted", "files": extracted_files}

def extract_zip(zip_path, upload_dir):
    """Extract the .zip file to a directory."""
    extracted_dir = os.path.join(upload_dir, "extracted")
    os.makedirs(extracted_dir, exist_ok=True)

    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extracted_dir)

    # Return list of extracted files
    return [os.path.join(extracted_dir, f) for f in os.listdir(extracted_dir)]

