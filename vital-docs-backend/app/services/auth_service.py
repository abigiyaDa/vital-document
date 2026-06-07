from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.repositories.officer_repo import OfficerRepository
from app.core.security import verify_password, create_access_token

class AuthService:
    def __init__(self, db: Session):
        self.repo = OfficerRepository(db)

    def login(self, username: str, password: str) -> dict:
        officer = self.repo.get_by_username(username)
        if not officer or not verify_password(password, officer.password_hash):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid username or password",
            )
        token = create_access_token({"sub": str(officer.officer_id)})
        return {"access_token": token, "token_type": "bearer"}