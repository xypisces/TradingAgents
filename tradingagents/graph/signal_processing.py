# TradingAgents/graph/signal_processing.py

from langchain_openai import ChatOpenAI
from tradingagents.i18n import get_agent_language_instruction


class SignalProcessor:
    """Processes trading signals to extract actionable decisions."""

    def __init__(self, quick_thinking_llm: ChatOpenAI, config=None):
        """Initialize with an LLM for processing."""
        self.quick_thinking_llm = quick_thinking_llm
        self.config = config or {}

    def process_signal(self, full_signal: str) -> str:
        """
        Process a full trading signal to extract the core decision.

        Args:
            full_signal: Complete trading signal text

        Returns:
            Extracted decision (BUY, SELL, or HOLD)
        """
        lang = self.config.get("lang", "en")
        lang_instruction = get_agent_language_instruction(lang)

        messages = [
            (
                "system",
                "You are an efficient assistant designed to analyze paragraphs or financial reports provided by a group of analysts. Your task is to extract the investment decision: SELL, BUY, or HOLD. Provide only the extracted decision (SELL, BUY, or HOLD) as your output, without adding any additional text or information."
                + lang_instruction,
            ),
            ("human", full_signal),
        ]

        return self.quick_thinking_llm.invoke(messages).content
