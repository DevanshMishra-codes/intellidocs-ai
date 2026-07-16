import shutil
import uuid
from pathlib import Path

from fastapi import HTTPException, UploadFile, status
from sqlalchemy.orm import Session

from app.models.document import Document
from app.models.user import User
from app.repositories.document_repository import document_repository

from app.ai.parser import pdf_parser
from app.ai.chunking import text_chunker
from app.ai.embeddings import embedding_generator
from app.ai.vector_store import vector_store

DOCUMENT_UPLOAD_DIR = Path("uploads/documents")
DOCUMENT_UPLOAD_DIR.mkdir(
    parents=True,
    exist_ok=True,
)


class DocumentService:

    def upload_document(
        self,
        db: Session,
        file: UploadFile,
        current_user: User,
    ):

        if not file.filename.lower().endswith(".pdf"):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Only PDF files are supported",
            )

        unique_filename = f"{uuid.uuid4()}.pdf"

        file_path = DOCUMENT_UPLOAD_DIR / unique_filename

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # -----------------------------
        # AI Processing Pipeline
        # -----------------------------

        text = pdf_parser.extract_text(str(file_path))

        chunks = text_chunker.chunk_text(text)

        embeddings = embedding_generator.embed(chunks)

        vector_store.load()

        vector_store.add(
            embeddings,
            chunks,
        )

        vector_store.save()

        # -----------------------------
        # Save metadata
        # -----------------------------

        document = Document(
            filename=file.filename,
            file_path=str(file_path),
            extracted_text=text,
            owner_id=current_user.id,
        )

        return document_repository.create(
            db,
            document,
        )

    def list_documents(
        self,
        db: Session,
        current_user: User,
    ):
        return document_repository.get_all(
            db,
            current_user.id,
        )

    def delete_document(
        self,
        db: Session,
        document_id,
        current_user: User,
    ):

        document = document_repository.get(
            db,
            document_id,
            current_user.id,
        )

        if document is None:
            raise HTTPException(
                status_code=404,
                detail="Document not found",
            )

        path = Path(document.file_path)

        if path.exists():
            path.unlink()

        document_repository.delete(
            db,
            document,
        )


document_service = DocumentService()