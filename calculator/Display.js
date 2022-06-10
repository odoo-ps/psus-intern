class Display {
  constructor(displayPreviousValue, displayCurrentValue) {
    this.displayPreviousValue = displayPreviousValue;
    this.displayCurrentValue = displayCurrentValue;
    this.calculator = new Calculator();
    this.current_value = "";
    this.previous_value = "";
    this.operator = undefined;
    this.signos = {
      sumar: "+",
      restar: "-",
      multiplicar: "x",
      dividir: "/",
    };
  }

  delete() {
    this.current_value = this.current_value.toString().slice(0, -1); // delete the last character of the current value
    this.printValue();
  }

  deleteAll() {
    this.current_value = "";
    this.previous_value = "";
    this.operator = undefined;
    this.printValue();
  }

  addNumber(number) {
    if (number === "." && this.current_value.includes(".")) {
      return;
    }
    this.current_value = this.current_value.toString() + number.toString();
    this.printValue();
  }

  compute(operator) {
    this.operator !== "igual" && this.calculate(); // if there is an operator in the calculator already execute the calculation
    this.operator = operator;
    this.previous_value = this.current_value || this.previous_value; // if there is no current value, use the previous value
    this.current_value = "";
    this.printValue();
  }

  printValue() {
    this.displayCurrentValue.textContent = this.current_value;
    this.displayPreviousValue.textContent = `${this.previous_value} ${
      this.signos[this.operator] || "" // if there is an operator, print it with the sign of the operator
    }`;
  }

  calculate() {
    const previous_value = parseFloat(this.previous_value);
    const current_value = parseFloat(this.current_value);
    if (isNaN(previous_value) || isNaN(current_value)) {
      // if the previous value or current value is not a number, return
      return;
    }
    this.current_value = this.calculator[this.operator](
      previous_value,
      current_value
    ); // execute the calculation with the operator and the previous and current values
  }
}
