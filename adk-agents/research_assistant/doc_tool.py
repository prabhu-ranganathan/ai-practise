import os
from pypdf import PdfReader
from docx import Document


class DocumentIntelligence:
    def __init__(self, chunk_size=1000, overlap=200):
        self.chunk_size = chunk_size
        self.overlap = overlap
        self.chunks = []
        self.current_file = None

    def load_and_index(self, filename: str) -> str:
        """Loads a document into memory and breaks it into searchable chunks."""
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_dir, "document", filename)

        if not os.path.exists(file_path):
            return f"Error: File {filename} not found."

        full_text = ""
        if filename.lower().endswith(".pdf"):
            reader = PdfReader(file_path)
            full_text = " ".join(
                [p.extract_text() or "" for p in reader.pages])
        elif filename.lower().endswith(".docx"):
            doc = Document(file_path)
            full_text = " ".join([p.text for p in doc.paragraphs])

        # Create overlapping chunks
        self.chunks = [
            full_text[i: i + self.chunk_size].replace('\n', ' ')
            for i in range(0, len(full_text), self.chunk_size - self.overlap)
        ]
        self.current_file = filename
        return f"Document '{filename}' is now indexed and ready for questions."

    def query_memory(self, question: str) -> str:
        """Searches the currently loaded document for an answer."""
        if not self.chunks:
            return "No document is currently loaded in memory. Please load one first."

        # Simple keyword-based relevance scoring
        query_words = set(question.lower().split())
        scored = []
        for chunk in self.chunks:
            score = sum(1 for word in query_words if word in chunk.lower())
            if score > 0:
                scored.append((score, chunk))

        scored.sort(key=lambda x: x[0], reverse=True)
        context = "\n\n---\n\n".join([c[1] for c in scored[:3]])
        return f"Context from {self.current_file}:\n\n{context}" if context else "No relevant info found."
