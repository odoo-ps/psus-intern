class Calculator{
    constructor(previousOperandTextElement,currentOperandTextElement){
        this.previousOperandTextElement =previousOperandTextElement
        this.currentOperandTextElement =currentOperandTextElement
        this.clear()

    }

    clear(){
        this.previousOp = ''
        this.currentOp = ''
        this.operation =undefined
    }
    delete(){
        this.currentOp =this.currentOp.toString().slice(0,-1)

    }
    appendNumber(number){
        if(number === '.' && this.currentOp.includes('.')) return 

        this.currentOp =this.currentOp.toString() + number.toString()

    }

    chooseOperation(operation){
        if(this.currentOp === '') return
        if(this.previousOp !== ''){
            this.compute()
        }
        this.operation =operation
        console.log(operation)
        this.previousOp =this.currentOp
        this.currentOp =''
    }

    compute(){
        let computation
        const prev = parseFloat(this.previousOp)
        const curr =parseFloat(this.currentOp)

        if(isNaN(prev) || isNaN(curr)) return 
        console.log(this.operation)
        switch(this.operation){
            case '+':
                computation =prev +curr
                break
            case '-':
                computation =prev - curr
                break
            case '*':
                computation = prev * curr
                break
            case '/':
                computation = prev / curr
                break
            default:
                return
        }

        this.currentOp =computation
        this.operation =undefined
        this.previousOp =''
    }
    getDisplayNumber(number){
        const stringNumber = number.toString()
        const integerDigits = parseFloat(stringNumber.split('.')[0])
        const decimalDigits = (stringNumber.split('.')[1])
        let integerDisplay
        if(isNaN(integerDigits)){
            integerDisplay =''

        }else{
            integerDisplay =integerDigits.toLocaleString('en',{
                maximumFractionDigits:0
            })
        }

        if(decimalDigits !=null){
            return `${integerDisplay}.${decimalDigits}`
        }else{
            return integerDisplay
        }
        return number
    }
    updateDisplay(){
        this.currentOperandTextElement.innerText =this.getDisplayNumber(this.currentOp)
        if(this.operation != null){
            this.previousOperandTextElement.innerText=`
                ${this.getDisplayNumber(this.previousOp)} ${this.operation}`
        }else{
            this.previousOperandTextElement.innerText= ''

        }
    }
}
const numberButtons = document.querySelectorAll('[data-number]')
const opButtons = document.querySelectorAll('[data-operation]')
const equalsButton = document.querySelector('[data-equals]')
const deleteButton = document.querySelector('[data-delete]')
const allClearButton = document.querySelector('[data-allclear]')
const previousOperandTextElement = document.querySelector('[data-previous-operand]')
const currentOperandTextElement = document.querySelector('[data-current-operand]')

const calculator = new Calculator(previousOperandTextElement,currentOperandTextElement)

numberButtons.forEach(button => {
    button.addEventListener('click',()=>{
        calculator.appendNumber(button.innerText)
        calculator.updateDisplay()
    })
})

opButtons.forEach(button => {
    button.addEventListener('click',()=>{
        console.log(button.innerText)
        calculator.chooseOperation(button.innerText)
        calculator.updateDisplay()
    })
})

equalsButton.addEventListener('click', button =>{
    calculator.compute()
    calculator.updateDisplay()
})

allClearButton.addEventListener('click', button =>{
    calculator.clear()
    calculator.updateDisplay()
})

deleteButton.addEventListener('click',button=>{
    calculator.delete()
    calculator.updateDisplay()
})