function log(...args) {
  console.log(...args);
}

// 判断输入是否为质数
function isPrime(num) {
  num = parseInt(num);
  if (num < 2) { return false }
  if (num === 2) { return true }
  if (num % 2 === 0) { return false }
  for (let i = 3; i <= Math.sqrt(num); i += 2) {
    if (num % i === 0) { return false }
  }
  return true;
}

// 第 n 个质数
function nthPrime(n) {
  let count = 0;
  let num = 2;
  while (count < n) {
    if (isPrime(num)) {
      count++;
    }
    num++;
  }
  return num - 1;
}

export default { log, isPrime, nthPrime };
