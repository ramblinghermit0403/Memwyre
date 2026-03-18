import sys
from pathlib import Path


backend_path = str(Path(__file__).parent.parent)
if backend_path not in sys.path:
    sys.path.insert(0, backend_path)

from app.services.agent_service import AgentService


def test_normalize_malformed_think_block():
    service = AgentService()
    raw = "Quick answer intro\n<think>unfinished reasoning"
    normalized = service._normalize_agent_output(raw)

    assert "<think>" not in normalized
    assert "</think>" not in normalized
    assert "Quick answer intro" in normalized


def test_normalize_valid_reasoning_and_remove_stray_tags():
    service = AgentService()
    raw = "<thinking>\nReasoning details\n</thinking>\n\nFinal answer.\n</think>"
    normalized = service._normalize_agent_output(raw)

    assert normalized.count("<think>") == 1
    assert normalized.count("</think>") == 1
    assert "Reasoning details" in normalized
    assert "Final answer." in normalized


def test_normalize_dedupes_repeated_headings_and_separators():
    service = AgentService()
    raw = "## Key Points\n## Key Points\n- Item\n---\n***\n\n\nDone"
    normalized = service._normalize_markdown_block(raw)

    assert normalized.count("## Key Points") == 1
    assert normalized.count("---") == 1
    assert "\n\n\n" not in normalized


def test_normalize_preserves_clean_content():
    service = AgentService()
    raw = "## Summary\n- One\n- Two\n\nFinal line."
    normalized = service._normalize_markdown_block(raw)

    assert normalized == raw
