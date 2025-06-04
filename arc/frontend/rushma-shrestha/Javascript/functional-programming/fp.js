

const nums = [1, 2, 3];
const squared = nums.map(n => n * n);
// [1, 4, 9]
console.log(squared)

const users = [{id: 1}, {id: 2}, {id: 3}];
const user = users.find(u => u.id === 2);

console.log(user);

const orders = [
  { customer: "Alice", total: 25 },
  { customer: "Bob", total: 75 },
  { customer: "Alice", total: 100 }
];

const aliceTotal = orders
  .filter(order => order.customer === "Alice")
  .map(order => order.total)
  .reduce((sum, value) => sum + value, 0);

// Result: 125
console.log(aliceTotal);