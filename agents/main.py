from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.anthropic import Claude
from agno.tools.duckduckgo import DuckDuckGoTools
import os

load_dotenv()

ANTHROPIC_KEY = os.getenv('ANTHROPIC_KEY')

agent = Agent(
    model=Claude(id="claude-3-7-sonnet-latest", api_key=ANTHROPIC_KEY),
    description="You're the best of the best in cryptocurrencies in the world.",
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True
)
agent.print_response(
    "Faça uma análise completxa do Bitcoin",
    stream=True
)