/*

Inventory Update
Compare and update the inventory stored in a 2D array against a second 2D array of a fresh delivery.
Update the current existing inventory item quantities (in arr1). If an item cannot be found, add the new item and quantity into the inventory array.
The returned inventory array should be in alphabetical order by item.

*/

// Example inventory lists
const curInv = [
  [21, "Bowling Ball"],
  [2, "Dirty Sock"],
  [1, "Hair Pin"],
  [5, "Microphone"],
];

const newInv = [
  [2, "Hair Pin"],
  [3, "Half-Eaten Apple"],
  [67, "Bowling Ball"],
  [7, "Toothpaste"],
];

function updateInventory(curInv, newInv) {
  let updateInventory = [];
  // iterate through newInv
  for (let i = 0; i < newInv.length; i++) {
    let boolean_add = false;
    // iterate through curInv
    for (let j = 0; j < curInv.length; j++) {
      // if the new iteam is already in curInv
      if (newInv[i][1] === curInv[j][1]) {
        boolean_add = false;
        // add the new quantity to the current quantity
        curInv[j][0] += newInv[i][0];
        break;
      } else {
        boolean_add = true;
      }
    }
    // if the new item is not in curInv
    if (boolean_add) {
      updateInventory.push(newInv[i]);
    }
  }
  updateInventory = updateInventory.concat(curInv);
  updateInventory.sort((a, b) => {
    if (a[1] < b[1]) {
      return -1;
    }
    if (a[1] > b[1]) {
      return 1;
    }
    return 0;
  });
  return updateInventory;
}

const updatedInventory = updateInventory(curInv, newInv);
console.log(updatedInventory);
