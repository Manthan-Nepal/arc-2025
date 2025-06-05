const users = [
  { name: 'jerry', age: 28 },
  { name: 'jane', age: 23 },
  { name: 'joe', age: 32 },
  { name: 'jimmy', age: 21 },
  { name: 'james', age: 26 }
];

// Filter users older than 25
const over25 = users.filter(user => user.age > 25);
console.log(over25)

//Increase age of each user by 2 years
const increaseage = users.map(user=>user.age+2);
console.log(increaseage)

// Calculate average age
const avgAge = users.reduce((sum, user) => sum + user.age, 0) / users.length;
console.log(avgAge.toFixed(2));
