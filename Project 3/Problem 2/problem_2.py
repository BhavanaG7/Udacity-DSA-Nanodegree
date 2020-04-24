'''
---------------------------------------------------------------------------------------------------------------------------------
Search in a Rotated Sorted Array
You are given a sorted array which is rotated at some random pivot point.

Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]

You are given a target value to search. If found in the array return its index, otherwise return -1.

You can assume there are no duplicates in the array and your algorithm's runtime complexity must be in the order of O(log n).
---------------------------------------------------------------------------------------------------------------------------------
'''

def rotated_array_search(nums, target):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    i = 0
    j = len(nums) - 1

    while i <= j:
        m = (i + j) // 2
            
        beg = nums[i]
        mid = nums[m]
        end = nums[j]
            
        if target == mid:
            return m
            
        elif beg <= target < mid:
            # Left ascending and target in left
            j = m - 1
                
        elif mid < target <= end:
            # Right ascending and target in right
            i = m + 1
                
        elif beg <= mid:
        # Left ascending but target in right
            i = m + 1
                
        elif mid <= end:
            # Right ascending but target in left
            j = m - 1
        
    return -1

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])