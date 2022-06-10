//***************************************
//Triple igual

/*function compare(a,b){
    if (a === b){
        return "Equal";
    }else{
        return "Not Equal";
    }
}

console.log(compare(5,"5"));

//***************************************
//shift() y psuh()
function nextInLine(arr,item){
    arr.push(item);
    return arr.shift();
}

var testArr =[1,2,3,4,5];

console.log("Before: " + JSON.stringify(testArr));
console.log(nextInLine(testArr,6));
console.log("After: " + JSON.stringify(testArr));

//***************************************
//"Objetos anidados"
var dog = {
    "name": "Merry",
    "owners": ["David","Erick","Angel"],
    "race":"Chihuahua",
    "age":2
};

console.log(dog.name);
console.log(dog["owners"]);
delete dog.age;
console.log(dog);

myStorage = {
    "car": {
        "inside": {
            "glove box": "maps",
            "passenger seat": "crumbs"
        },
        "outside":{
            "trunk": "jack"
        }
    }
};

console.log(myStorage.car.inside["glove box"]); 

//***************************************
//JSON.stringify, un objeto se convierte en un JSON string
console.log(JSON.stringify({ x: 5, y: 6 }));
console.log(JSON.stringify(new Date(2006, 0, 2, 15, 4, 5)));
console.log(JSON.stringify({ x: [10, undefined, function(){}, Symbol('')] }));
console.log(JSON.stringify([new Number(3), new String('false'), new Boolean(false)]));

//***************************************
//Cambiando el tipo de datos
console.log(parseInt("5"));
console.log(parseInt("10011",2)); //Binario

//***************************************
//Ternary Operator
function checkEqual(a,b){
    return a === b ? true: false;
}

console.log(checkEqual(5,"5"));

//***************************************
// More complex ternary operator
function checkSign(num){
    return num > 0 ? "positive" : num < 0 ? "negative" : "zero";
}

console.log(checkSign(0));

//***************************************
// Arrow functions
var magic = () => {
    return new Date();
};
//Equivalente a la de arriba
var magic = () => new Date();

//Con parametros
const myConcat = (arr1,arr2) => arr1.concat(arr2);
console.log(myConcat([1,2,3],[2,2]))

//Funciones de orden mayor
const realNumberArray = [4,5.6,-9,3.14]

const squareList = (arr)=>{
    const squaredIntegers = arr.filter(num => Number.isInteger(num) && num > 0).map(x => x*x);
    return squaredIntegers;
}

const squaredIntegers = squareList(realNumberArray);
console.log(squaredIntegers);

//***************************************
//Default Parameters y function()
const increment = (function(){
    return function increment(number,value=1){
        return number+value;
    }
})();

const stats = {
    max: 56.78,
    standar_deviation: 4.34,
    median: 34.54, 
    min: -0.75
}

const half = (function(){
    return function half({max,min}){ //Destructuring Assignment
        return (max + min) / 2.0;
    };
})();
console.log(status);
console.log(half(stats));

//***************************************
//Rest operator
const sum = (function(){
    return function sum(...args){ //rest operator, ..args
        return args.reduce((a,b)=> a+b,0);
    }
})(); 
console.log(sum(1,2,3));

//***************************************
//Spread operator
const arr1 = ['JAN','FEB','MAR']
let arr2;
(function(){
    arr2 = [...arr1];
    arr1[0] = 'potato';
})();

//***************************************
//Complex strings
const person = {
    name: "Mario"
};

consta greeting = `Hello, my name is ${person.name}!`;
console.log(greeting);

//***************************************
//Clases, constructores, get y set
class Book{
    constructor(author){
        this._author = author;
    }

    get writer(){
        return this._author;
    }

    set writer(updatedAuthor){
        this._author = updatedAuthor;
    }
}*/

