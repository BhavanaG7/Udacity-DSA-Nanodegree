'''
---------------------------------------------------------------------------------------------------------------------------------
Max and Min in a Unsorted Array
In this problem, we will look for smallest and largest integer from a list of unsorted integers. The code should run in O(n) time. Do not use Python's inbuilt functions to find min and max.

Bonus Challenge: Is it possible to find the max and min in a single traversal?
---------------------------------------------------------------------------------------------------------------------------------
'''

def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    cur_max=0
    cur_min=999
    for i in ints:
        if i<cur_min:
            cur_min=i
        elif i>cur_max:
            cur_max=i
    return (cur_min,cur_max)

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)
print(get_min_max(l))
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

#------------------------------------------------------------------------

l = [i for i in range(10, 21)]  # a list containing 10-20
random.shuffle(l)
print(get_min_max(l))
print ("Pass" if ((10, 20) == get_min_max(l)) else "Fail")

#------------------------------------------------------------------------
l = [i for i in range(30, 51)]  # a list containing 30-50
random.shuffle(l)
print(get_min_max(l))
print ("Pass" if ((30, 50) == get_min_max(l)) else "Fail")