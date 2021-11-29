function smallest_multiple(roof) {
  let arrayIntegers = [];
  let multiples = [];

  for(let i = 1; i <= roof; i++) {
    arrayIntegers.push(i);
  }

  for(let i = 0; i < arrayIntegers.length; i++) {
    const allIsOne = arrayIntegers.every((integer) => integer === 1);

    if(allIsOne === true) {
      break;
    } else {
      
      
      i=0
    }
  }

};

smallest_multiple(10);

// O menor número divisível por todos os números de 1 a 10 é 2520. Crie um algoritmo capaz de calcular o 
// menor número divisível  por todos os números de 1 a um dado número.