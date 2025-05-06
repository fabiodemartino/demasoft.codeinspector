import os
import zipfile
import shutil
from io import BytesIO
from workflows.code_upload.services import handle_zip_upload

def test_handle_zip_upload_creates_directory():
    memory_zip = BytesIO()
    with zipfile.ZipFile(memory_zip, mode="w") as zf:
        zf.writestr("hello.txt", "world")
    memory_zip.seek(0)

    class FakeFile:
        def __init__(self, stream):
            self.stream = stream
            self.filename = "test.zip"
        
        def save(self, path):
            with open(path, 'wb') as f:
                f.write(self.stream.read())

    fake_file = FakeFile(memory_zip)
    project_number = 12345  # Example project number
    result_path = handle_zip_upload(fake_file, project_number)

    try:
        # Verify the directory was created
        assert os.path.exists(result_path)
        assert os.path.isdir(result_path)  # Ensure it's a directory

        # Verify the file is extracted correctly
        expected_file_path = os.path.join(result_path, "hello.txt")
        expected_file_path = os.path.normpath(expected_file_path)  # Normalize path for cross-platform consistency
        
        assert os.path.isfile(expected_file_path)

        # Verify that the directory structure includes the project number
        project_dir = os.path.join(result_path, f"project_{project_number}")
        project_dir = os.path.normpath(project_dir)  # Normalize path for cross-platform consistency
        
        assert os.path.exists(project_dir)  # Check if the project folder exists
        
    finally:
        # Clean up
        if os.path.exists(result_path):
            shutil.rmtree(result_path)
        zip_path = result_path + ".zip"
        if os.path.exists(zip_path):
            os.remove(zip_path)
