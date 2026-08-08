#!/usr/bin/node
const args = process.argv.slice(2);

if (args.length < 2) {
  console.log(0);
} else {
  let max = -Infinity;
  let second = -Infinity;

  for (let i = 0; i < args.length; i++) {
    const num = parseInt(args[i], 10);
    if (num > max) {
      second = max;
      max = num;
    } else if (num > second && num < max) {
      second = num;
    }
  }

  console.log(second === -Infinity ? 0 : second);
}
