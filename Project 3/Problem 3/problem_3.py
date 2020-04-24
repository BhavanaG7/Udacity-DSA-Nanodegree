'''
---------------------------------------------------------------------------------------------------------------------------------
Rearrange Array Elements
Rearrange Array Elements so as to form two number such that their sum is maximum. Return these two numbers. You can assume that all array elements are in the range [0, 9]. The number of digits in both the numbers cannot differ by more than 1. You're not allowed to use any sorting function that Python provides and the expected time complexity is O(nlog(n)).

for e.g. [1, 2, 3, 4, 5]

The expected answer would be [531, 42]. Another expected answer can be [542, 31]. In scenarios such as these when there are more than one possible answers, return any one.
---------------------------------------------------------------------------------------------------------------------------------
'''

class MaxHeap:
    def __init__(self,items=[]):
        super().__init__()

        #create heap list having 0th index value as 0
        self.heap_list=[0]

        for i in items:
            self.heap_list.append(i)
            self.__floatup(len(self.heap_list)-1)

    #to add element to the heap
    def push(self,value):
        #append the value to the heap and then float up the value
        #floatup(index_value)
        self.heap_list.append(value)
        self.__floatup(len(self.heap_list)-1)

    #to get the max element i.e,the root element
    def peek(self):
        if self.heap_list[1] is not None:
            return self.heap_list[1]
        else:
            return False

    def pop(self):
        #trying to pop from empty list , 1 because initial heap contains [0]
        if len(self.heap_list)<=1:
            return False

        #if heap contains only 1 element along with initial [0] i.e, [0,1] or [0,2]
        #pop it and assign it to variable max . since when we pop we always pop the maximum element
        elif len(self.heap_list)==2:
            max=self.heap_list.pop()

        #when the length is greater than 2
        #1.we swap the last and and the first root element
        #2.pop 
        #3.bubbledown the heap. i.e, rearrange the heap
        else:
            self.__swap(1,len(self.heap_list)-1)
            max=self.heap_list.pop()
            self.__bubbledown(1)

        return max

    #swap(index1,index2)
    def __swap(self,a,b):
        self.heap_list[a],self.heap_list[b]=self.heap_list[b],self.heap_list[a]
            
    def __floatup(self,index):
        #if index is 1 no floatup is required since it is the first element
        if index<=1:
            return
        else:
            parent=index//2

            if self.heap_list[parent]<self.heap_list[index]:
                self.__swap(index,parent)
                self.__floatup(parent)

    def __bubbledown(self,index):
        left=index*2
        right=index*2+1

        largest=index

        if left<len(self.heap_list) and self.heap_list[largest]<self.heap_list[left]:
            largest=left

        if right<len(self.heap_list) and self.heap_list[largest]<self.heap_list[right]:
            largest=right

        if largest!=index:
            self.__swap(index,largest)
            self.__bubbledown(largest)

    def size(self):
        return len(self.heap_list)-1

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if len(input_list)==0:
        return None

    heap_obj=MaxHeap(input_list)

    firstnum=""
    secondnum=""
    for i in range(heap_obj.size()):
        if i % 2==1:
            firstnum+=str(heap_obj.pop())
        else:
            secondnum+=str(heap_obj.pop())
    return [int(firstnum),int(secondnum)]



def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case)
test_case=[[16,28,4,5,22],[225, 28164]]
test_function(test_case)
test_case=[[4,7,2,10,15,13],[1372, 15104]]
test_function(test_case)