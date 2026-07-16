from app.ai.embeddings import embedding_generator
from app.ai.llm import llm
from app.ai.vector_store import vector_store


class ChatService:

    def ask(
        self,
        question: str,
    ):

        vector_store.load()

        query_embedding = embedding_generator.embed(
            [question]
        )[0]

        chunks = vector_store.search(
            query_embedding,
            k=5,
        )

        if not chunks:
            return {
                "answer": "No documents have been uploaded yet."
            }

        context = "\n\n".join(chunks)

        answer = llm.ask(
            context=context,
            question=question,
        )

        return {
            "question": question,
            "answer": answer,
            
        }


chat_service = ChatService()