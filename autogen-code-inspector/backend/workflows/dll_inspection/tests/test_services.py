import pytest
from io import BytesIO
from workflows.dll_inspection.services import inspect_dll

@pytest.mark.skip(reason="Requires ILSpyCmd installed and configured")
def test_inspect_dll_success():
    dll_content = BytesIO(b"MZ dummy dll data")
    dll_content.filename = "test.dll"

    class DummyFile:
        def __init__(self, stream): self.stream = stream
        def save(self, path):
            with open(path, 'wb') as f:
                f.write(self.stream.read())

    result = inspect_dll(DummyFile(dll_content))
    assert "output" in result
