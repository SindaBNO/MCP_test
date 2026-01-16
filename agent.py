import os

from dotenv import load_dotenv
from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from mcp import StdioServerParameters

# Charge les variables d'environnement depuis .env
load_dotenv()

AZURE_API_KEY = os.getenv("AZURE_API_KEY")
AZURE_API_BASE = os.getenv("AZURE_API_BASE")
AZURE_API_VERSION = os.getenv("AZURE_API_VERSION")
AZURE_DEPLOYMENT = os.getenv("AZURE_DEPLOYMENT")

missing = [
    name
    for name, value in [
        ("AZURE_API_KEY", AZURE_API_KEY),
        ("AZURE_API_BASE", AZURE_API_BASE),
        ("AZURE_API_VERSION", AZURE_API_VERSION),
        ("AZURE_DEPLOYMENT", AZURE_DEPLOYMENT),
    ]
    if not value
]

if missing:
    raise RuntimeError(
        f"⚠️ Variables manquantes dans .env : {', '.join(missing)}. "
        "Merci de les définir avant de lancer `adk web`."
    )

# Modèle Azure via LiteLlm
# LiteLlm utilisera les variables d'environnement AZURE_API_KEY,
# AZURE_API_BASE et AZURE_API_VERSION déjà définies ci-dessus.
model = LiteLlm(
    model=f"azure/{AZURE_DEPLOYMENT}"
)
# MCPToolset vers le serveur Azure MCP (utilise ta session az login)
azure_mcp_tool = MCPToolset(
    connection_params=StdioConnectionParams(
        server_params=StdioServerParameters(
            command="npx",
            args=["-y", "@azure/mcp@latest", "server", "start"],
            env=os.environ.copy(),
        ),
    ),
)

# Agent racine pour ADK Web
root_agent = LlmAgent(
    model=model,
    name="azure_mcp_agent_gpt4_1",
    instruction=(
        "Tu es un assistant cloud architect spécialisé sur Azure. "
        "Utilise les outils du serveur MCP Azure pour lister les ressources, "
        "concevoir des architectures, générer du Bicep et expliquer clairement chaque étape. "
        "Respecte les conventions de nommage fournies par l'utilisateur "
        "et privilégie les architectures serverless et sécurisées."
    ),
    tools=[azure_mcp_tool],
)
