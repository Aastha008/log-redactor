import yaml
from pathlib import Path
from src.models import RedactionConfig

def load_config(path: str = 'config.yaml') -> RedactionConfig:
    with open(path, 'r') as f:
        data = yaml.safe_load(f)
    return RedactionConfig(**data)