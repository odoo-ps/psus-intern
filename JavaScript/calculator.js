const form = document.getElementById("form");

/*const inputs = document.querySelectorAll("#form input");
/*const expresions = {
  nums : /^,{1,9999999999}$/
}

const validarFormulario = (e) =>{
  switch (e.target.name) {
    case "num1":
    console.log("Num 1 is: "+e.target.value);
    break;

    case "num2":
    console.log("Num 2 is: "+e.target.value);
    break;

  }
}

inputs.forEach((input) => {
  input.addEventListener("keyup", validarFormulario);
  input.addEventListener("blur", validarFormulario);
});*/

function calculate(num1,num2,op){
  switch (op) {
    case "Addition":
      alert("Result: "+ (num1 + num2));
    break;

    case "Subtraction":
      alert("Result: "+ (num1 - num2));
    break;

    case "Multiplication":
      alert("Result: "+ (num1 * num2));
    break;

    case "Division":
      alert("Result: "+ (num1 / num2));
    break;
  }
}

form.addEventListener("submit", (e) =>  {

  e.preventDefault();

  const num1 = document.getElementById("num1");
  const num2 = document.getElementById("num2");
  const op = document.getElementById("op");

  console.log("Num 1 is: "+ num1.value);
  console.log("Num 2 is: "+ num2.value);
  console.log("Operation: "+ op.value);


  calculate(Number(num1.value),Number(num2.value),op.value);

});
