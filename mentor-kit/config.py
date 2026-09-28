"""The only place provider and model IDs live. Change provider by setting env vars; no code changes."""
import os

PROVIDER = os.getenv("PROVIDER", "anthropic")          # openai, google_genai, mistralai, ollama, ...
CHAT_MODEL = os.getenv("CHAT_MODEL", "claude-opus-5")
JUDGE_MODEL = os.getenv("JUDGE_MODEL", "claude-sonnet-5")
FAST_MODEL = os.getenv("FAST_MODEL", "claude-haiku-4-5")
EMBED_MODEL = os.getenv("EMBED_MODEL", "sentence-transformers/all-mpnet-base-v2")  # local, open source


def model_id(name: str) -> str:
    """'provider:model' string accepted by langchain's init_chat_model and create_agent."""
    return f"{PROVIDER}:{name}"
