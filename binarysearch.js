function binarySearch(arr, val) {
    let left = 0;
    let right = arr.length - 1;
    
    while (left < right) {
        let mid = Math.floor(left + (right - left) / 2);
        if (arr[mid] == val) return mid;
        else if (arr[mid] > val) {
            right = mid + 1;
            continue;
        } else {
            left = mid - 1;
            continue;
        }
    }
    return -1;
}

console.log(binarySearch([1, 3, 5, 7, 9, 11], 5));
