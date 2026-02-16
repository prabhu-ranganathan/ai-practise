from google.adk.agents import Agent
from google.adk.apps import App
from dotenv import load_dotenv
from .doc_tool import DocumentIntelligence
import os
load_dotenv()

# We wrap the tool methods so the Agent understands their purpose
doc_intel = DocumentIntelligence()


def list_available_docs() -> list[str]:
    """Lists files in the 'document' directory."""
    doc_dir = os.path.join(os.path.dirname(__file__), "document")
    return [f for f in os.listdir(doc_dir) if f.endswith((".pdf", ".docx"))]


root_agent = Agent(
    name="research_assistant",
    model="gemini-2.5-flash",
    tools=[
        list_available_docs,
        doc_intel.load_and_index,
        doc_intel.query_memory
    ],
    instruction=(
        "You are a Research Assistant. Follow this workflow:\n"
        "1. Use 'list_available_docs' to see what files exist.\n"
        "2. If a user asks about a file, use 'load_and_index' to pull it into memory.\n"
        "3. Once loaded, use 'query_memory' to find answers within that document.\n"
        "Stay concise and only answer based on the document context."
    )
)

app = App(name="research_assistant", root_agent=root_agent)
