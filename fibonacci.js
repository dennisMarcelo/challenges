function even_fibonacci_numbers(roof) {
  let penultimate = 0;
  let last = 1;
  let sum = null;
  
  for(let  cont = 0; cont < roof; cont ++){
      let fibonacci = penultimate + last;
      if(fibonacci < roof && fibonacci%2 === 0 ){
        sum += fibonacci;
      }
      
      penultimate = last;
      last = fibonacci
      
  }
  
  return sum;
}

console.log(even_fibonacci_numbers(10000000))