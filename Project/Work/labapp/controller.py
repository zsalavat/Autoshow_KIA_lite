import os
from labapp import db
from .models import *
from .utils import row_to_dict
from config import basedir, syncDB, resetDB
from flask import session, make_response, redirect, url_for, jsonify
import bcrypt

"""
В данном модуле реализуются CRUD-методы для работы с БД
"""

# Получаем список всех запросов.
def get_contact_req_all():
    # объявляем пустой список
    result = []
    # Получаем итерируемый объект, где содержатся все строки таблицы запросов с сортировкой по id
    rows = db.session.query(ContactRequest).order_by(ContactRequest.id)
    # конвертируем каждую строку в dict и добавляем в список result
    for row in rows:
        result.append(row_to_dict(row))
    # возвращаем dict формата { 'contactrequests': result }, где result - это список с dict-объектов с информацией
    return {'contactrequests': result}

# Получаем запрос по id (конструкция .filter(...) эквивалентна условию WHERE в SQL
def get_contact_req_by_id(id):
    result = db.session.query(ContactRequest).filter(ContactRequest.id == int(id)).first()
    return row_to_dict(result)

# Получаем все запросы по имени автора
def get_contact_req_by_author(firstname):
    result = []
    rows = db.session.query(ContactRequest).filter(ContactRequest.firstname == firstname)
    for row in rows:
        result.append(row_to_dict(row))
    return {'contactrequests': result}

# Создать новый запрос
def create_contact_req(json_data):
    try:
        # Формируем объект ContactRequest по данным из json_data
        contactreq = ContactRequest(
            firstname=json_data['firstname'],
            lastname=json_data['lastname'],
            patronymic=json_data['patronymic'],
            email=json_data['email'],
            phone=json_data['phone'],
            city=json_data['city'],
            options=json_data['options'],
            price=json_data['price'],
            employee=json_data['employee'])
        # INSERT запрос в БД
        db.session.add(contactreq)
        # Подтверждение изменений в БД
        db.session.commit()
        # Возвращаем результат
        return { 'message': "ContactRequest Created!" }
        # если возникла ошибка запроса в БД
    except Exception as e:
        # откатываем изменения в БД
        db.session.rollback()
        # возвращаем dict с ключом 'error' и тектом ошибки
        return {'message': str(e)}

# Удалить запрос по id в таблице
def delete_contact_req_by_id(id):
    try:
        # DELETE запрос в БД
        db.session.query(ContactRequest).filter(ContactRequest.id == int(id)).delete()
        db.session.commit()
        return { 'message': "ContactRequest Deleted!" }
    except Exception as e:
        db.session.rollback()
        return {'message': str(e)}

# Обновить текст запроса по id в таблице
def update_contact_req_by_id(id, json_data):
    try:
        # UPDATE запрос в БД
        # ORM обновит те поля в contactrequest, которые будут указаны в json_data
        db.session.query(ContactRequest).filter(ContactRequest.id == id).update(json_data)
        db.session.commit()
        return { 'message': "ContactRequest Updated!" }
    except Exception as e:
        db.session.rollback()
        return {'message': str(e)}

# Авторизация пользователя
def login_user(form_data):
    # Получаем логин и пароль из данных формы
    username = form_data.get('loginField')
    password = form_data.get('passField').encode('utf-8')
    # Ищем пользователя в БД
    result = db.session.query(Login).filter(Login.username == username).first()
    user = row_to_dict(result)
    # если пользователь не найден переадресуем на страницу /login
    if user is None:
        return redirect(url_for('login'))
    # если пароль не прошел проверку, переадресуем на страницу /login
    elif not bcrypt.checkpw(password, user['password']):
        return redirect(url_for('login'))
    # иначе регистрируем сессию пользователя (записываем логин пользователя в параметр user) и высылаем cookie "AuthToken"
    else:
        response = redirect('/')
        session['user'] = user['username']
        response.set_cookie('AuthToken', user['username'])
        return response

# Зарегистрировать пользовательский аккаунт
def register_user(form_data):
    # Получаем пароль из формы
    password = form_data.get('passField').encode('utf-8')
    # Создаем хеш пароля с солью
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password, salt)
    try:
        # Формируем объект Login для записи в БД
        user = Login(
            username=form_data.get('loginField'),
            password=hashed,
            email=form_data.get('emailField'))
        # INSERT запрос в БД
        db.session.add(user)
        # Подтверждение изменений в БД
        db.session.commit()
        # Переадресуем на страницу авторизации
        return redirect(url_for('login'))
        # если возникла ошибка запроса в БД
    except Exception as e:
        # откатываем изменения в БД
        db.session.rollback()
        # возвращаем response с ошибкой сервера
        return make_response(jsonify({'message': str(e)}), 500)

# Если параметр syncDB выставлен в True, то при запуске приложения
# автоматически создаем таблицы в БД
if syncDB == True:
    db.create_all()

# Если параметр resetDB выставлен в True, то при запуске приложения
# удаляем ВСЕ таблицы в БД и создаем чистых таблицы по заданным моделям
if resetDB == True:
    db.delete_all()
    db.create_all()
#ЗДЕСЬ НАЧНУТСЯ МАШИНЫ
# Получаем список всех запросов.
def get_car_req_all():
    # объявляем пустой список
    result = []
    # Получаем итерируемый объект, где содержатся все строки таблицы запросов с сортировкой по id
    rows = db.session.query(Сars).order_by(Сars.id)
    # конвертируем каждую строку в dict и добавляем в список result
    for row in rows:
        result.append(row_to_dict(row))
    # возвращаем dict формата { 'cars': result }, где result - это список с dict-объектов с информацией
    return {'cars': result}

# Получаем запрос по id (конструкция .filter(...) эквивалентна условию WHERE в SQL
def get_car_req_by_id(id):
    result = db.session.query(Сars).filter(Сars.id == int(id)).first()
    return row_to_dict(result)

# Получаем все запросы по названию модели
def get_car_req_by_caption(caption):
    result = []
    rows = db.session.query(Сars).filter(Сars.caption == caption)
    for row in rows:
        result.append(row_to_dict(row))
    return {'cars': result}

# Создать новый запрос
def create_car_req(json_data):
    try:
        # Формируем объект ContactRequest по данным из json_data
        carReq =Сars(
            caption=json_data['caption'],
            complectation=json_data['complectation'],
            color=json_data['color'],
            price=json_data['price'])
        # INSERT запрос в БД
        db.session.add(carReq)
        # Подтверждение изменений в БД
        db.session.commit()
        # Возвращаем результат
        return {'message': "CarRequest Created!"}
        # если возникла ошибка запроса в БД
    except Exception as e:
        # откатываем изменения в БД
        db.session.rollback()
        # возвращаем dict с ключом 'error' и текcтом ошибки
        return {'message': str(e)}

# Удалить запрос по id в таблице
def delete_car_req_by_id(id):
    try:
        # DELETE запрос в БД
        db.session.query(Сars).filter(Сars.id == int(id)).delete()
        db.session.commit()
        return { 'message': "Car Deleted!" }
    except Exception as e:
        db.session.rollback()
        return {'message': str(e)}

# Обновить текст запроса по id в таблице
def update_car_req_by_id(id, json_data):
    try:
        # UPDATE запрос в БД
        # ORM обновит те поля в contactrequest, которые будут указаны в json_data
        db.session.query(Сars).filter(Сars.id == id).update(json_data)
        db.session.commit()
        return { 'message': "Car Updated!" }
    except Exception as e:
        db.session.rollback()
        return {'message': str(e)}
#ЗДЕСЬ НАЧНУТСЯ КЛИЕНТЫ
# Получаем список всех запросов.
def get_client_req_all():
    # объявляем пустой список
    result = []
    # Получаем итерируемый объект, где содержатся все строки таблицы запросов с сортировкой по id
    rows = db.session.query(Сlients).order_by(Сlients.id)
    # конвертируем каждую строку в dict и добавляем в список result
    for row in rows:
        result.append(row_to_dict(row))
    # возвращаем dict формата { 'clients': result }, где result - это список с dict-объектов с информацией
    return {'clients': result}

# Получаем запрос по id (конструкция .filter(...) эквивалентна условию WHERE в SQL
def get_client_req_by_id(id):
    result = db.session.query(Сlients).filter(Сlients.id == int(id)).first()
    return row_to_dict(result)

# Получаем все запросы по названию модели
def get_client_req_by_firstname(firstname):
    result = []
    rows = db.session.query(Сlients).filter(Сlients.firstname == firstname)
    for row in rows:
        result.append(row_to_dict(row))
    return {'cars': result}

# Создать новый запрос
def create_client_req(json_data):
    try:
        # Формируем объект ContactRequest по данным из json_data
        clientReq =Сlients(
            firstname=json_data['firstname'],
            lastname=json_data['lastname'],
            patronymic=json_data['patronymic'],
            email=json_data['email'],
            phone=json_data['phone'])
        # INSERT запрос в БД
        db.session.add(clientReq)
        # Подтверждение изменений в БД
        db.session.commit()
        # Возвращаем результат
        return {'message': "ClientRequest Created!"}
        # если возникла ошибка запроса в БД
    except Exception as e:
        # откатываем изменения в БД
        db.session.rollback()
        # возвращаем dict с ключом 'error' и текcтом ошибки
        return {'message': str(e)}

# Удалить запрос по id в таблице
def delete_client_req_by_id(id):
    try:
        # DELETE запрос в БД
        db.session.query(Сlients).filter(Сlients.id == int(id)).delete()
        db.session.commit()
        return { 'message': "Car Deleted!" }
    except Exception as e:
        db.session.rollback()
        return {'message': str(e)}

# Обновить текст запроса по id в таблице
def update_client_req_by_id(id, json_data):
    try:
        # UPDATE запрос в БД
        # ORM обновит те поля в contactrequest, которые будут указаны в json_data
        db.session.query(Сlients).filter(Сlients.id == id).update(json_data)
        db.session.commit()
        return { 'message': "Сlients Updated!" }
    except Exception as e:
        db.session.rollback()
        return {'message': str(e)}




















