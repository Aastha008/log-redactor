from fastapi import FastAPI, Depends
from src.models import RedactionRequest, RedactionResponse
from src.core import Redactor
from src.config import load_config

app = FastAPI()
redactor = Redactor(load_config())

@app.post("/redact")
def redact(req: RedactionRequest) -> RedactionResponse:
    if req.is_json:
        try:
            data = json.loads(req.text)
            return RedactionResponse(redacted_text=json.dumps(redactor.redact_json(data)))
        except:
            pass
    return RedactionResponse(redacted_text=redactor.redact_text(req.text))