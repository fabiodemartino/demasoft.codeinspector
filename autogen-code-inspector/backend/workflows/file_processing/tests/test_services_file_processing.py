import zipfile
import pytest
import tempfile
from io import BytesIO
from workflows.file_processing.services import process_file_upload

class DummyFile:
    def __init__(self, stream, filename):
        self.stream = stream
        self.filename = filename

    def save(self, path):
        with open(path, 'wb') as f:
            self.stream.seek(0)
            f.write(self.stream.read())

def test_process_file_upload():
    # Create an in-memory ZIP file
    dummy_zip = BytesIO()
    with zipfile.ZipFile(dummy_zip, 'w') as zipf:
        zipf.writestr('dummy_file.txt', 'Hello, World!')
    dummy_zip.seek(0)

    # Create a dummy file-like object with filename
    dummy_file = DummyFile(dummy_zip, "test.zip")

    # Use a temporary directory to avoid filesystem pollution
    with tempfile.TemporaryDirectory() as temp_dir:
        result = process_file_upload(dummy_file, upload_dir=temp_dir)

        assert result["message"] == "File uploaded and extracted"
        assert isinstance(result["files"], list)
        assert len(result["files"]) > 0
        assert any("dummy_file.txt" in f for f in result["files"])
