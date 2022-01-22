/*
Реализация AJAX с помощью асинхронного метода fetch. Современный вариант реализации AJAX.
*/

var sendbtn = document.getElementById("sendbtn");    // выбираем DOM-елемент (кнопку)

// Привязываем к элементу обработчик события "click"
sendbtn.addEventListener("click", function (e) {
    /* Инструкция preventDefault позволяет переопределить стандартное поведение браузера,
    если ее убрать, то браузер по-умолчанию обновит страницу после отправки данных формы */
    e.preventDefault();
    // Получаем данные полей формы
    let fcaption = document.getElementsByName("fcaption")[0].value;
    let fcomplectation = document.getElementsByName("fcomplectation")[0].value;
    let fcolor = document.getElementsByName("fcolor")[0].value;
    let fprice = document.getElementsByName("fprice")[0].value
    // Преобразуем полученные данные в JSON
    var formdata = JSON.stringify({ caption: fcaption,complectation:fcomplectation, color: fcolor, price: fprice});

    // Отправляем запрос через fetch (необходимо выставить соответствующий заголовок (headers)!)
    fetch("/api/cars",
    {
        method: "POST",
        body: formdata,
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then( response => {
        // fetch в случае успешной отправки возвращает Promise, содержащий response объект (ответ на запрос)
        // Возвращаем json-объект из response и получаем данные из поля message
        response.json().then(function(data) {
            console.log(data)
            let statfield = document.getElementById("statusfield");
            //statfield.textContent = data.message;
            //statfield.textContent.bold();
            alert(data.message);
        });
    })
    .catch( error => {
        alert(error);
        console.error('error:', error);
    });
});