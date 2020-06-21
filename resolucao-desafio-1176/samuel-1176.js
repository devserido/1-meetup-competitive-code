var input = require('fs').readFileSync('/dev/stdin', 'utf8');

function fibonacci(X){
    var a = 0, b = 1, aux;
  
    while (X > 0){
      aux = a;
      a = a + b;
      b = aux;
      X--;
    }
  
    return a;
  }

var lines = input.split('\n');

var Rep = parseInt(lines.shift());

for (var i = 0; i < Rep; i++) {
    var X = parseInt(lines.shift());
   
    var Fib = fibonacci(X);

    console.log('Fib('+X+') = '+Fib);
}
