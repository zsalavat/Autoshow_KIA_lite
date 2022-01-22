from sqlalchemy import Column, ForeignKey, Integer, String, Text ,DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

"""
Модуль с описанием ORM-моделей базы данных
"""

from labapp import db

class Login(db.Model):
    __tablename__ = 'login'
    id = Column(Integer, primary_key=True)
    username = Column(String(255), nullable=False, unique=True)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False, unique=True)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)

class ContactRequest(db.Model):
    __tablename__ = 'contactrequest'
    id = Column(Integer, primary_key=True)
    firstname = Column(String(255), nullable=False)
    lastname = Column(String(255))
    patronymic = Column(String(255))
    email = Column(String(255))
    phone = Column(String(255))
    city = Column(String(255))
    options = Column(String(255))
    price = Column(Integer)
    employee=Column(String(255))
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)

class Сars(db.Model):
    __tablename__ = 'cars'
    id = Column(Integer, primary_key=True)
    caption = Column(String(255), nullable=False)
    complectation = Column(String(255), nullable=False)
    color = Column(String(255), nullable=False)
    price = Column(Integer)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)

class Сlients(db.Model):
    __tablename__ = 'clients'
    id = Column(Integer, primary_key=True)
    firstname = Column(String(255), nullable=False)
    lastname = Column(String(255))
    patronymic= Column(String(255))
    email = Column(String(255))
    phone = Column(String(255))
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
