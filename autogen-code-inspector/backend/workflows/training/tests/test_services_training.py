import pytest
from workflows.training.services import trigger_training

@pytest.mark.skip(reason="Training process is external and slow")
def test_trigger_training_valid_config():
    config = {
        "model_name": "mistral",
        "dataset_path": "trainer/data/my_dataset.json",
        "output_dir": "trainer/model/",
        "epochs": 3
    }
    result = trigger_training(config)
    assert result["status"] == "training_started"
