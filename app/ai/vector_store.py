import faiss
import numpy as np
import pickle
from pathlib import Path

VECTOR_DIR = Path("uploads/vectors")

VECTOR_DIR.mkdir(
    parents=True,
    exist_ok=True,
)

INDEX_PATH = VECTOR_DIR / "faiss.index"

CHUNKS_PATH = VECTOR_DIR / "chunks.pkl"


class VectorStore:

    def __init__(self):

        self.dimension = 384

        self.index = faiss.IndexFlatL2(
            self.dimension
        )

        self.chunks = []

    def add(
        self,
        embeddings,
        chunks,
    ):

        self.index.add(
            np.array(
                embeddings,
                dtype="float32",
            )
        )

        self.chunks.extend(chunks)

    def search(
        self,
        embedding,
        k=5,
    ):

        if self.index.ntotal == 0:
            return []

        k = min(k, self.index.ntotal)

        distances, indices = self.index.search(
            np.array([embedding], dtype="float32"),
            k,
        )

        seen = set()
        results = []

        for idx in indices[0]:
            if idx < len(self.chunks):
                chunk = self.chunks[idx]

                if chunk not in seen:
                    seen.add(chunk)
                    results.append(chunk)

        return results

    def save(self):

        Path("uploads").mkdir(
            exist_ok=True
        )

        faiss.write_index(
            self.index,
            str(INDEX_PATH),
        )

        with open(
            CHUNKS_PATH,
            "wb",
        ) as f:

            pickle.dump(
                self.chunks,
                f,
            )

    def load(self):

        index = INDEX_PATH

        chunks = CHUNKS_PATH

        if index.exists():

            self.index = faiss.read_index(
                str(index)
            )

        if chunks.exists():

            with open(
                chunks,
                "rb",
            ) as f:

                self.chunks = pickle.load(f)


vector_store = VectorStore()