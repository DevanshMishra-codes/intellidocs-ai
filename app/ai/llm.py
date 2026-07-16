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

        Your task is to answer ONLY from the supplied context.

        Rules:

        1. Never make up information.
        2. If the answer is not present, reply:

        "I couldn't find that information in the uploaded documents."

        3. Keep answers concise and professional.
        4. If asked for a summary, summarize the context.

        ====================

        Context:

        {context}

        ====================

        Question:

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