 
// Variables in Javascript

/*

A variable refers to a Value that can be changed during program execution.Variables are the names given
to memory locations.javaScript variables are created using 'var', 'let', or 'const' keyword followed by 
an assignment.

*/


// Rules for declaring variable in javascript
/*

    1. Should contain only alphanumeric, _, $
    2. should start with _, $,TEXT
    3. Should not contain spaces.

*/


// Example

let a = 'orange';
console.log(a)              //oragne


// Differnt types of Variable in Javascript
/*

var:variable can be re-declared and updated .A global scope variable.
let: variable cannot be re-declared but can be updated.A block scope variable.
const:variable cannot be re-declared or updated.A block scope variable

*/




// Datatypes and type Correction


/*

Datatypes defines the type and charactertics of a variable.

types: Primitive, Non-primitive


*/

// Primitive Datatype

/*
Primitive Datatypes are the fundamental datatypes that are not derived from other datatypes and helps
in the formation of non-primitive datatypes.

For eg: Number,BigInt ,Boolean, Undefined ,Null , Symbol , String

*/


// Non-Primitive Datatypes

/*
Non-Primitive Datatypes are derived from primitive datatypes and are Complex.

For eg: Array,Set ,object and Map
*/

// Type Conversion
// Types of Type Conversion

/*
The process of converting a variable from one data type to another.
1. Implicit type conversion
2. Explicit type conversion
*/

// Implicit Type Conversion
/*
JavaScript automatically converts one data type to another during operations.
*/

console.log("\nImplicity type conversion");
console.log("Float, Boolean, String");
console.log(10 + 3.14); // 13.14 (integer => float)
console.log(10 + true); // 11 (true is converted to 1)
console.log(10 + "5"); //105 (number => string, concatenation)
console.log(10 - "3"); //7 (string => number)
console.log(10 * "4"); //40 (sstring => number)
console.log(10 / "2"); //5 (string => number)

// Explicit Type Conversion (Casting)
/*
Explicit type conversion, or casting, is done manually by the programmer using JavaScript built-in functions like:
Number(), BigInt(), Boolean(),  undefined(), null(), Symbol(), String()
*/

console.log("\nExplicity type conversion");
console.log("Integer");
console.log(Number(10)); //10
console.log(Number("123")); //123


console.log("\nBigInt");
console.log(BigInt(10)); //10n


console.log("\nBoolean");
console.log(Boolean(10)); //true


console.log("\nString");
console.log(String("Hello World!!!")); //Hello World!!!
console.log(String(12345)); //12345


// Arrow Function


let result2 = (a,b)=>{
    return a+b;
}

console.log('arrow function',result2(5,6));


// Single parameter(arrow function)
let square = a=>a*a
console.log('arrow function(single parameter)',square(5));

// Empty Paranthesis

let empty = ()=>'hello world';
console.log('empty parameter',empty());


// Template literals (string interpolation)


var b = 'Hello';

console.log(`${b} , I am Adish Prajapati`)
