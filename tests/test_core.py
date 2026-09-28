import pytest
from src.core import Redactor
from src.models import RedactionConfig

def test_redaction():
    cfg = RedactionConfig(patterns={'email': r'\S+@\S+'}, json_keys=['secret'])
    redactor = Redactor(cfg)
    assert 'EMAIL_REDACTED' in redactor.redact_text('test@example.com')
    assert redactor.redact_json({'secret': '123'}) == {'secret': 'REDACTED'}