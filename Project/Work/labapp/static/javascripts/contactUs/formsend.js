function numberWithSpaces(x) {
    return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, " ");
}
 document.getElementsByClassName("info__model")[0].innerHTML=localStorage.getItem('name')
 document.getElementsByClassName("info__price")[0].innerHTML=numberWithSpaces(localStorage.getItem('price'))+" ₽"
 document.getElementsByClassName("info__complectation")[0].innerHTML=localStorage.getItem('complectation')
 document.getElementsByClassName("info__color")[0].innerHTML=localStorage.getItem('color')
 document.getElementsByClassName("login")[0].innerHTML+=localStorage.getItem('login')
  document.getElementsByClassName("dateNow")[0].innerHTML=new Date().toLocaleDateString()
document.getElementsByClassName("info__options")[0].innerHTML=localStorage.getItem('options')
var sendbtn = document.getElementById("sendbtn");    // выбираем DOM-елемент (кнопку)

// Привязываем к элементу обработчик события "click"
sendbtn.addEventListener("click", function (e) {
    /* Инструкция preventDefault позволяет переопределить стандартное поведение браузера,
    если ее убрать, то браузер по-умолчанию обновит страницу после отправки данных формы */
    e.preventDefault();
    // Получаем данные полей формы
    //Только для клиента
    let llastname= document.getElementsByName("flastname")[0].value
    let lpatronymic = document.getElementsByName("fpatronymic")[0].value
    let lfirstname = document.getElementsByName("ffirstname")[0].value
    let lphone = document.getElementsByName("fphone")[0].value
    let lcity = document.getElementsByName("fcity")[0].value
    let lemail = document.getElementsByName("femail")[0].value
    //Для договора
    let loptions=document.getElementsByClassName("info__options")[0].innerHTML
    let lprice=document.getElementsByClassName("info__price")[0].innerHTML
    let lemployee=document.getElementsByClassName("login")[0].innerHTML
    //Только для авто:
    let lcaption=document.getElementsByClassName("info__model")[0].innerHTML
    let lcomplectation=document.getElementsByClassName("info__complectation")[0].innerHTML
    let lcolor=document.getElementsByClassName("info__color")[0].innerHTML
    // Преобразуем полученные данные в JSON
    var formdata = JSON.stringify({ firstname: lfirstname,lastname:llastname, patronymic: lpatronymic, email: lemail, phone: lphone,city:lcity,options:loptions,price:lprice,employee:lemployee})
    var clientdata = JSON.stringify({ firstname: lfirstname,lastname:llastname, patronymic: lpatronymic, email: lemail, phone: lphone})
    var cardata = JSON.stringify({ caption: lcaption,complectation:lcomplectation, color: lcolor, price: lprice})
    var test = JSON.stringify({'formdata': {formdata}, 'clientdata': {clientdata}, 'cardata': {cardata}});
    // Отправляем запрос через fetch (необходимо выставить соответствующий заголовок (headers)!)
    fetch("/api/contactrequest",
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
    fetch("/api/clients",
    {
        method: "POST",
        body: clientdata,
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
    fetch("/api/cars",
    {
        method: "POST",
        body: cardata,
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

fetch("/api/test",
{
    method: "POST",
    body: test,
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
        alert(test);
    });
})
.catch( error => {
   
});

    
  
});
