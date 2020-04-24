'''
--------------------------------------------------------------------------------------------------------------------------
Least Recently Used Cache
We have briefly discussed caching as part of a practice problem while studying hash maps.

The lookup operation (i.e., get()) and put() / set() is supposed to be fast for a cache memory.

While doing the get() operation, if the entry is found in the cache, it is known as a cache hit. If, however, the entry is not found, it is known as a cache miss.

When designing a cache, we also place an upper bound on the size of the cache. If the cache is full and we want to add a new entry to the cache, we use some criteria to remove an element. After removing an element, we use the put() operation to insert the new element. The remove operation should also be fast.

For our first problem, the goal will be to design a data structure known as a Least Recently Used (LRU) cache. An LRU cache is a type of cache in which we remove the least recently used entry when the cache memory reaches its limit. For the current problem, consider both get and set operations as an use operation.

Your job is to use an appropriate data structure(s) to implement the cache.

In case of a cache hit, your get() operation should return the appropriate value.
In case of a cache miss, your get() should return -1.
While putting an element in the cache, your put() / set() operation must insert the element. If the cache is full, you must write code that removes the least recently used entry first and then insert the element.
All operations must take O(1) time.

For the current problem, you can consider the size of cache = 5.

Here is some boiler plate code and some example test cases to get you started on this problem:
----------------------------------------------------------------------------------------------------------------------------
'''
from collections import OrderedDict
#advantage of using OrderedDict is that it maintains the order in which values are inserted
class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.cache=OrderedDict()
        self.capacity=capacity

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if self.cache is not None and key in self.cache:
            #pop value
            value=self.cache.pop(key)
            #add back
            self.cache[key]=value
            #return Value
            return value
        else:
            return -1


    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        
        if self.capacity==0:
            print("Can't set the value because capacity is 0")
            return

        if key in self.cache:
            #if key is present then pop it and add new value
            self.cache.pop(key)
            self.cache[key]=value

        #key not present
        else:
            #if cache has space left
            if len(self.cache)<self.capacity:
                self.cache[key]=value
            
            #if we dont have space
            else:
                self.cache.popitem(last=False)
                self.cache[key]=value

our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

print(our_cache.get(1))      # returns 1
print(our_cache.get(2))      # returns 2
print(our_cache.get(9))     # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

print(our_cache.get(3))    # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

#Edge Case
print("Edge Case 1:")
print("when capacity is Zero")

our_cache=LRU_Cache(0)
our_cache.set(10,20)
print(our_cache.get(10))

print("------------------------------------------------------------------------")
print("Edge Case 2:")
print("when we insert the value to exsisting key-value pair")

our_cache=LRU_Cache(2)
our_cache.set(1,10)
print(f"before :{our_cache.get(1)}")
our_cache.set(2,20)
our_cache.set(1,100)

print(f"after :{our_cache.get(1)}")
print(our_cache.get(2))
