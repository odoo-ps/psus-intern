const numberButtons = document.querySelectorAll('[data-number]');
const operationButtons = document.querySelectorAll('[data-operation]');
const equalsButton = document.querySelector('[data-equals]');
const deleteButton = document.querySelector('[data-delete]');
const allClearButton = document.querySelector('[data-all-clear]');
const previousOperandTextElement = document.querySelector('[data-previous-operand]');
const currentOperandTextElement = document.querySelector('[data-current-operand]');

class Calculator {
    constructor(prevElem, currElem) {
        this.prevElem = prevElem;
        this.currElem = currElem;
        this.clear();
    }

    clear() {
        this.currElem = '';
        this.prevElem = '';
        this.operation = undefined;
    }
    
    delete() {
        this.currOp = this.currOp.toString().slice(0, -1)
    }
    
    appendNumber(number) {
        if (number === '.' && this.currOp.includes('.')) {
            return;
        }
        this.currOp = this.currOp.toString() + number.toString();
    }
    
    chooseOperation(operation) {
        if (this.currOp === '') {
            return;
        }
        if (this.prevOp !== '') {
            this.compute();
        }
        
        this.operation = operation;
        this.prevOp = this.currOp;
        this.currOp = '';
    }
    
    compute() {
        let computation;
        const prev = parseFloat(this.prevOp);
        const current = parseFloat(this.currOp);

        if (isNaN(prev) || isNaN(current)) {
            return;
        }

        switch (this.operation) {
            case '+':
                computation = prev + current;
                break;
            case '-':
                computation = prev - current;
                break;
            case '*':
                computation = prev * current;
                break;
            case '÷':
                computation = prev / current;
                break;
            default:
                return;
        }

        this.currOp = computation;
        this.operation = undefined;
        this.prevOp = '';
    }
    
    updateDisplay() {
        this.currElem.innerText = this.getDisplayNumber(this.currOp);
        if (this.operation != null) {
            this.prevElem.innerText = `${this.getDisplayNumber(this.prevOp)} ${this.operation}`;
        } else {
            this.prevOp.innerText = '';
        }
    }

    getDisplayNumber() {
        const strNum= number.toString();
        const intNum = parseFloat(strNum.split('.')[0]);
        const decNum = strNum.split('.')[1];
        let intDisp; // try if display already exists

        if (isNaN(intNum)) {
            intDisp = '';
        } else {
            intDisp = intNum.toLocaleString('en', { maximumFractionDigits: 0 });
        }
        if (decNum != null) {
            return `${intNum}.${decNum}`;
        } else {
            return intDisp;
        }
    }
};