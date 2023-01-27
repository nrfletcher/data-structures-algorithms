#include <stdio.h>
#include <string.h>

int main()
{
    char nums[] = {1, 3, 5, 7, 9, 11, 33, 78, 99, 105};
    printf("Found at index: %d \n", binary_search(nums, 5, sizeof(nums)));
    return -1;
}

int binary_search(char nums[], int target, int len)
{
    int low, high, mid;

    low = 0;
    high = len - 1;

    while (low <= high)
    {
        mid = high - (high + low) / 2;
        if (target < nums[mid])
            high = mid - 1;
        else if (target > nums[mid])
            low = mid + 1;
        else
            return mid;
    }
    return -1;
}
