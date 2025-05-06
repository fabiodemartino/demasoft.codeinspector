import subprocess
import tempfile
import json

def trigger_training(config):
    with tempfile.NamedTemporaryFile("w", delete=False, suffix=".json") as f:
        json.dump(config, f)
        config_path = f.name

    # This assumes `train.py` is accessible in the container's PATH
    try:
        result = subprocess.run(
            ["python", "trainer/train.py", "--config", config_path],
            capture_output=True, text=True, check=True
        )
        return {"status": "training_started", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Training failed: {e.stderr}")
