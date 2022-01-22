# -*- coding: utf-8 -*-
# Подключаем объект приложения Flask из __init__.py
from labapp import app
# Подключаем библиотеку для "рендеринга" html-шаблонов из папки templates
from flask import render_template, make_response, request, Response, session, redirect, url_for, jsonify, json
# Подключаем контроллер
from . import controller
import functools
# Структура основного навигационнго меню веб-приложения,
# оформленное в виде массива dict объектов


# Функция-декоратор для проверки авторизации пользователя
def login_required(route_func):
    @functools.wraps(route_func)
    def decorated_route(*args, **kwargs):
        # Если не установлен параметр сессии user или значение cookie 'AuthToken' не равно логину пользователя
        if not session.get('user') or request.cookies.get('AuthToken') != session.get('user'):
            # перенаправляем на страницу авторизации
            return redirect(url_for('login'))
        return route_func(*args, **kwargs)
    return decorated_route


# Обработка запроса к индексной странице
@app.route('/ourBlog')
def ourBlog():
    images = ["/static/images/ourBlog/1.png", "/static/images/ourBlog/2.png", "/static/images/ourBlog/3.png",
              "/static/images/ourBlog/4.png", "/static/images/ourBlog/5.png", "/static/images/ourBlog/6.png"]
    menu = ["Первый пункт", "Второй пункт", "Третий пункт", "Четвертый пункт"]
    main__title = "OurBlog"
    main__text = "Here you can follow our news"
    return render_template('ourBlog.html', title="OurBlog", main__title=main__title, main__text=main__text,menu=menu,images=images)

# Обработка запроса к странице contact.html
@app.route('/ourTeam')
def ourTeam():
    main__title = "OurTeam"
    main__text = "Here you can see our team!"
    return render_template('ourTeam.html', title="OurTeam", main__title=main__title, main__text=main__text)
@app.route('/insurance')
def insurance():
    main__title = "Страхование"
    main__text = ""
    return render_template('MethodKinniRaifa.html', title="Страхование", main__title=main__title, main__text=main__text)
# Обработка запроса к индексной странице
@app.route('/')
@app.route('/portfolio')
def portfolio():
    car = []
    car.append((0,'KIA Picanto',"/static/images/portfolio/kia-picanto.png", 67, 6.7, 10.6, '900 000'))
    car.append((1,'KIA RIO',"/static/images/portfolio/kia-rio.png", 100, 7.4, 9.6, '950 000'))
    car.append((2,'KIA RIO X',"/static/images/portfolio/kia-riox.png", 100, 7.1, 9.3, '1 100 000'))
    car.append((3,'KIA Ceed',"/static/images/portfolio/kia-ceed.png", 123, 7.9, 8.6, '1 550 000'))
    return render_template('portfolio.html', title="Сatalog", car=car,main__title="Каталог авто", main__text="Добро пожаловать!")

@app.route('/services')
def services():
    main__title = "Services"
    main__text = "Here you can see our services"
    return render_template('services.html', title="Services", main__title=main__title, main__text=main__text)


# Обработка POST-запроса для демонстрации AJAX
@app.route('/', methods=['POST'])
def post_contact():
    # Если в запросе нет данных или неверный заголовок запроса (т.е. нет 'application/json'),
    # или в этом объекте нет, например, обязательного поля 'name'
    if not request.json or not 'name' in request.json:
        # возвращаем стандартный код 400 HTTP-протокола (неверный запрос)
        return bad_request()
    # Иначе отправляем json-ответ
    else:
        msg = "Дорогой, "+ request.json['name']+" "+request.json['lastname']+", Успех!";
        return json_response({'message': msg})

# Обработка перехода к странице addCar
@app.route('/addCar')
def addCar():
    main__title = "addCar"
    main__text = "Here you can add car!"
    return render_template('addCar.html', title="Добавь машину в базу!",main__title=main__title, main__text=main__text)

# Обработка перехода к странице contact.html
@app.route('/contactUs')
@login_required
def contactUs():
    main__title = "Договор"
    return render_template('contactUs.html', title="ContactUs",main__title=main__title, main__text="")
# Страница авторизации

@app.route('/login', methods=['GET', 'POST'])
def login():
    main__title = "Войти в систему"
    main__text = "Here you can come!"
    # Если POST-запрос
    if request.method == 'POST':
        # если нажата кнопка "Зарегистрировать", переалресуем на страницу регистрации
        if request.form.get('regBtn') == 'true':
            return redirect(url_for('register'))
        # иначе запускаем авторизацию по данным формы
        else:
            return controller.login_user(request.form)
    else:
        return render_template('login.html', title="Login", main__title=main__title, main__text=main__text)

# Страница регистрации
@app.route('/register', methods=['GET', 'POST'])
def register():
    main__title = "Регистрация"
    main__text = "Here you can registrate!"
    # Если POST-запрос, регистрируем нового пользователя
    if request.method == 'POST':
        return controller.register_user(request.form)
    else:
        return render_template('register.html', title='Register', main__title=main__title, main__text=main__text)

"""
    Реализация обработчиков маршрутов (@app.route) REST API для модели ContactRequest (см. models.py).
    Обработчики маршрутов вызывают соответствующие HTTP-методам CRUD-операции из контроллера (см. controller.py)
"""
@app.route('/api/contactrequest', methods=['GET'])
def get_contact_req_all():
    response = controller.get_contact_req_all()
    return json_response(response)

@app.route('/api/contactrequest/<int:id>', methods=['GET'])
def get_contact_req_by_id(id):
    response = controller.get_contact_req_by_id(id)
    return json_response(response)

@app.route('/api/contactrequest/author', methods=['GET'])
def get_get_contact_req_by_author():
    firstname = request.args.get('firstname')
    # Если в адресной строке не передан параметр /api/contactrequest?firstname=<имя_автора>
    if not firstname:
        # то возвращаем стандартный код 400 HTTP-протокола (неверный запрос)
        return bad_request()
        # Иначе отправляем json-ответ
    else:
        response = controller.get_contact_req_by_author(firstname)
    return json_response(response)

@app.route('/api/contactrequest', methods=['POST'])
def create_contact_req():
    # Если в запросе нет данных или неверный заголовок запроса (т.е. нет 'application/json'),
    # или в данных нет обязательного поля 'firstname' или 'lastname'
    if not request.json or not 'firstname' or not 'lastname' in request.json:
        # возвращаем стандартный код 400 HTTP-протокола (неверный запрос)
        return bad_request()
    # Иначе добавляем запись в БД отправляем json-ответ
    else:
        response = controller.create_contact_req(request.json)
        return json_response(response)

# @app.route('/api/test', methods=['POST'])
# def creat():
#     # Если в запросе нет данных или неверный заголовок запроса (т.е. нет 'application/json'),
#     # или в данных нет обязательного поля 'firstname' или 'lastname'
#     # if not request.json or not 'firstname' or not 'lastname' in request.json:
#     #     # возвращаем стандартный код 400 HTTP-протокола (неверный запрос)
#     #     return bad_request()
#     # # Иначе добавляем запись в БД отправляем json-ответ
#     # else:
#     response = controller.get_contact_req_all(request.json)
#     return json_response(response)

@app.route('/api/contactrequest/<int:id>', methods=['PUT'])
def update_contact_req_by_id(id):
    # Если в запросе нет данных или неверный заголовок запроса (т.е. нет 'application/json'),
    # или в данных нет обязательного поля 'city'
    if not request.json or not 'city' in request.json:
        # возвращаем стандартный код 400 HTTP-протокола (неверный запрос)
        return bad_request()
    # Иначе обновляем запись в БД и отправляем json-ответ
    else:
        response = controller.update_contact_req_by_id(id, request.json)
        return json_response(response)

@app.route('/api/contactrequest/<int:id>', methods=['DELETE'])
def delete_contact_req_by_id(id):
    response = controller.delete_contact_req_by_id(id)
    return json_response(response)

#ЗДЕСЬ НАЧНУТСЯ МАШИНЫ
@app.route('/api/cars', methods=['GET'])
def get_car_req_all():
    response = controller.get_car_req_all()
    return json_response(response)

@app.route('/api/cars/<int:id>', methods=['GET'])
def get_car_req_by_id(id):
    response = controller.get_car_req_by_id(id)
    return json_response(response)

@app.route('/api/cars/caption', methods=['GET'])
def get_get_car_req_by_caption():
    caption = request.args.get('caption')
    if not caption:
        # то возвращаем стандартный код 400 HTTP-протокола (неверный запрос)
        return bad_request()
        # Иначе отправляем json-ответ
    else:
        response = controller.get_car_req_by_caption(caption)
    return json_response(response)

@app.route('/api/cars', methods=['POST'])
def create_car_req():
    # Если в запросе нет данных или неверный заголовок запроса (т.е. нет 'application/json'),
    # или в данных нет обязательного поля 'caption' или 'complectation'
    if not request.json or not 'caption' or not 'complectation' in request.json:
        # возвращаем стандартный код 400 HTTP-протокола (неверный запрос)
        return bad_request()
    # Иначе добавляем запись в БД отправляем json-ответ
    else:
        response = controller.create_car_req(request.json)
        return json_response(response)

@app.route('/api/cars/<int:id>', methods=['PUT'])
def update_car_req_by_id(id):
    # Если в запросе нет данных или неверный заголовок запроса (т.е. нет 'application/json'),
    # или в данных нет обязательного поля 'color'
    if not request.json or not 'color' in request.json:
        # возвращаем стандартный код 400 HTTP-протокола (неверный запрос)
        return bad_request()
    # Иначе обновляем запись в БД и отправляем json-ответ
    else:
        response = controller.update_car_req_by_id(id, request.json)
        return json_response(response)

@app.route('/api/cars/<int:id>', methods=['DELETE'])
def delete_car_req_by_id(id):
    response = controller.delete_car_req_by_id(id)
    return json_response(response)

#ЗДЕСЬ НАЧНУТСЯ КЛИЕНТЫ
@app.route('/api/clients', methods=['GET'])
def get_client_req_all():
    response = controller.get_client_req_all()
    return json_response(response)

@app.route('/api/clients/<int:id>', methods=['GET'])
def get_client_req_by_id(id):
    response = controller.get_client_req_by_id(id)
    return json_response(response)

@app.route('/api/clients/caption', methods=['GET'])
def get_get_client_req_by_firstname():
    firstname = request.args.get('firstname')
    if not firstname:
        # то возвращаем стандартный код 400 HTTP-протокола (неверный запрос)
        return bad_request()
        # Иначе отправляем json-ответ
    else:
        response = controller.get_client_req_by_firstname(firstname)
    return json_response(response)

@app.route('/api/clients', methods=['POST'])
def create_client_req():
    # Если в запросе нет данных или неверный заголовок запроса (т.е. нет 'application/json'),
    # или в данных нет обязательного поля 'firstname' или 'lastname'
    if not request.json or not 'firstname' or not 'lastname' in request.json:
        # возвращаем стандартный код 400 HTTP-протокола (неверный запрос)
        return bad_request()
    # Иначе добавляем запись в БД отправляем json-ответ
    else:
        response = controller.create_client_req(request.json)
        return json_response(response)

@app.route('/api/clients/<int:id>', methods=['PUT'])
def update_client_req_by_id(id):
    # Если в запросе нет данных или неверный заголовок запроса (т.е. нет 'application/json'),
    # или в данных нет обязательного поля 'lastname'
    if not request.json or not 'patronymic' in request.json:
        # возвращаем стандартный код 400 HTTP-протокола (неверный запрос)
        return bad_request()
    # Иначе обновляем запись в БД и отправляем json-ответ
    else:
        response = controller.update_client_req_by_id(id, request.json)
        return json_response(response)

@app.route('/api/clients/<int:id>', methods=['DELETE'])
def delete_client_req_by_id(id):
    response = controller.delete_client_req_by_id(id)
    return json_response(response)
"""
Реализация response-методов, возвращающих клиенту стандартные коды протокола HTTP
"""

# Возврат html-страницы с кодом 404 (Не найдено)
@app.route('/notfound')
def not_found_html():
    return render_template('404.html', title='404', err={ 'error': 'Not found', 'code': 404 })

# Формирование json-ответа. Если в метод передается только data (dict-объект), то по-умолчанию устанавливаем код возврата code = 200
# В Flask есть встроенный метод jsonify(dict), который также реализует данный метод (см. пример метода not_found())
def json_response(data, code=200):
    return Response(status=code, mimetype="application/json", response=json.dumps(data))

# Пример формирования json-ответа с использованием встроенного метода jsonify()
# Обработка ошибки 404 протокола HTTP (Данные/страница не найдены)
def not_found():
    return make_response(jsonify({'error': 'Not found'}), 404)

# Обработка ошибки 400 протокола HTTP (Неверный запрос)
def bad_request():
    return make_response(jsonify({'error': 'Bad request'}), 400)


