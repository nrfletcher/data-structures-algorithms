// This function takes an array with the assumption that the array is sorted, and a value
// The function will return the index of the value, or -1 if the value is not found
// Because we can halve our searching space each iteration, binary search is logn worst case time complexity

function binarySearch(arr, val) {
    // Set our initial left pointer to the leftmost and right to the rightmost
    let left = 0;
    let right = arr.length - 1;
    
    while (left < right) {
        // Each iteration find our new mid
        // This formula gives us the same as high + low / 2 but ensures we do not encounter integer overflow
        let mid = Math.floor(left + (right - left) / 2);
        // If our current index is the item, return that index
        if (arr[mid] == val) return mid;
        // If our current item is larger, start again with our rightmost now being the original middle value
        else if (arr[mid] > val) {
            right = mid + 1;
            continue;
        // If our current item is less than value, set our leftmost to the original middle value
        } else {
            left = mid - 1;
            continue;
        }
    }
    return -1;
}

console.log(binarySearch([1, 3, 5, 7, 9, 11], 5));
