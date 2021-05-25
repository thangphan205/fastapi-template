from sqlalchemy.orm import Session
from fastapi import FastAPI
from passlib.context import CryptContext
from fastapi.encoders import jsonable_encoder
from datetime import datetime
from models import models
from schemas.users import User, UserCreate, UserUpdate, UserUpdatePassword
import requests, json
from settings import settings

from loguru import logger

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_user_by_id(db: Session, id: int):
    return db.query(models.User).filter(models.User.id == id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


# def get_users(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.User).offset(skip).limit(limit).all()


def get_users(
    db: Session,
    skip: int = 0,
    limit: int = 100,
    username: str = "",
    full_username: str = "",
    department: str = "",
):

    return (
        db.query(models.User)
        .filter(models.User.username.ilike("%{}%".format(username)))
        .filter(models.User.full_username.ilike("%{}%".format(full_username)))
        .filter(models.User.department.ilike("%{}%".format(department)))
        .all()
    )


def create_user(db: Session, user: models.User):
    hashed_password = get_password_hash(user.password)
    DATETIME_NOW = datetime.now()
    db_user = models.User(
        username=user.username,
        full_username=user.full_username,
        email=user.email,
        hashed_password=hashed_password,
        role=user.role,
        is_active=user.is_active,
        created_date=DATETIME_NOW,
        login_fail=user.login_fail,
        department=user.department,
        last_login=DATETIME_NOW,
        description=user.description,
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return True


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def get_user_by_id(db: Session, id: int):
    return db.query(models.User).filter(models.User.id == id).first()


def get_user(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


def update_user_login_fail(db: Session, db_user: models.User):
    db_user.login_fail += 1
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return True


def update_user(
    db: Session,
    db_user: models.User,
    user_update: UserUpdate,
    current_user: User,
):
    obj_data = jsonable_encoder(db_user)
    update_data = user_update.dict(exclude_unset=True)
    for field in obj_data:
        if field in update_data:
            setattr(db_user, field, update_data[field])
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def update_user_password(
    db: Session,
    db_user: models.User,
    user_update: UserUpdatePassword,
    current_user: User,
):
    obj_data = jsonable_encoder(db_user)
    update_data = user_update.dict(exclude_unset=True)
    db_user.hashed_password = get_password_hash(update_data["password"])
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return False
