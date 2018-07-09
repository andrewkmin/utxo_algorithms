// PLEASE TRY TO SOLVE THIS PROBLEM, THIS IS A REQUIREMENT TO BE CONSIDERED. 
// You possess bitcoins in the form of UTXOs sorted by date and you need to send your friend X bitcoins. 
// Find a date range whose outputs that will result in the least amount of change. 
// Ideal solution will use Python whose function find_range(utxos, x) will give back the start and end dates. 
// Each utxo has value and date (in unix time). *

// Write a Python program that prints the SHA256 hash of "Hello World" in hexadecimal. *

function minCoins(utxos, m, v, someSet) {
  console.log('inside function', utxos)
  // if remaining value < smallest UTXO, we're done
  if (v > utxos[0]) {
    return someSet;
  }

  if (v == utxos[0]) {
    return someSet.add(utxos[0]);
  }

  var subset = new Set();
  console.log('utxos', utxos);
  for (var i = 0; i < utxos.length; i++) {
    let savedVal = utxos[i];
    utxos.splice(i, 1);
    if (utxos[i] <= v) {
      console.log('inside', utxos[i], v)
      subset = minCoins(utxos, m, v - savedVal, someSet);
      someSet.add(savedVal);
    }
  }
  
  let set3 = new Set(function*() { yield* subset; yield* someSet; }());
  return set3; 
}

// need to sort UTXOs by amount
var utxos = [9, 6, 5, 1];
utxos.sort((a, b) => {
  return b - a;
});
var m = utxos.length; // # of utxos we can use
var v = 6; // amount we need change for; try 13
var included = new Set();

// console.log('final', minCoins(utxos, m, v, included));


var newUtxos = [1, 9, 6, 5];

function nonRecursive(value, utxos) {
  var remainder = value;
  // memo here later
  var memo = {};
  for (var i = 0; i < utxos.length; i++) {
    remainder = value;
    let temp = 0;
    for (var j = i; j < utxos.length; j++) {
      if (utxos[j] <= remainder) {
        remainder = remainder - utxos[j];
      } else {
        // save index we break on
        temp = j - 1; // to have inclusive range [i, j] 
        break;
      }
    }
    temp = j-1; // the else statement isn't hit when j is maxed
    // do something with indices here (memoization)
    let str = i + ":" + temp;
    memo[str] = remainder;
  }
  console.log(memo);
}

nonRecursive(50, newUtxos);