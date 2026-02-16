# Research Assistant Agent

A lightweight AI-powered Research Assistant built using Google's **Agent Development Kit (ADK)** and **Gemini 2.5 Flash**. This agent can list, index, and query local documents (PDF and DOCX) to help you find information efficiently.

## Features

- **Document Discovery**: Automatically detects PDF and DOCX files in the local `document/` directory.
- **Dynamic Indexing**: Loads documents into memory and chunks them for searching on demand.
- **Context-Aware Querying**: Uses a simple keyword-based RAG (Retrieval-Augmented Generation) system to provide relevant context to the Gemini model for answering questions.
- **Agentic Workflow**: Follows a predefined workflow: List -> Index -> Query.

## Prerequisites

- Python 3.9+
- A Google AI Studio API Key (for Gemini 2.5 Flash)

## Setup

1. **Clone or Download** this repository.
2. **Install Dependencies**:
   ```bash
   pip install google-adk pypdf python-docx python-dotenv
   ```
3. **Configure Environment Variables**:
   Create a `.env` file in the root directory (one should already be provided) and add your Google API Key:
   ```env
   GOOGLE_API_KEY="your_api_key_here"
   ```

## Usage

1. **Prepare Documents**: Place the PDF or DOCX files you want to research in the `document/` directory.
2. **Run the Agent**:
   ```bash
   python agent.py
   ```
3. **Interact**: The agent will follow its instructions. You can ask:
   - "What documents are available?"
   - "Tell me about [filename].pdf"
   - "Based on the document, what is the main topic?"

## Project Structure

```text
research_assistant/
├── agent.py          # Main entry point and Agent configuration
├── doc_tool.py       # Document Intelligence tool (loading, chunking, querying)
├── document/         # Folder for local PDF/DOCX files
├── .env              # Environment variables
└── .adk/             # ADK specific configurations
```

## How it Works

1. **Agent Definition**: `agent.py` defines the Gemini-powered agent and its available tools.
2. **Document Intelligence**: `doc_tool.py` contains the `DocumentIntelligence` class which handles:
   - Text extraction from PDFs and Word documents.
   - Text chunking with overlap for better context preservation.
   - Simple keyword-based retrieval to search chunks.
3. **Workflow**: The agent is instructed to first list files, then load a specific file into memory when asked, and finally query that memory to answer questions.
