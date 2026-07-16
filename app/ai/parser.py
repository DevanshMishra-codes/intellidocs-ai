import fitz  # PyMuPDF
from pathlib import Path


class PDFParser:
    """
    Handles PDF text extraction.
    """

    @staticmethod
    def extract_text(file_path: str) -> str:
        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(f"{file_path} not found.")

        text = ""

        document = fitz.open(file_path)

        try:
            for page in document:
                text += page.get_text()
        finally:
            document.close()

        return text.strip()


pdf_parser = PDFParser()