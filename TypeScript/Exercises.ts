//**********************************************
//Functions and type of data in typescritp
const multiplicator + (a: number, b: number, printText: string) => {
   console.log(printText, a*b)

}

multiplicator(6, 4, 'Multiplied a string and 4, the result is: ')

//**********************************************
//A calculator
const operation = ['multiply', 'add', 'divide']

const calculator = (a: number, b:number, op:string){
  if(!operation.includes(op)){
    console.log('This operation is not defined')
  }
  if(op == 'multiply') return a*b
  if(op == 'add') return a+b
  if(op == 'divide') return a/b{
    if(b == 0) return "You can't divide by 0"
  }
}

console.log(calculator(8,5,'add'))

//**********************************************
//You can create your own type of data3
type operation = ['multiply', 'add', 'divide']

const calculator = (a: number, b:number, op:operation): number =>{ //Una funcion que devuelve numero o un string
  if(op == 'multiply') return a*b
  if(op == 'add') return a+b

  if(op == 'divide') return a/b{
    if(b == 0) throw mew Error("You can't divide by 0")
  }
}

try { //Para tratar de dividir sobre 0
  console.log(calculator(1,0,'divide'))
} catch (e) {
  console.log('Err',e) //Si no se mandara el error
}

//**********************************************
//De esta forma cuando lo ejecutemos en linea de comando tendremos que pasar los
//parametros --> ts-node Exercises.ts 'a' 'b'
const multiplicator + (a: number, b: number, printText: string) => {
   console.log(printText, a*b)
}

const a: number = Number(process.argv[2])
const b: number = Number(process.argv[3])

multiplicator(a, b, `Multiplied ${a} and ${b} and the result is: `)

//**********************************************
//Parametro 'any' sirve para tener implicito el tipo de dato
const parseArgument = (args) => {
  if (args.length == 4) throw new Error ("Wrong number of arguments")

  const a = Number(args[0])
  const b = Number(args[1])

  if(!isNaN(a) && !isNaN(a)){
    return[a,b]
  }else{
    throw new Error('Provided values were not numbers!')
  }
}

const cleanArguments = parseArguments(process.argv)

const a: number = Number(cleanArguments[0])
const b: number = Number(cleanArguments[1])

multiplicator(a, b, `Multiplied ${a} and ${b} and the result is: `)
