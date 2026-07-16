import ollama


class LLM:

    MODEL = "qwen2.5:3b"

    def ask(
        self,
        context: str,
        question: str,
    ) -> str:

        prompt = f"""
You are IntelliDocs AI.

Answer ONLY using the provided context.

If the answer is not available in the context, reply exactly:

"I couldn't find that information in the uploaded documents."

-------------------------
Context
-------------------------

{context}

-------------------------
Question
-------------------------

{question}
"""

        response = ollama.chat(
            model=self.MODEL,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        return response["message"]["content"]


llm = LLM()