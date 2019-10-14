function swap(items, leftIndex, rightIndex){
    let temp = items[leftIndex];
    items[leftIndex] = items[rightIndex];
    items[rightIndex] = temp;
}
function partition(items, left, right) {
    let pivot   = items[Math.floor((right + left) / 2)], //middle element
        i       = left, //left pointer
        j       = right; //right pointer
    while (i <= j) {
        while (items[i] < pivot) {
            i++;
        }
        while (items[j] > pivot) {
            j--;
        }
        if (i <= j) {
            swap(items, i, j); //sawpping two elements
            i++;
            j--;
        }
    }
    return i;
}

function quicksort2(items, left, right) {
    let index;
    if (items.length > 1) {
        index = partition(items, left, right); //index returned from partition
        if (left < index - 1) { //more elements on the left side of the pivot
            quicksort2(items, left, index - 1);
        }
        if (index < right) { //more elements on the right side of the pivot
            quicksort2(items, index, right);
        }
    }
    return items;
}
function sort(items) {
  return quicksort2(items, 0, items.length-1)
}