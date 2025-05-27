from ii_agent.llm.base import LLMClient
from ii_agent.llm.openai import OpenAIDirectClient


def get_client(client_name: str, **kwargs) -> LLMClient:
    """Get a client for a given client name."""
    if client_name in ["openai-direct", "deepseek", "anthropic-direct"]:
        # All use OpenAI-compatible client now
        return OpenAIDirectClient(**kwargs)
    else:
        raise ValueError(f"Unknown client name: {client_name}")


__all__ = [
    "LLMClient",
    "OpenAIDirectClient",
    "get_client",
]
