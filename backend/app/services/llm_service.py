from ollama import Client
from app.core.settings import settings

class LLMService:
    """
    Handles communication with the local Ollama model.
    """

    def __init__(self):
        self.client = Client(
            host=settings.ollama_host
        )

        self.model = settings.ollama_model

    def generate(
        self,
        question: str,
        context: str,
    ) -> str:

        prompt = f"""
You are VidyAI, an academic AI assistant.

Answer ONLY using the context below.

If the answer cannot be found in the context, reply:

"I couldn't find that information in the uploaded document."

-------------------------
Context:
{context}
-------------------------

Question:
{question}

Answer:
"""

        response = self.client.chat(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        return response["message"]["content"]