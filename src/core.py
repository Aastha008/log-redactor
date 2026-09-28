import re
import json
from typing import Dict
from src.models import RedactionConfig

class Redactor:
    def __init__(self, config: RedactionConfig):
        self.config = config
        self.compiled_patterns = {k: re.compile(v) for k, v in config.patterns.items()}

    def redact_text(self, text: str) -> str:
        for name, pattern in self.compiled_patterns.items():
            text = pattern.sub(f'[{name.upper()}_REDACTED]', text)
        return text

    def redact_json(self, data: Dict) -> Dict:
        if isinstance(data, dict):
            return {k: (self.redact_json(v) if k not in self.config.json_keys else 'REDACTED') for k, v in data.items()}
        elif isinstance(data, list):
            return [self.redact_json(i) for i in data]
        return data

    def process_stream(self, stream):
        for line in stream:
            try:
                data = json.loads(line)
                yield json.dumps(self.redact_json(data)) + '\n'
            except json.JSONDecodeError:
                yield self.redact_text(line)