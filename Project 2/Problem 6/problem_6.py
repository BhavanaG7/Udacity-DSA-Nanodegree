'''
--------------------------------------------------------------------------------------------------------------------------
Union and Intersection of Two Linked Lists
Your task for this problem is to fill out the union and intersection functions. The union of two sets A and B is the set of elements which are in A, in B, or in both A and B. The intersection of two sets A and B, denoted by A ∩ B, is the set of all objects that are members of both the sets A and B.

You will take in two linked lists and return a linked list that is composed of either the union or intersection, respectively. Once you have completed the problem you will create your own test cases and perform your own run time analysis on the code.

We have provided a code template below, you are not required to use it:
----------------------------------------------------------------------------------------------------------------------------
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        out_string+="NULL"
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    # Your Solution Here
    head1=llist_1.head
    head2=llist_2.head

    union_list=LinkedList()
    all_val=set()

    if head1 is None and head2 is None:
        return union_list

    while head1 is not None:
        val=head1.value
        all_val.add(val)
        head1=head1.next

    while head2 is not None:
        val=head2.value
        all_val.add(val)
        head2=head2.next

    union_head=union_list.head

    for val in all_val:
        if union_head is None:
            union_list.append(val)
            union_head=union_list.head
        else:
            union_head.next=Node(val)
            union_head=union_head.next

    union_head.next=None
    return union_list

def intersection(llist_1, llist_2):
    # Your Solution Here
    head1=llist_1.head
    head2=llist_2.head

    intersection_list=LinkedList()
    value1=set()
    value2=set()

    if head1 is None and head2 is None:
        return intersection_list

    while head1 is not None:
        val=head1.value
        value1.add(val)
        head1=head1.next

    while head2 is not None:
        val=head2.value
        value2.add(val)
        head2=head2.next

    head3=intersection_list.head

    for val in value1:
        if val in value2:
            if head3 is None:
                intersection_list.append(val)
                head3=intersection_list.head
            else:
                head3.next=Node(val)
                head3=head3.next

    if head3 is not None:
        head3.next=None
    return intersection_list

#edge case
#if two lists are empty
print("Both list are empty")
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

print(f"linked_list_1 : {linked_list_1}")
print(f"linked_list_2 : {linked_list_2}")
print (f"Union : {union(linked_list_1,linked_list_2)}")
print (f"Intersection : {intersection(linked_list_1,linked_list_2)}")

print("---------------------------------------------------------------------------------")

#edge case
print("One of list is empty")
linked_list_7 = LinkedList()
linked_list_8 = LinkedList()

element_7 = [3,2,4,35,6,65,6,4,3,21]
for i in element_7:
    linked_list_7.append(i)

print(f"linked_list_1 : {linked_list_7}")
print(f"linked_list_2 : {linked_list_8}")
print (f"Union : {union(linked_list_7,linked_list_8)}")
print (f"Intersection : {intersection(linked_list_7,linked_list_8)}")
print("---------------------------------------------------------------------------------")
# Test case 1
print("list1 and list2 have some elements in common")
linked_list_11 = LinkedList()
linked_list_12 = LinkedList()

element_11 = [3,2,4,35,6,65,6,4,3,21]
element_12 = [6,32,4,9,6,1,11,21,1]

for i in element_11:
    linked_list_11.append(i)

for i in element_12:
    linked_list_12.append(i)

print(f"linked_list_1 : {linked_list_11}")
print(f"linked_list_2 : {linked_list_12}")
print (f"Union : {union(linked_list_11,linked_list_12)}")
print (f"Intersection : {intersection(linked_list_11,linked_list_12)}")
print("---------------------------------------------------------------------------------")

# Test case 2
print("Both list contains unique element i.e, no similar elements in both the list")
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print(f"linked_list_1 : {linked_list_3}")
print(f"linked_list_2 : {linked_list_4}")
print (f"Union : {union(linked_list_3,linked_list_4)}")
print (f"Intersection : {intersection(linked_list_3,linked_list_4)}")
print("---------------------------------------------------------------------------------")
