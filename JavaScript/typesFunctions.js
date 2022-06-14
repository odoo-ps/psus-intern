//There are two types of functions

//Name function
function sum(a,b){
    return a+b;
}

function isPositive(number){
    return number >= 0
}

//and functions with no name (annonimus functions)
document.addEventListener('click',function(){
    console.log('Click')
})

//this functions can be converted in arrow-functions, concises and easy to use and read
let sum2 = (a,b) =>{
    return a+b;
}

let isPositive = (number) =>{
    return number >= 0
}

document.addEventListener('click',() => {
    console.log('Click')
})

//even can be more simple (1 one line)
let sum3 = (a,b) => a+b;
let isPositive = number => number >= 0; //whe there is one parameter the parenthesis can be  removed

document.addEventListener('click',() => console.log('Click'))
