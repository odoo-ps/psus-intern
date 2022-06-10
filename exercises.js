// ';' at end of line is good code style
var a; // declaration
var b = 4; // assignment

var c = 5;
c = "value" // value types can change for var

// variable keywords:
/* var   : mutable, can be re-declared
   let   : mutable, can't be re-declared
   const : immutable, can't be re-declared */

var camelCase = 1; // camel case convention
let camelCase2 = 2; // for mutable variables
const CAMEL_CASE_3 = 1; // all caps for immutable

b++; // equivalent to 'b = b + 1;' similarly 'b--;' for 'b = b - 1;'
b += 5; // equivalent to 'b = b + 5;'
/* can use with other operators, -, * and / */

c = "Use \\ as an escape char in strings for special chars \\n or \\'";
console.log(c); // prints passed in variable

var myStr = "test";
myStr += "ing"; // unlike python, '+' operator on strings don't add a space
var strLen = myStr.length; // string acts as 'list' of characters
myStr[0] // index starts at 0

const multiDim = [[1, 2], [3, 4]] // nested arrays are allowed
multiDim[0] = 1; // arrays are mutable even if var itself is const
multiDim[0] = [1, 2];
multiDim[0][1] = 3; // unpacking multidim array, var[row][col]

var exList = [1, 2, 3, 4, 5, 6, 7]
var lastVal = exList.pop() // pop() removes last element, shift() removes first
exList.push(7) // push() adds element at last index, unshift() at first index

function exFunc(num1, num2) {
   var num3 = num1 + num2; // local var, scope only to function
   num3 += b; // can access global vars in same file
   return num3;
}

a = exFunc(1, 3);
console.log(a);

function gteFunc(num1, num2) {
   if (num1 > num2) {  // conditions must be in parentheses and bracketed
      return `${num1} is greater than ${num2}`;
   } else if (num1 == num2) { // else if statement follows trailing bracket
      if (num1 === num2) { // === strictly compares value AND native type of args
         return `${num1} is equal to ${num2}`;
      } else {
         return `${num1} is equal to ${num2} but aren't the same types.`;
         // strings and ints are compared using string ascii values
         // args are implicitly typecasted for comparison unless strict (===)
      }
   } else if (num1 < num2) {
      return `${num1} is less than ${num2}`;
      // ${expression} can be used in strings to refer to variables or dynamic values
   } else { // all else fails
      return "Something went wrong!";
   }
}

// ! (bang) inverse bool, use with == or === (!= or !==)
// && (and) both conditions must be true to return true, else false
// || (or) if all conditions false then return false, else true

function ranged(val) {
   let answer = "";

   switch(val) { // switch-case format
     case 1: // switch case will check all cases after initial
     case 2: // until break is found, running cases
       answer = "Low";
       break;
     case 3:
     case 4:
       answer = "Mid";
       break;
     case 5:
     case 6:
       answer = "High";
       break;
   }
 
   return answer;
 }

// init object structure
const testObj = { // need '=' assignment
  "hat": "ballcap",
  "shirt": "jersey", // use ',' instead of ';'
  "shoes": "cleats"
}; // requires ';' at end
// since property values are mutable, can change it:
// testObj.hat = "bonnet";
// properties can be added or removed:
// testObj.pants = "denim";
// delete testObj.hat;

console.log(testObj.hat); // exObj["prop1"] quotes required for brackets

// https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/basic-javascript/testing-objects-for-properties