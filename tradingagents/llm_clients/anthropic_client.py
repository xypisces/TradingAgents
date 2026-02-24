from typing import Any, Optional

from langchain_anthropic import ChatAnthropic

from .base_client import BaseLLMClient
from .validators import validate_model


class AnthropicClient(BaseLLMClient):
    """Client for Anthropic Claude models."""

    def __init__(self, model: str, base_url: Optional[str] = None, **kwargs):
        super().__init__(model, base_url, **kwargs)

    def get_llm(self) -> Any:
        """Return configured ChatAnthropic instance."""
        llm_kwargs = {"model": self.model}
        
        if self.base_url:
            llm_kwargs["anthropic_api_url"] = self.base_url
            # Proxy services may block the SDK's default User-Agent
            # ("Anthropic/Python x.x.x"). Override it for compatibility.
            llm_kwargs["default_headers"] = {"User-Agent": "python-httpx"}

        for key in ("timeout", "max_retries", "api_key", "max_tokens", "callbacks"):
            if key in self.kwargs:
                llm_kwargs[key] = self.kwargs[key]

        return ChatAnthropic(**llm_kwargs)

    def validate_model(self) -> bool:
        """Validate model for Anthropic."""
        return validate_model("anthropic", self.model)
