/**
 * @param {number} n
 * @return {number}
 */
 var countPrimes = function(n) {
    
  let primeNumbers = [];
  
  for (let i = 2; i < n; i++) {
      
      let factors = [];
      
      for (let k = 0; k <= i; k++) {
          
          if (i % k == 0) {
              factors.push(k);
          }
          
      }
          
      if (factors.length <= 2) {
          primeNumbers.push(i);
      }
      
  }
  
  return primeNumbers.length;
  
};