// JavaScript commonly has three variable declarations:

// 1) let
// Used to declare a variable that can be reassigned.
// It has BLOCK scope, not necessarily "local" scope.
let name = "Raju";

// 2) var
// Used to declare a variable with FUNCTION scope.
// It is NOT automatically global.
var age = 26;

// 3) const
// Used to declare a variable that cannot be reassigned.
// It also has BLOCK scope.
// It is NOT necessarily global.
const nam = "name";

console.log("My name is", name, nam);

// nam = "Johnson"; // Error: Assignment to constant variable

console.log("My age is", age);

let b = 10;
let a = 23;

console.log("Sum is", a + b);

let is_it_right = false;
console.log(is_it_right);

// let and const have block scope.
// var has function scope.

// Declaration
let year;

// Initialization
year = 2026;

console.log("Year is", year);
console.log("Inside the script");
