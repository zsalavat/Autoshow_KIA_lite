// select elements
let extraDriversCount;
let carColor;
let noCrashYear;

// input elements
let driverAge;
let experience;
let carAge;
let carPrice;
let rate;
var btn=document.getElementById("sendbtn");
btn.addEventListener("click", function (e) {
extraDriversCount= document.getElementsByName("extraDriversCount")[0];
carColor= document.getElementsByName("carColor")[0];
noCrashYear= document.getElementsByName("noCrashYear")[0];
driverAge=document.getElementsByName("driverAge")[0];
experience=document.getElementsByName("experience")[0];
carAge=document.getElementsByName("carAge")[0];
carPrice= document.getElementsByName("carPrice")[0];
rate=document.getElementsByName("rate")[0];
  let lambdas = [0.15, 0.166, 0.075, 0.2, 0.184, 0.1, 0.125];
  let risk = lambdas[0] * v1(parseFloat(driverAge.value)) + lambdas[1] * v2(parseFloat(experience.value)) +
  lambdas[2] * v3(parseFloat(extraDriversCount.value)) + lambdas[3] * v4(parseFloat(carAge.value)) +
  lambdas[4] * v5(parseFloat(carPrice.value)) + lambdas[5] * v6(carColor.value) + lambdas[6] * v7(parseFloat(noCrashYear.value));
  // answer
  let result=(1-parseFloat(risk))*parseFloat(rate.value);
   alert("Стоимость вашей страховки составит:"+result.toFixed(2)+"₽"+" в год");
});

function getValueFromLine(x1, y1, x2, y2, x) {
  let A = y2 - y1;
  let B = x1 - x2;
  let C = x1 * (y1 - y2) + y1 * (x2 - x1);

  return -(A * x + C) / B;
}

function v1(x) {
  if (x == 18) {
    return 0;
  }
  else if (x <= 26) {
    return getValueFromLine(18, 0, 26, 0.5, x);
  }
  else if (x <= 30) {
    return getValueFromLine(26, 0.5, 30, 1, x);
  }
  else if (x <= 50) {
    return 1;
  }
  else if (x <= 60) {
    return getValueFromLine(50, 1, 60, 0.5, x);
  }
  else if (x <= 80) {
    return getValueFromLine(60, 0.5, 80, 0, x);
  }
  else {
    return 0;
  }
}

function v2(x) {
  if (x == 0) {
    return 0;
  }
  else if (x <= 3) {
    return getValueFromLine(0, 0, 3, 0.25, x);
  }
  else if (x <= 5) {
    return getValueFromLine(3, 0.25, 5, 0.5, x);
  }
  else if (x <= 25) {
    return getValueFromLine(5, 0.5, 25, 0.75, x);
  }
  else if (x <= 60) {
    return getValueFromLine(25, 0.75, 60, 1, x);
  }
  else {
    return 1;
  }
}

function v3(x) {
  if (x == 0) {
    return 1;
  }
  else if (x == 1) {
    return 0.75;
  }
  else if (x == 2) {
    return 0.5;
  }
  else {
    return 0;
  }
}

function v4(x) {
  if (x == 0) {
    return 1;
  }
  else if (x <= 3) {
    return getValueFromLine(0, 1, 3, 0.75, x);
  }
  else if (x <= 5) {
    return getValueFromLine(3, 0.75, 5, 0.5, x);
  }
  else if (x <= 7) {
    return getValueFromLine(5, 0.5, 7, 0.25, x);
  }
  else if (x <= 20) {
    return getValueFromLine(7, 0.25, 20, 0, x);
  }
  else {
    return 0;
  }
}

function v5(x) {
  if (x == 0) {
    return 1;
  }
  else if (x <= 70) {
    return getValueFromLine(0, 1, 100, 0.75, x);
  }
  else if (x <= 180) {
    return getValueFromLine(100, 0.75, 200, 0.5, x);
  }
  else if (x <= 300) {
    return getValueFromLine(200, 0.5, 300, 0.25, x);
  }
  else if (x <= 1000) {
    return getValueFromLine(300, 0.25, 1000, 0, x);
  }
  else {
    return 0;
  }
}

function v6(xStr) {
  let x = 0;
  if (xStr == 'светлый тон не металлик') {
    x = 0;
  }
  else if (xStr == 'цветной тон не металлик') {
    x = 1;
  }
  else if (xStr == 'темный тон не металлик') {
    x = 2;
  }
  else {
    x = 3;
  }

  return v3(x);
}

function v7(x) {
  if (x == 0) {
    return 0;
  }
  else if (x == 1) {
    return 0.25;
  }
  else if (x == 2) {
    return 0.5;
  }
  else if (x == 3) {
    return 0.75;
  }
  else {
    return 1;
  }
}

  module.exports = {v1, v6, v3}




//   // select elements
// let extraDriversCount = 23;
// let carColor= 3;
// let noCrashYear= 3;

// // input elements
// let driverAge = 2;
// let experience = 3;
// let carAge= 3;
// let carPrice= 3;
// let rate= 3;