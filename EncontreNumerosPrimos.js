function nth_prime(number) {
  const primeNumbers = []

  for(let inteiro = 0; inteiro < number; inteiro++) {
    let isPrime = true;

    for(let i = 0; i <= primeNumbers.length; i++) {
      if( (inteiro % primeNumbers[i] === 0) && inteiro !== primeNumbers[i] ) {
        isPrime = false;
      }
    }

    if((inteiro%1 ===0) && (inteiro % inteiro === 0) && (inteiro !== 1) && isPrime && (number%inteiro  === 0)) {
      primeNumbers.push(inteiro);
    }

  };

  console.table(primeNumbers);
  return primeNumbers[primeNumbers.length-1];
}

console.log(nth_prime(13195));
// nth_prime(13195)