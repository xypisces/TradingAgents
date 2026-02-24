"""
Internationalization (i18n) module for TradingAgents.
Supports English ("en") and Simplified Chinese ("cn").
"""

TRANSLATIONS = {
    # ========== CLI Welcome & Titles ==========
    "welcome_title": {
        "en": "Welcome to TradingAgents",
        "cn": "欢迎使用 TradingAgents",
    },
    "welcome_subtitle": {
        "en": "Multi-Agents LLM Financial Trading Framework",
        "cn": "多智能体 LLM 金融交易框架",
    },
    "welcome_body": {
        "en": "[bold green]TradingAgents: Multi-Agents LLM Financial Trading Framework - CLI[/bold green]",
        "cn": "[bold green]TradingAgents: 多智能体 LLM 金融交易框架 - CLI[/bold green]",
    },
    "workflow_steps_label": {
        "en": "[bold]Workflow Steps:[/bold]",
        "cn": "[bold]工作流程:[/bold]",
    },
    "workflow_steps": {
        "en": "I. Analyst Team → II. Research Team → III. Trader → IV. Risk Management → V. Portfolio Management",
        "cn": "I. 分析师团队 → II. 研究团队 → III. 交易员 → IV. 风险管理 → V. 投资组合管理",
    },

    # ========== Step Titles ==========
    "step_language_title": {
        "en": "Step 0: Language",
        "cn": "第 0 步: 语言选择",
    },
    "step_language_prompt": {
        "en": "Select the output language",
        "cn": "请选择输出语言",
    },
    "step_ticker_title": {
        "en": "Step 1: Ticker Symbol",
        "cn": "第 1 步: 股票代码",
    },
    "step_ticker_prompt": {
        "en": "Enter the ticker symbol to analyze",
        "cn": "请输入要分析的股票代码",
    },
    "step_date_title": {
        "en": "Step 2: Analysis Date",
        "cn": "第 2 步: 分析日期",
    },
    "step_date_prompt": {
        "en": "Enter the analysis date (YYYY-MM-DD)",
        "cn": "请输入分析日期 (YYYY-MM-DD)",
    },
    "step_analysts_title": {
        "en": "Step 3: Analysts Team",
        "cn": "第 3 步: 分析师团队",
    },
    "step_analysts_prompt": {
        "en": "Select your LLM analyst agents for the analysis",
        "cn": "选择用于分析的 LLM 分析师智能体",
    },
    "step_depth_title": {
        "en": "Step 4: Research Depth",
        "cn": "第 4 步: 研究深度",
    },
    "step_depth_prompt": {
        "en": "Select your research depth level",
        "cn": "选择研究深度级别",
    },
    "step_provider_title": {
        "en": "Step 5: LLM Provider",
        "cn": "第 5 步: LLM 服务商",
    },
    "step_provider_prompt": {
        "en": "Select which service to talk to",
        "cn": "选择 LLM 服务商",
    },
    "step_thinking_title": {
        "en": "Step 6: Thinking Agents",
        "cn": "第 6 步: 思考引擎",
    },
    "step_thinking_prompt": {
        "en": "Select your thinking agents for analysis",
        "cn": "选择用于分析的思考引擎",
    },
    "step_thinking_mode_title": {
        "en": "Step 7: Thinking Mode",
        "cn": "第 7 步: 思考模式",
    },
    "step_thinking_mode_prompt_google": {
        "en": "Configure Gemini thinking mode",
        "cn": "配置 Gemini 思考模式",
    },
    "step_reasoning_title": {
        "en": "Step 7: Reasoning Effort",
        "cn": "第 7 步: 推理力度",
    },
    "step_reasoning_prompt": {
        "en": "Configure OpenAI reasoning effort level",
        "cn": "配置 OpenAI 推理力度级别",
    },

    # ========== Report Section Titles ==========
    "market_analysis": {
        "en": "Market Analysis",
        "cn": "市场分析",
    },
    "social_sentiment": {
        "en": "Social Sentiment",
        "cn": "社交媒体情绪",
    },
    "news_analysis": {
        "en": "News Analysis",
        "cn": "新闻分析",
    },
    "fundamentals_analysis": {
        "en": "Fundamentals Analysis",
        "cn": "基本面分析",
    },
    "research_team_decision": {
        "en": "Research Team Decision",
        "cn": "研究团队决策",
    },
    "trading_team_plan": {
        "en": "Trading Team Plan",
        "cn": "交易团队计划",
    },
    "portfolio_mgmt_decision": {
        "en": "Portfolio Management Decision",
        "cn": "投资组合管理决策",
    },

    # ========== Report Subsection Titles ==========
    "analyst_team_reports": {
        "en": "Analyst Team Reports",
        "cn": "分析师团队报告",
    },
    "bull_researcher_analysis": {
        "en": "Bull Researcher Analysis",
        "cn": "看多研究员分析",
    },
    "bear_researcher_analysis": {
        "en": "Bear Researcher Analysis",
        "cn": "看空研究员分析",
    },
    "research_manager_decision": {
        "en": "Research Manager Decision",
        "cn": "研究经理决策",
    },
    "aggressive_analyst_analysis": {
        "en": "Aggressive Analyst Analysis",
        "cn": "激进分析师分析",
    },
    "conservative_analyst_analysis": {
        "en": "Conservative Analyst Analysis",
        "cn": "保守分析师分析",
    },
    "neutral_analyst_analysis": {
        "en": "Neutral Analyst Analysis",
        "cn": "中性分析师分析",
    },
    "portfolio_manager_decision": {
        "en": "Portfolio Manager Decision",
        "cn": "投资组合经理决策",
    },
    "risk_mgmt_team_decision": {
        "en": "Risk Management Team Decision",
        "cn": "风险管理团队决策",
    },
    "portfolio_manager_decision_section": {
        "en": "Portfolio Manager Decision",
        "cn": "投资组合经理决策",
    },

    # ========== Panel & UI Labels ==========
    "panel_progress": {
        "en": "Progress",
        "cn": "进度",
    },
    "panel_messages": {
        "en": "Messages & Tools",
        "cn": "消息 & 工具",
    },
    "panel_current_report": {
        "en": "Current Report",
        "cn": "当前报告",
    },
    "waiting_for_report": {
        "en": "[italic]Waiting for analysis report...[/italic]",
        "cn": "[italic]正在等待分析报告...[/italic]",
    },
    "complete_analysis_report": {
        "en": "Complete Analysis Report",
        "cn": "完整分析报告",
    },
    "trading_analysis_report": {
        "en": "Trading Analysis Report",
        "cn": "交易分析报告",
    },
    "generated": {
        "en": "Generated",
        "cn": "生成时间",
    },

    # ========== Table Headers ==========
    "col_team": {
        "en": "Team",
        "cn": "团队",
    },
    "col_agent": {
        "en": "Agent",
        "cn": "智能体",
    },
    "col_status": {
        "en": "Status",
        "cn": "状态",
    },
    "col_time": {
        "en": "Time",
        "cn": "时间",
    },
    "col_type": {
        "en": "Type",
        "cn": "类型",
    },
    "col_content": {
        "en": "Content",
        "cn": "内容",
    },

    # ========== Team Names ==========
    "team_analyst": {
        "en": "Analyst Team",
        "cn": "分析师团队",
    },
    "team_research": {
        "en": "Research Team",
        "cn": "研究团队",
    },
    "team_trading": {
        "en": "Trading Team",
        "cn": "交易团队",
    },
    "team_risk": {
        "en": "Risk Management",
        "cn": "风险管理",
    },
    "team_portfolio": {
        "en": "Portfolio Management",
        "cn": "投资组合管理",
    },

    # ========== Agent Names ==========
    "agent_market_analyst": {
        "en": "Market Analyst",
        "cn": "市场分析师",
    },
    "agent_social_analyst": {
        "en": "Social Analyst",
        "cn": "社交分析师",
    },
    "agent_news_analyst": {
        "en": "News Analyst",
        "cn": "新闻分析师",
    },
    "agent_fundamentals_analyst": {
        "en": "Fundamentals Analyst",
        "cn": "基本面分析师",
    },
    "agent_bull_researcher": {
        "en": "Bull Researcher",
        "cn": "看多研究员",
    },
    "agent_bear_researcher": {
        "en": "Bear Researcher",
        "cn": "看空研究员",
    },
    "agent_research_manager": {
        "en": "Research Manager",
        "cn": "研究经理",
    },
    "agent_trader": {
        "en": "Trader",
        "cn": "交易员",
    },
    "agent_aggressive_analyst": {
        "en": "Aggressive Analyst",
        "cn": "激进分析师",
    },
    "agent_neutral_analyst": {
        "en": "Neutral Analyst",
        "cn": "中性分析师",
    },
    "agent_conservative_analyst": {
        "en": "Conservative Analyst",
        "cn": "保守分析师",
    },
    "agent_portfolio_manager": {
        "en": "Portfolio Manager",
        "cn": "投资组合经理",
    },

    # ========== Status Labels ==========
    "status_pending": {
        "en": "pending",
        "cn": "等待中",
    },
    "status_in_progress": {
        "en": "in_progress",
        "cn": "进行中",
    },
    "status_completed": {
        "en": "completed",
        "cn": "已完成",
    },
    "status_error": {
        "en": "error",
        "cn": "错误",
    },

    # ========== Footer Stats ==========
    "stat_agents": {
        "en": "Agents",
        "cn": "智能体",
    },
    "stat_reports": {
        "en": "Reports",
        "cn": "报告",
    },

    # ========== Post-analysis prompts ==========
    "analysis_complete": {
        "en": "\n[bold cyan]Analysis Complete![/bold cyan]\n",
        "cn": "\n[bold cyan]分析完成![/bold cyan]\n",
    },
    "save_report_prompt": {
        "en": "Save report?",
        "cn": "是否保存报告?",
    },
    "save_path_prompt": {
        "en": "Save path (press Enter for default)",
        "cn": "保存路径 (按回车使用默认路径)",
    },
    "report_saved": {
        "en": "\n[green]✓ Report saved to:[/green]",
        "cn": "\n[green]✓ 报告已保存至:[/green]",
    },
    "complete_report_label": {
        "en": "  [dim]Complete report:[/dim]",
        "cn": "  [dim]完整报告:[/dim]",
    },
    "save_error": {
        "en": "[red]Error saving report:",
        "cn": "[red]保存报告出错:",
    },
    "display_report_prompt": {
        "en": "\nDisplay full report on screen?",
        "cn": "\n是否在屏幕上显示完整报告?",
    },

    # ========== Interactive prompts ==========
    "select_ticker_prompt": {
        "en": "Enter the ticker symbol to analyze:",
        "cn": "请输入要分析的股票代码:",
    },
    "select_ticker_validate": {
        "en": "Please enter a valid ticker symbol.",
        "cn": "请输入有效的股票代码。",
    },
    "no_ticker_error": {
        "en": "\n[red]No ticker symbol provided. Exiting...[/red]",
        "cn": "\n[red]未提供股票代码，退出...[/red]",
    },
    "select_date_prompt": {
        "en": "Enter the analysis date (YYYY-MM-DD):",
        "cn": "请输入分析日期 (YYYY-MM-DD):",
    },
    "select_date_validate": {
        "en": "Please enter a valid date in YYYY-MM-DD format.",
        "cn": "请输入有效的日期，格式为 YYYY-MM-DD。",
    },
    "no_date_error": {
        "en": "\n[red]No date provided. Exiting...[/red]",
        "cn": "\n[red]未提供日期，退出...[/red]",
    },
    "select_analysts_prompt": {
        "en": "Select Your [Analysts Team]:",
        "cn": "选择你的 [分析师团队]:",
    },
    "select_analysts_instruction": {
        "en": "\n- Press Space to select/unselect analysts\n- Press 'a' to select/unselect all\n- Press Enter when done",
        "cn": "\n- 按空格键选择/取消选择分析师\n- 按 'a' 全选/取消全选\n- 按回车键确认",
    },
    "select_analysts_validate": {
        "en": "You must select at least one analyst.",
        "cn": "至少需要选择一位分析师。",
    },
    "no_analysts_error": {
        "en": "\n[red]No analysts selected. Exiting...[/red]",
        "cn": "\n[red]未选择分析师，退出...[/red]",
    },
    "selected_analysts_label": {
        "en": "[green]Selected analysts:[/green]",
        "cn": "[green]已选择的分析师:[/green]",
    },
    "select_depth_prompt": {
        "en": "Select Your [Research Depth]:",
        "cn": "选择你的 [研究深度]:",
    },
    "select_depth_instruction": {
        "en": "\n- Use arrow keys to navigate\n- Press Enter to select",
        "cn": "\n- 使用方向键导航\n- 按回车键选择",
    },
    "no_depth_error": {
        "en": "\n[red]No research depth selected. Exiting...[/red]",
        "cn": "\n[red]未选择研究深度，退出...[/red]",
    },
    "select_provider_prompt": {
        "en": "Select your LLM Provider:",
        "cn": "选择你的 LLM 服务商:",
    },
    "no_provider_error": {
        "en": "\n[red]no OpenAI backend selected. Exiting...[/red]",
        "cn": "\n[red]未选择 LLM 服务商，退出...[/red]",
    },
    "select_quick_llm_prompt": {
        "en": "Select Your [Quick-Thinking LLM Engine]:",
        "cn": "选择你的 [快速思考 LLM 引擎]:",
    },
    "no_quick_llm_error": {
        "en": "\n[red]No shallow thinking llm engine selected. Exiting...[/red]",
        "cn": "\n[red]未选择快速思考引擎，退出...[/red]",
    },
    "select_deep_llm_prompt": {
        "en": "Select Your [Deep-Thinking LLM Engine]:",
        "cn": "选择你的 [深度思考 LLM 引擎]:",
    },
    "no_deep_llm_error": {
        "en": "\n[red]No deep thinking llm engine selected. Exiting...[/red]",
        "cn": "\n[red]未选择深度思考引擎，退出...[/red]",
    },
    "select_language_prompt": {
        "en": "Select Language / 选择语言:",
        "cn": "Select Language / 选择语言:",
    },

    # ========== Depth options ==========
    "depth_shallow": {
        "en": "Shallow - Quick research, few debate and strategy discussion rounds",
        "cn": "浅度 - 快速研究，少量辩论和策略讨论轮次",
    },
    "depth_medium": {
        "en": "Medium - Middle ground, moderate debate rounds and strategy discussion",
        "cn": "中度 - 适中研究，中等辩论轮次和策略讨论",
    },
    "depth_deep": {
        "en": "Deep - Comprehensive research, in depth debate and strategy discussion",
        "cn": "深度 - 全面研究，深入辩论和策略讨论",
    },

    # ========== Date validation ==========
    "date_future_error": {
        "en": "[red]Error: Analysis date cannot be in the future[/red]",
        "cn": "[red]错误: 分析日期不能是未来日期[/red]",
    },
    "date_invalid_error": {
        "en": "[red]Error: Invalid date format. Please use YYYY-MM-DD[/red]",
        "cn": "[red]错误: 日期格式无效，请使用 YYYY-MM-DD 格式[/red]",
    },

    # ========== Save report section names ==========
    "report_section_analysts": {
        "en": "I. Analyst Team Reports",
        "cn": "一、分析师团队报告",
    },
    "report_section_research": {
        "en": "II. Research Team Decision",
        "cn": "二、研究团队决策",
    },
    "report_section_trading": {
        "en": "III. Trading Team Plan",
        "cn": "三、交易团队计划",
    },
    "report_section_risk": {
        "en": "IV. Risk Management Team Decision",
        "cn": "四、风险管理团队决策",
    },
    "report_section_portfolio": {
        "en": "V. Portfolio Manager Decision",
        "cn": "五、投资组合经理决策",
    },

    # ========== Announcements ==========
    "announcements": {
        "en": "Announcements",
        "cn": "公告",
    },
}

# Maps internal agent names to i18n keys
AGENT_NAME_I18N_MAP = {
    "Market Analyst": "agent_market_analyst",
    "Social Analyst": "agent_social_analyst",
    "News Analyst": "agent_news_analyst",
    "Fundamentals Analyst": "agent_fundamentals_analyst",
    "Bull Researcher": "agent_bull_researcher",
    "Bear Researcher": "agent_bear_researcher",
    "Research Manager": "agent_research_manager",
    "Trader": "agent_trader",
    "Aggressive Analyst": "agent_aggressive_analyst",
    "Neutral Analyst": "agent_neutral_analyst",
    "Conservative Analyst": "agent_conservative_analyst",
    "Portfolio Manager": "agent_portfolio_manager",
}

# Maps internal team names to i18n keys
TEAM_NAME_I18N_MAP = {
    "Analyst Team": "team_analyst",
    "Research Team": "team_research",
    "Trading Team": "team_trading",
    "Risk Management": "team_risk",
    "Portfolio Management": "team_portfolio",
}


def get_text(key: str, lang: str = "en") -> str:
    """Get translated text by key and language.

    Args:
        key: Translation key
        lang: Language code ("en" or "cn")

    Returns:
        Translated string, falls back to English if translation not found.
    """
    entry = TRANSLATIONS.get(key)
    if entry is None:
        return key  # Return the key itself as fallback
    return entry.get(lang, entry.get("en", key))


def get_agent_name(internal_name: str, lang: str = "en") -> str:
    """Get the localized display name for an agent.

    Args:
        internal_name: The internal English agent name (e.g., "Market Analyst")
        lang: Language code

    Returns:
        Localized agent name, falls back to internal_name.
    """
    i18n_key = AGENT_NAME_I18N_MAP.get(internal_name)
    if i18n_key is None:
        return internal_name
    return get_text(i18n_key, lang)


def get_team_name(internal_name: str, lang: str = "en") -> str:
    """Get the localized display name for a team.

    Args:
        internal_name: The internal English team name (e.g., "Research Team")
        lang: Language code

    Returns:
        Localized team name, falls back to internal_name.
    """
    i18n_key = TEAM_NAME_I18N_MAP.get(internal_name)
    if i18n_key is None:
        return internal_name
    return get_text(i18n_key, lang)


def get_agent_language_instruction(lang: str = "en") -> str:
    """Get the language instruction to append to agent prompts.

    When lang is "cn", returns an instruction telling the LLM to respond in Chinese.
    When lang is "en", returns an empty string (no change needed).

    Args:
        lang: Language code ("en" or "cn")

    Returns:
        Language instruction string to append to prompts.
    """
    if lang == "cn":
        return (
            "\n\nIMPORTANT: You MUST write your entire response and report in "
            "Simplified Chinese (简体中文). All analysis, conclusions, tables, "
            "and recommendations must be in Chinese. Use professional financial "
            "terminology in Chinese."
        )
    return ""
