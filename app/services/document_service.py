import shutil
import uuid
from pathlib import Path

from fastapi import HTTPException, UploadFile, status
from sqlalchemy.orm import Session

from app.models.document import Document
from app.models.user import User
from app.repositories.document_repository import document_repository

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)


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

        file_path = UPLOAD_DIR / unique_filename

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        document = Document(
            filename=file.filename,
            file_path=str(file_path),
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