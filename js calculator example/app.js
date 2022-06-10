const numbers = document.querySelectorAll(".number")
const currentOperand = document.querySelector(".current-operand")
const previousOperand = document.querySelector(".previous-operand")
const equal = document.querySelector(".equal")
const operators = document.querySelectorAll(".operator")
const del = document.querySelector(".del")
const ac = document.querySelector("#ac")
let result = null
let operation = ""
for (const number of numbers) {
    number.addEventListener("click", e =>{
        e.preventDefault()
       
        currentOperand.innerText = currentOperand.innerText+number.innerText
        if (currentOperand.innerText == '.') {
            currentOperand.innerText = '0.'
        }
  

    })
    
}
for (const operator of operators) {
    operator.addEventListener("click", e =>{
        if (currentOperand.innerText == '0.') {
            console.log("si");
            currentOperand.innerText = '0.0'
            previousOperand.innerText = currentOperand.innerText + operator.innerText
        }else{
            previousOperand.innerText = currentOperand.innerText + operator.innerText
        }
       
        result = parseFloat(currentOperand.innerText)
        currentOperand.innerText = ""
        operation = operator.innerText
        console.log(operation);   
    })
    
}
equal.addEventListener("click", e =>{
    e.preventDefault()

    switch (operation) {
        case '+':
                if (currentOperand.innerText != '') {
                    previousOperand.innerText += currentOperand.innerText 
                result += parseInt(currentOperand.innerText)
                currentOperand.innerText = result
                }
                
            break;
        case '-':
                if (currentOperand.innerText != '') {
                    previousOperand.innerText += currentOperand.innerText 
                result -= parseFloat(currentOperand.innerText)
                currentOperand.innerText = result
                }
                
            break
        case '÷':
            if (currentOperand.innerText != '') {
                previousOperand.innerText += currentOperand.innerText 
                result /= parseFloat(currentOperand.innerText)
                if (result == Infinity || result == NaN) {
                    currentOperand.innerText = "ERROR"
                }
                else{
                    currentOperand.innerText = result
                }
            }
               
            break
        case '*':
                if (currentOperand.innerText != '') {
                    previousOperand.innerText += currentOperand.innerText 
                    result *= parseFloat(currentOperand.innerText)
                    currentOperand.innerText = result
                }
                
            break

        default:
            break;
    }
})

del.addEventListener('click', e => {
    e.preventDefault()
    currentOperand.innerText = ''
})

ac.addEventListener('click', e => {
    e.preventDefault()
    currentOperand.innerText = ''
    previousOperand.innerText = ''
})

