from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.core.security import hash_password
from app.models.user import User
from app.repositories.user_repository import user_repository
from app.schemas.user import UserCreate
from app.core.security import (
    verify_password,
    create_access_token,
)


class UserService:

    def create_user(
        self,
        db: Session,
        user_data: UserCreate
    ) -> User:

        if user_repository.get_by_email(db, user_data.email):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered",
            )

        if user_repository.get_by_username(db, user_data.username):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Username already taken",
            )

        user = User(
            username=user_data.username,
            email=user_data.email,
            hashed_password=hash_password(user_data.password),
        )

        return user_repository.create(db, user)

    def login_user(
        self,
        db: Session,
        email: str,
        password: str,
    ):

        user = user_repository.get_by_email(db, email)

        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid credentials",
            )

        if not verify_password(
            password,
            user.hashed_password,
        ):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid credentials",
            )

        access_token = create_access_token(
            {
                "sub": str(user.id)
            }
        )

        return access_token


user_service = UserService()