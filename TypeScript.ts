let gate: boolean = true;
let age: number = 23;
let companyName: string = "Biggie Cheese";

let gate = true;
let age = 23;
let companyName = "Biggie Cheese";

let omni: any = 4;
omni = "could also be a string";
omni = false;
let omni: string = 'asd';

const PI = 3.1415;

// Using the typed array type
let list: number[] = [0.000001, 0.000001, 0.000001]
// Alternatively, using the generic array type
let list: Array<number> = [1,2,3];

enum Color {Red, Green, Blue};
let c: Color = Color.Green;
console.log(Color[c]);

function popup(): void{
    alert("Biggie Cheese");
}

let f1 = function (i: number): number { return i * i; }
let f2 = function (i: number) { return i * i; }
let f3 = (i: number): number => { return i * i; }
let f4 = (i: number) => { return i * i; }
let f5 = (i: number) => i * i;

