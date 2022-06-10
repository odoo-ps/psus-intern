//lets create a bubble sort function
function bubbleSort(array) {
  //we need to loop through the array
  for (var i = 0; i < array.length; i++) {
    //we need to loop through the array again
    for (var j = 0; j < array.length; j++) {
      //if the current value is greater than the next value
      if (array[j] > array[j + 1]) {
        //we need to swap the values
        var temp = array[j];
        array[j] = array[j + 1];
        array[j + 1] = temp;
      }
    }
  }
  //return the sorted array
  return array;
}

const array = [5, 3, 4, 1, 2];
console.log(bubbleSort(array));
