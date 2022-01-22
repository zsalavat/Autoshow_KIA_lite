const {v1,v6, v3} = require('./sketch');

describe('Функция v1', () => {
    const numbersIn = [18, 100, 28, 61];
    const numbersOut = [0, 0, 0.75, 0.475]
    for(let i = 0; i < numbersIn.length; i++) {
      it('Значение' + ' ' + numbersIn[i] + ' == ' + numbersOut[i], () => {
        expect(v1(numbersIn[i])).toBe(numbersOut[i]);
      });
    }    
});

describe('Функция v6', () => {
    const strIn = ['светлый тон не металлик', 'цветной тон не металлик', 'темный тон не металлик'];
    const numbersOut = [1, 0.75, 0.5]
    for(let i = 0; i < strIn.length; i++) {
      it('Значение' + ' ' + strIn[i] + ' == ' + numbersOut[i], () => {
        expect(v6(strIn[i])).toBe(numbersOut[i]);
    });
  }    
});




// import  v1 from '@/javascripts/methodKinniRaifa/sketch'