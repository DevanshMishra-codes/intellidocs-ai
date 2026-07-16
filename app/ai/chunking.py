from typing import List


class TextChunker:
    """
    Splits text into smaller chunks.
    """

    @staticmethod
    def chunk_text(
        text: str,
        chunk_size: int = 200,
        overlap: int = 40,
    ) -> List[str]:

        words = text.split()

        chunks = []

        start = 0

        while start < len(words):

            end = start + chunk_size

            chunk = " ".join(words[start:end])

            chunks.append(chunk)

            start += chunk_size - overlap

        return chunks


text_chunker = TextChunker()