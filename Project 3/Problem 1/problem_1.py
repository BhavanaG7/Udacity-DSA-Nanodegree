'''
--------------------------------------------------------------------------------------------------------------------------
Finding the Square Root of an Integer
Find the square root of the integer without using any Python library. You have to find the floor value of the square root.

For example if the given number is 16, then the answer would be 4.

If the given number is 27, the answer would be 5 because sqrt(5) = 5.196 whose floor value is 5.

The expected time complexity is O(log(n))
----------------------------------------------------------------------------------------------------------------------------
'''
def sqrt(number):
    left=0
    right=number

    while left<=right:
        mid=(left+right)//2
        mid_square=mid*mid

        if mid_square==number:
            return mid
        elif mid_square<number:
            left=mid+1
        else:
            right=mid-1
    return left-1


print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
