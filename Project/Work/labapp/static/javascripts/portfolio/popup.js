jQuery(document).ready(function($){
var basePrice;
class Popup {
    constructor(name, img, price) {
        this.container = document.createElement('div');
        this.container.className = 'popup';          
        this.container.innerHTML = this.render(name, img, price);
        basePrice=price;
        basePrice=basePrice.split(' ').join('');
        localStorage.setItem('name',name);
        localStorage.setItem('price',price);
        this.insert();
    }
    render(name, img) {  return `                
    <div class="popup__body">
        <div class="popup__content">
            <a href="#header" class="popup__close close-popup">X</a>
            <div class="popup__car-img car__img"><img src="${img}" alt=""></div>
            <div class="popup__car-name" >${name}</div>
            <div class="popup__configuration">
            <div class="popup__text">Комплектация:</div>
                 <input class="form__input_1" placeholder="Стандарт" list="id1" name="reqComplectation">
                <datalist id="id1">
                <option value="Стандарт"></option>
                <option value="Люкс"></option>
                </datalist>
            </div>
            <div class="popup__car-colors">
                 <div class="popup__text">Цвет:</div>
                 <input class="form__input_2" placeholder="Красный" list="id2" name="reqColor">
                <datalist id="id2">
                <option value="Красный"></option>
                <option value="Синий"></option>
                </datalist>
            </div>
                    <div class="checkbox">
      <input type="checkbox" id="click" name="Зимняя  резина" data="70000">
      <label for="click" class="text"> Зимняя  резина </label>
      <input type="checkbox" id="click" name="Тонировка" data="10000">
      <label for="click" class="text"> Тонировка </label>
      <input type="checkbox" id="click" name="Чехлы для сидений" data="20000">
      <label for="click" class="text"> Чехлы для сидений</label>
    </div>
            <button class="popup__button button" id="sendbtn"><a href="/contactUs">Продолжить</a></button>
        </div>
    </div>
    `              
}
    hide() {
        this.container.classList.remove('open');     
        this.destroy();            
    }

    insert() {
        container.insertAdjacentElement('beforeend', this.container);
        
        const closeLink = document.querySelector('.close-popup');
        closeLink.addEventListener(
            'click',
            (e) => { this.hide(); }
        );        
        this.container.addEventListener('click', (e) =>{
            if(!e.target.closest('.popup__content')) {
                this.hide();
            }
        });
               
    }       
    show() {
        this.container.classList.add('open');
        var btn=document.getElementById("sendbtn");
btn.addEventListener("click", function (e) {
    let complectation = document.getElementsByName("reqComplectation")[0].value;
    let color = document.getElementsByName("reqColor")[0].value;
    let options=" ";
    let priceOptions=0;
$('input:checkbox:checked').each(function(){
	options+=$(this).attr("name")+", ";
	priceOptions+=parseFloat($(this).attr("data"));
});
    if(complectation=="Люкс"){
        localStorage.setItem('price',String(parseFloat(basePrice)*1.2+parseFloat(priceOptions)));
    }
    else{
     localStorage.setItem('price',String(parseFloat(basePrice)+parseFloat(priceOptions)));
    }
    localStorage.setItem('complectation', complectation);
    localStorage.setItem('color', color);
    options=options.replace(/,\s*$/, "");
    localStorage.setItem('options',options);
});


    }
    destroy() {
        this.container.remove();
    }
   

}

function select(object) {
    if(object.classList.contains('active')) {
        object.classList.remove('active');
    }
    else {
        object.classList.add('active');
    }
}
const container = document.querySelector('.container');
const link = document.querySelectorAll('.car');


for(var i=0; i<link.length; i++) {
        link[i].addEventListener('click', function (e) {  
            const name = document.getElementById("name_" + $(car).index(this)).getAttribute("name");
            const img = document.getElementById("img_" + $(car).index(this)).getAttribute("name");
            const price = document.getElementById("price_" + $(car).index(this)).getAttribute("name");
            const popup = new Popup(name, img, price);
            popup.show();
        })
}
});


