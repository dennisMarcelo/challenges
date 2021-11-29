function caixa(values) {
  let temporaryArray = values;

  for (let index = 0; temporaryArray.length >= index; index++) {
    if(temporaryArray[index] === 0){
      temporaryArray.splice(index-1, 2)

      index = 0;
    }
  };
  
  const soma = temporaryArray.reduce((acc, current) => acc+current);
  
  console.log(soma);
  return soma;
}

caixa([
  1, 3, 5, 4, 0,
  0, 7, 0, 0, 6
])