const displayPreviousValue = document.getElementById("previous_value");
const displayCurrentValue = document.getElementById("current_value");
const buttonNumber = document.querySelectorAll(".number"); // array of buttons
const buttonOptions = document.querySelectorAll(".operator"); // array of operators

const display = new Display(displayPreviousValue, displayCurrentValue);

buttonNumber.forEach((button) => {
  button.addEventListener("click", () => {
    display.addNumber(button.innerHTML);
  });
});

buttonOptions.forEach((button) => {
  button.addEventListener("click", () => {
    display.compute(button.value);
  });
});
