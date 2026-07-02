from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    Date,
    DateTime,
)

from sqlalchemy.orm import declarative_base

from datetime import datetime


Base = declarative_base()


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True)

    # ---------------------------
    # Личные данные
    # ---------------------------

    last_name = Column(String, default="")
    first_name = Column(String, default="")
    middle_name = Column(String, default="")

    gender = Column(String, default="")

    birth_date = Column(Date, nullable=True)

    phone = Column(String, default="")

    email = Column(String, default="")

    address = Column(String, default="")

    photo = Column(String, default="")

    # ---------------------------
    # Работа
    # ---------------------------

    department = Column(String, default="")

    position = Column(String, default="")

    hire_date = Column(Date, nullable=True)

    hire_order_number = Column(String, default="")

    hire_order_date = Column(Date, nullable=True)

    # ---------------------------
    # Воинский учет
    # ---------------------------

    military_status = Column(String, default="")

    # ---------------------------
    # Медицинская книжка
    # ---------------------------

    medical_book_status = Column(String, default="")

    # ---------------------------
    # Семья
    # ---------------------------

    marital_status = Column(String, default="")

    has_children = Column(Boolean, default=False)

    children_count = Column(Integer, default=0)

    # ---------------------------
    # Статус
    # ---------------------------

    employment_status = Column(String, default="Работает")

    dismissal_date = Column(Date, nullable=True)

    dismissal_order_number = Column(String, default="")

    dismissal_order_date = Column(Date, nullable=True)

    # ---------------------------
    # Дополнительно
    # ---------------------------

    notes = Column(String, default="")

    # ---------------------------
    # Служебная информация
    # ---------------------------

    created_at = Column(DateTime, default=datetime.now)

    updated_at = Column(
        DateTime,
        default=datetime.now,
        onupdate=datetime.now,
    )


class Department(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True)

    name = Column(String, unique=True, nullable=False)


class Position(Base):
    __tablename__ = "positions"

    id = Column(Integer, primary_key=True)

    name = Column(String, unique=True, nullable=False)