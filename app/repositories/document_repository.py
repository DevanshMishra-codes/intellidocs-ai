from uuid import UUID

from sqlalchemy.orm import Session

from app.models.document import Document


class DocumentRepository:

    def create(
        self,
        db: Session,
        document: Document,
    ):
        db.add(document)
        db.commit()
        db.refresh(document)
        return document

    def get_all(
        self,
        db: Session,
        owner_id: UUID,
    ):
        return (
            db.query(Document)
            .filter(Document.owner_id == owner_id)
            .order_by(Document.created_at.desc())
            .all()
        )

    def get(
        self,
        db: Session,
        document_id: UUID,
        owner_id: UUID,
    ):
        return (
            db.query(Document)
            .filter(
                Document.id == document_id,
                Document.owner_id == owner_id,
            )
            .first()
        )

    def delete(
        self,
        db: Session,
        document: Document,
    ):
        db.delete(document)
        db.commit()


document_repository = DocumentRepository()