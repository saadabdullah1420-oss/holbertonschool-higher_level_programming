#!/usr/bin/node
const numbers = process.argv.slice(2).map(arg => parseInt(arg));

if (numbers.length < 2) {
  console.log(0);
} else {
  numbers.sort((a, b) => b - a);
  console.log(numbers[1]);
}
