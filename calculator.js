function addText(char){
    s = document.getElementById("textbox").innerHTML;
    if (containsLetter(s)){
        document.getElementById("textbox").innerHTML = String(char);
    }
    else {
        document.getElementById("textbox").innerHTML += String(char);
    }
}

function containsLetter(str){
    for (char of str){
        if ((/[a-zA-Z]/).test(char)){
            return true;
        }
    } return false;
}

function clearTextBox(){
    document.getElementById("textbox").innerHTML = "";
}

function submit(){
    s = document.getElementById("textbox").innerHTML;
    clearTextBox();
    itemArray = new Array();
    num = "";
    for (let char of s){
        if (!isNaN(char) || char == "."){
            num += char;
        }
        else {
            if (num == ""){
                itemArray.push(char);
            }
            else {
                itemArray.push(Number(num));
                itemArray.push(char)
                num = "";
            }
        }
    }
    if (num != ""){
        itemArray.push(Number(num));
    }
    console.log(itemArray);
    calculate(itemArray);
}

function isValid(items){
    if (items.includes(NaN)){
        return false;
    }
    return true;
}

function calculate(items){
    if (items.length == 0){
        document.getElementById("textbox").innerHTML = 0;
        return;
    }
    if (items.length == 1){
        if (!isNaN(items[0])){
            document.getElementById("textbox").innerHTML = items[0];
            return;
        }
        else{
            document.getElementById("textbox").innerHTML = "bruh";
            return;
        }
    }
    if (items[0] == '-'){
        items.shift();
        items[0] *= -1;
        result = items[0];
    }
    while (items.length >= 3){
        if (items[1] == '+'){
            result = items[0] + items[2];
        }
        else if (items[1] == '-'){
            result = items[0] - items[2];
        }
        else if (items[1] == '*'){
            result = items[0] * items[2];
        }
        else if (items[1] == '/'){
            result = items[0] / items[2];
        }
        items.shift(); items.shift();
        items[0] = result;
        console.log(items);
    }
    if (isNaN(result)){
        document.getElementById("textbox").innerHTML = "bruh";
    }
    else{
        document.getElementById("textbox").innerHTML = result;
    }
}
