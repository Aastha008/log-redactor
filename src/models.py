from pydantic import BaseModel, Field
from typing import List, Dict, Any

class RedactionConfig(BaseModel):
    patterns: Dict[str, str]
    json_keys: List[str]

class RedactionRequest(BaseModel):
    text: str
    is_json: bool = False

class RedactionResponse(BaseModel):
    redacted_text: str