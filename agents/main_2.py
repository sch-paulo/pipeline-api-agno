from agno.agent import Agent
from agno.models.anthropic import Claude
from agno.tools.postgres import PostgresTools
import os
from dotenv import load_dotenv

load_dotenv()

ANTHROPIC_KEY = os.getenv('ANTHROPIC_KEY')

# Initialize PostgresTools with connection details
postgres_tools = PostgresTools(
    host="",
    port=5432,
    db_name="",
    user="",
    password="",
    table_schema="public",
)

# Create an agent with the PostgresTools
agent = Agent(tools=[postgres_tools],
              model=Claude(id="claude-3-7-sonnet-latest", api_key=ANTHROPIC_KEY))

agent.print_response("Fale todas as tabelas do banco de dados", markdown=True)

agent.print_response("""
Faça uma query para pegar todas as cotações de bitcoin na tabela bitcoin_dados
""")

agent.print_response("""
Faça uma análise super complexa sobre o bitcoin usando os dados da tabela bitcoin_dados
""")