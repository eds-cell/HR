from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base, Employee

DATABASE_URL = "sqlite:///database/employees.db"

engine = create_engine(DATABASE_URL, echo=False)

Session = sessionmaker(bind=engine)


def create_database():
    Base.metadata.create_all(engine)


def get_session():
    return Session()


def add_employee(data: dict):
    session = Session()

    employee = Employee(
        last_name=data.get("last_name", ""),
        first_name=data.get("first_name", ""),
        middle_name=data.get("middle_name", ""),
        gender=data.get("gender", ""),
        department=data.get("department", ""),
        position=data.get("position", ""),
        phone=data.get("phone", ""),
        email=data.get("email", "")
    )

    session.add(employee)
    session.commit()
    session.refresh(employee)
    session.close()

    return employee


def get_employees():
    session = Session()

    employees = (
        session.query(Employee)
        .order_by(Employee.last_name, Employee.first_name)
        .all()
    )

    session.close()

    return employees


def get_employee(employee_id):
    session = Session()

    employee = (
        session.query(Employee)
        .filter(Employee.id == employee_id)
        .first()
    )

    session.close()

    return employee


def delete_employee(employee_id):
    session = Session()

    employee = (
        session.query(Employee)
        .filter(Employee.id == employee_id)
        .first()
    )

    if employee:
        session.delete(employee)
        session.commit()

    session.close()


def update_employee(employee_id, data):
    session = Session()

    employee = (
        session.query(Employee)
        .filter(Employee.id == employee_id)
        .first()
    )

    if employee is None:
        session.close()
        return False

    employee.last_name = data.get("last_name", employee.last_name)
    employee.first_name = data.get("first_name", employee.first_name)
    employee.middle_name = data.get("middle_name", employee.middle_name)
    employee.gender = data.get("gender", employee.gender)
    employee.department = data.get("department", employee.department)
    employee.position = data.get("position", employee.position)
    employee.phone = data.get("phone", employee.phone)
    employee.email = data.get("email", employee.email)

    session.commit()
    session.close()

    return True