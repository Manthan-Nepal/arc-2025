const users = [
  { name: 'jerry', age: 28 },
  { name: 'jane', age: 23 },
  { name: 'joe', age: 32 },
  { name: 'jimmy', age: 21 },
  { name: 'james', age: 26 }
];

// Step 1: Filter users older than 25
const over25 = users.filter(user => user.age > 25);
console.log(over25)