import os
import zipfile
import uuid

UPLOAD_DIR = "/tmp/uploads"  # Adjust this path for your environment (e.g., for Windows use 'C:\\temp\\uploads')

def handle_zip_upload(file, project_number):
    if not file.filename.endswith(".zip"):
        raise ValueError("Only ZIP files are supported")

    session_id = str(uuid.uuid4())
    extract_path = os.path.join(UPLOAD_DIR, session_id)
    os.makedirs(extract_path, exist_ok=True)

    zip_path = os.path.join(UPLOAD_DIR, f"{session_id}.zip")
    file.save(zip_path)

    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)

    # Create a project-specific directory
    project_dir = os.path.join(extract_path, f"project_{project_number}")
    os.makedirs(project_dir, exist_ok=True)

    # Move the extracted files into the project folder
    for item in os.listdir(extract_path):
        s = os.path.join(extract_path, item)
        d = os.path.join(project_dir, item)
        if os.path.isdir(s):
            # If it's a directory, move its contents, not the directory itself
            for sub_item in os.listdir(s):
                sub_s = os.path.join(s, sub_item)
                sub_d = os.path.join(d, sub_item)
                os.rename(sub_s, sub_d)
        else:
            # Move individual files
            os.rename(s, d)

    os.remove(zip_path)
    return project_dir  # Returning the project directory
