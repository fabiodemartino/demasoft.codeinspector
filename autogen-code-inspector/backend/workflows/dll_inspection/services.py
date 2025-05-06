import os
import uuid
import subprocess

UPLOAD_DIR = "/tmp/dlls"

def inspect_dll(file):
    session_id = str(uuid.uuid4())
    save_path = os.path.join(UPLOAD_DIR, f"{session_id}.dll")
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    file.save(save_path)

    # Run ILSpyCmd or another .NET decompiler — this is a placeholder
    try:
        result = subprocess.run(
            ["ilspycmd", "-p", save_path],
            capture_output=True, text=True, check=True
        )
        return {"output": result.stdout}
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Decompiler failed: {e.stderr}")
