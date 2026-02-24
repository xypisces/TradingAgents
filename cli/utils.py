import questionary
from typing import List, Optional, Tuple, Dict

from cli.models import AnalystType
from tradingagents.i18n import get_text

ANALYST_ORDER = [
    ("Market Analyst", AnalystType.MARKET),
    ("Social Media Analyst", AnalystType.SOCIAL),
    ("News Analyst", AnalystType.NEWS),
    ("Fundamentals Analyst", AnalystType.FUNDAMENTALS),
]


def select_language() -> str:
    """Prompt the user to select a language."""
    LANGUAGE_OPTIONS = [
        ("English", "en"),
        ("中文 (Simplified Chinese)", "cn"),
    ]

    choice = questionary.select(
        "Select Language / 选择语言:",
        choices=[
            questionary.Choice(display, value=value)
            for display, value in LANGUAGE_OPTIONS
        ],
        instruction="\n- Use arrow keys to navigate\n- Press Enter to select",
        style=questionary.Style(
            [
                ("selected", "fg:green noinherit"),
                ("highlighted", "fg:green noinherit"),
                ("pointer", "fg:green noinherit"),
            ]
        ),
    ).ask()

    if choice is None:
        print("\n[red]No language selected. Defaulting to English...[/red]")
        return "en"

    return choice


def get_ticker(lang="en") -> str:
    """Prompt the user to enter a ticker symbol."""
    ticker = questionary.text(
        get_text("select_ticker_prompt", lang),
        validate=lambda x: len(x.strip()) > 0 or get_text("select_ticker_validate", lang),
        style=questionary.Style(
            [
                ("text", "fg:green"),
                ("highlighted", "noinherit"),
            ]
        ),
    ).ask()

    if not ticker:
        print(get_text("no_ticker_error", lang))
        exit(1)

    return ticker.strip().upper()


def get_analysis_date(lang="en") -> str:
    """Prompt the user to enter a date in YYYY-MM-DD format."""
    import re
    from datetime import datetime

    def validate_date(date_str: str) -> bool:
        if not re.match(r"^\d{4}-\d{2}-\d{2}$", date_str):
            return False
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return True
        except ValueError:
            return False

    date = questionary.text(
        get_text("select_date_prompt", lang),
        validate=lambda x: validate_date(x.strip())
        or get_text("select_date_validate", lang),
        style=questionary.Style(
            [
                ("text", "fg:green"),
                ("highlighted", "noinherit"),
            ]
        ),
    ).ask()

    if not date:
        print(get_text("no_date_error", lang))
        exit(1)

    return date.strip()


def select_analysts(lang="en") -> List[AnalystType]:
    """Select analysts using an interactive checkbox."""
    choices = questionary.checkbox(
        get_text("select_analysts_prompt", lang),
        choices=[
            questionary.Choice(display, value=value) for display, value in ANALYST_ORDER
        ],
        instruction=get_text("select_analysts_instruction", lang),
        validate=lambda x: len(x) > 0 or get_text("select_analysts_validate", lang),
        style=questionary.Style(
            [
                ("checkbox-selected", "fg:green"),
                ("selected", "fg:green noinherit"),
                ("highlighted", "noinherit"),
                ("pointer", "noinherit"),
            ]
        ),
    ).ask()

    if not choices:
        print(get_text("no_analysts_error", lang))
        exit(1)

    return choices


def select_research_depth(lang="en") -> int:
    """Select research depth using an interactive selection."""

    # Define research depth options with their corresponding values
    DEPTH_OPTIONS = [
        (get_text("depth_shallow", lang), 1),
        (get_text("depth_medium", lang), 3),
        (get_text("depth_deep", lang), 5),
    ]

    choice = questionary.select(
        get_text("select_depth_prompt", lang),
        choices=[
            questionary.Choice(display, value=value) for display, value in DEPTH_OPTIONS
        ],
        instruction=get_text("select_depth_instruction", lang),
        style=questionary.Style(
            [
                ("selected", "fg:yellow noinherit"),
                ("highlighted", "fg:yellow noinherit"),
                ("pointer", "fg:yellow noinherit"),
            ]
        ),
    ).ask()

    if choice is None:
        print(get_text("no_depth_error", lang))
        exit(1)

    return choice


def select_shallow_thinking_agent(provider, lang="en") -> str:
    """Select shallow thinking llm engine using an interactive selection."""

    # Define shallow thinking llm engine options with their corresponding model names
    SHALLOW_AGENT_OPTIONS = {
        "openai": [
            ("GPT-5 Mini - Cost-optimized reasoning", "gpt-5-mini"),
            ("GPT-5 Nano - Ultra-fast, high-throughput", "gpt-5-nano"),
            ("GPT-5.2 - Latest flagship", "gpt-5.2"),
            ("GPT-5.1 - Flexible reasoning", "gpt-5.1"),
            ("GPT-4.1 - Smartest non-reasoning, 1M context", "gpt-4.1"),
        ],
        "anthropic": [
            ("Claude Haiku 4.5 - Fast + extended thinking", "claude-haiku-4-5"),
            ("Claude Sonnet 4.5 - Best for agents/coding", "claude-sonnet-4-5"),
            ("Claude Sonnet 4 - High-performance", "claude-sonnet-4-20250514"),
            ("Claude Sonnet 4.6 - High-performance-4.6", "claude-sonnet-4-6"),
        ],
        "google": [
            ("Gemini 3 Flash - Next-gen fast", "gemini-3-flash-preview"),
            ("Gemini 2.5 Flash - Balanced, recommended", "gemini-2.5-flash"),
            ("Gemini 3 Pro - Reasoning-first", "gemini-3-pro-preview"),
            ("Gemini 2.5 Flash Lite - Fast, low-cost", "gemini-2.5-flash-lite"),
        ],
        "xai": [
            ("Grok 4.1 Fast (Non-Reasoning) - Speed optimized, 2M ctx", "grok-4-1-fast-non-reasoning"),
            ("Grok 4 Fast (Non-Reasoning) - Speed optimized", "grok-4-fast-non-reasoning"),
            ("Grok 4.1 Fast (Reasoning) - High-performance, 2M ctx", "grok-4-1-fast-reasoning"),
            ("Grok 4 Fast (Reasoning) - High-performance", "grok-4-fast-reasoning"),
        ],
        "openrouter": [
            ("NVIDIA Nemotron 3 Nano 30B (free)", "nvidia/nemotron-3-nano-30b-a3b:free"),
            ("Z.AI GLM 4.5 Air (free)", "z-ai/glm-4.5-air:free"),
        ],
        "ollama": [
            ("Qwen3:latest (8B, local)", "qwen3:latest"),
            ("GPT-OSS:latest (20B, local)", "gpt-oss:latest"),
            ("GLM-4.7-Flash:latest (30B, local)", "glm-4.7-flash:latest"),
        ],
    }

    choice = questionary.select(
        get_text("select_quick_llm_prompt", lang),
        choices=[
            questionary.Choice(display, value=value)
            for display, value in SHALLOW_AGENT_OPTIONS[provider.lower()]
        ],
        instruction=get_text("select_depth_instruction", lang),
        style=questionary.Style(
            [
                ("selected", "fg:magenta noinherit"),
                ("highlighted", "fg:magenta noinherit"),
                ("pointer", "fg:magenta noinherit"),
            ]
        ),
    ).ask()

    if choice is None:
        print(get_text("no_quick_llm_error", lang))
        exit(1)

    return choice


def select_deep_thinking_agent(provider, lang="en") -> str:
    """Select deep thinking llm engine using an interactive selection."""

    # Define deep thinking llm engine options with their corresponding model names
    DEEP_AGENT_OPTIONS = {
        "openai": [
            ("GPT-5.2 - Latest flagship", "gpt-5.2"),
            ("GPT-5.1 - Flexible reasoning", "gpt-5.1"),
            ("GPT-5 - Advanced reasoning", "gpt-5"),
            ("GPT-4.1 - Smartest non-reasoning, 1M context", "gpt-4.1"),
            ("GPT-5 Mini - Cost-optimized reasoning", "gpt-5-mini"),
            ("GPT-5 Nano - Ultra-fast, high-throughput", "gpt-5-nano"),
        ],
        "anthropic": [
            ("Claude Sonnet 4.5 - Best for agents/coding", "claude-sonnet-4-5"),
            ("Claude Opus 4.5 - Premium, max intelligence", "claude-opus-4-5"),
            ("Claude Opus 4.1 - Most capable model", "claude-opus-4-1-20250805"),
            ("Claude Haiku 4.5 - Fast + extended thinking", "claude-haiku-4-5"),
            ("Claude Sonnet 4 - High-performance", "claude-sonnet-4-20250514"),
            ("Claude Sonnet 4.6 - High-performance-4.6", "claude-sonnet-4-6"),
        ],
        "google": [
            ("Gemini 3 Pro - Reasoning-first", "gemini-3-pro-preview"),
            ("Gemini 3 Flash - Next-gen fast", "gemini-3-flash-preview"),
            ("Gemini 2.5 Flash - Balanced, recommended", "gemini-2.5-flash"),
        ],
        "xai": [
            ("Grok 4.1 Fast (Reasoning) - High-performance, 2M ctx", "grok-4-1-fast-reasoning"),
            ("Grok 4 Fast (Reasoning) - High-performance", "grok-4-fast-reasoning"),
            ("Grok 4 - Flagship model", "grok-4-0709"),
            ("Grok 4.1 Fast (Non-Reasoning) - Speed optimized, 2M ctx", "grok-4-1-fast-non-reasoning"),
            ("Grok 4 Fast (Non-Reasoning) - Speed optimized", "grok-4-fast-non-reasoning"),
        ],
        "openrouter": [
            ("Z.AI GLM 4.5 Air (free)", "z-ai/glm-4.5-air:free"),
            ("NVIDIA Nemotron 3 Nano 30B (free)", "nvidia/nemotron-3-nano-30b-a3b:free"),
        ],
        "ollama": [
            ("GLM-4.7-Flash:latest (30B, local)", "glm-4.7-flash:latest"),
            ("GPT-OSS:latest (20B, local)", "gpt-oss:latest"),
            ("Qwen3:latest (8B, local)", "qwen3:latest"),
        ],
    }

    choice = questionary.select(
        get_text("select_deep_llm_prompt", lang),
        choices=[
            questionary.Choice(display, value=value)
            for display, value in DEEP_AGENT_OPTIONS[provider.lower()]
        ],
        instruction=get_text("select_depth_instruction", lang),
        style=questionary.Style(
            [
                ("selected", "fg:magenta noinherit"),
                ("highlighted", "fg:magenta noinherit"),
                ("pointer", "fg:magenta noinherit"),
            ]
        ),
    ).ask()

    if choice is None:
        print(get_text("no_deep_llm_error", lang))
        exit(1)

    return choice

def select_llm_provider(lang="en") -> tuple[str, str]:
    """Select the OpenAI api url using interactive selection."""
    import os

    # Default URLs per provider; BACKEND_URL env-var overrides all of them
    # so that a custom proxy address never has to appear in source code.
    env_url = os.getenv("BACKEND_URL", "").rstrip("/")

    BASE_URLS = [
        ("OpenAI", "https://api.openai.com/v1"),
        ("Google", "https://generativelanguage.googleapis.com/v1"),
        ("Anthropic", env_url),
        ("xAI", "https://api.x.ai/v1"),
        ("Openrouter", "https://openrouter.ai/api/v1"),
        ("Ollama", "http://localhost:11434/v1"),
    ]
    choice = questionary.select(
        get_text("select_provider_prompt", lang),
        choices=[
            questionary.Choice(display, value=(display, value))
            for display, value in BASE_URLS
        ],
        instruction=get_text("select_depth_instruction", lang),
        style=questionary.Style(
            [
                ("selected", "fg:magenta noinherit"),
                ("highlighted", "fg:magenta noinherit"),
                ("pointer", "fg:magenta noinherit"),
            ]
        ),
    ).ask()
    
    if choice is None:
        print(get_text("no_provider_error", lang))
        exit(1)
    
    display_name, url = choice
    print(f"You selected: {display_name}\tURL: {url}")

    return display_name, url


def ask_openai_reasoning_effort() -> str:
    """Ask for OpenAI reasoning effort level."""
    choices = [
        questionary.Choice("Medium (Default)", "medium"),
        questionary.Choice("High (More thorough)", "high"),
        questionary.Choice("Low (Faster)", "low"),
    ]
    return questionary.select(
        "Select Reasoning Effort:",
        choices=choices,
        style=questionary.Style([
            ("selected", "fg:cyan noinherit"),
            ("highlighted", "fg:cyan noinherit"),
            ("pointer", "fg:cyan noinherit"),
        ]),
    ).ask()


def ask_gemini_thinking_config() -> str | None:
    """Ask for Gemini thinking configuration.

    Returns thinking_level: "high" or "minimal".
    Client maps to appropriate API param based on model series.
    """
    return questionary.select(
        "Select Thinking Mode:",
        choices=[
            questionary.Choice("Enable Thinking (recommended)", "high"),
            questionary.Choice("Minimal/Disable Thinking", "minimal"),
        ],
        style=questionary.Style([
            ("selected", "fg:green noinherit"),
            ("highlighted", "fg:green noinherit"),
            ("pointer", "fg:green noinherit"),
        ]),
    ).ask()


def format_tool_args(args, max_length=80) -> str:
    """Format tool arguments for terminal display."""
    result = str(args)
    if len(result) > max_length:
        return result[:max_length - 3] + "..."
    return result
