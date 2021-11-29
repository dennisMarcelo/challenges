function nth_prime(n) {
  const primeNumbers = []
  let number = null;

  while(primeNumbers.length < n){
    let isPrime = true;
    for(let i = 0; i <= primeNumbers.length; i++) {
      if( (number % primeNumbers[i] === 0) && number !== primeNumbers[i] ) {
        isPrime = false;
      }
    }

    if((number%1 ===0) && (number % number === 0) && (number !== 1) && isPrime) {
      primeNumbers.push(number);
    }

    number += 1;
  }

  console.log(primeNumbers);
  return primeNumbers[n-1];
}

console.log(nth_prime(6));
// nth_prime(6)