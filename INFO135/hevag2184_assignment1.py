"""
To solve these questions i have read the lecture notes and the corresponding chapters in the book.
I also watched some videos to get a better understanding.
Videos on linked-lists: (https://www.youtube.com/watch?v=JlMyYuY1aXU&t=246s) and (https://www.youtube.com/watch?v=F8AbOfQwl1c)
Videos on stacks: (https://www.youtube.com/watch?v=O1KeXo8lE8A)

Question 1:

(I imported the math library to show the answer with code)

a) For the Italian dictionary it would take O(log2 102400) = 16.64
If we round up we get 17. So it would take 17 tries to find the word in the worst case.


b) For the French dictionary it would take O(log2 480000) = 18.87
If we round up we get 19. So it would take 19 tries to find the word in the worst case.


Question 2:
First the node class is created. It has two attributes, "data" storing the data for the node and "next" being the pointer to the next node.
Then the linked list class is created. It has one attribute, "head" that is pointing to the first node in the list.

The print_list method is created in the linked list class. It starts from the head and prints the data of each node until it reaches the end of the list, a node that points to None.

Lastly, three nodes are created and the linked list is created. The head is pointing to the first node and the first node is pointing to the second node and so on.
The print_list method is called to print the data of each node in the list, displaying the letters A, B and C.


Question 3:

For this question i have used the stack class from the lecture notes as my starting point.

First the stack class is created. It has one attribute, "items" that is an empty list.

The is_empty method is created. It checks if the length of the list is 0. If it is, it returns True, if not it returns False.
The push method is created. It takes an item as a parameter and appends it to the list.
The pop method is created. It checks if the list is empty, returning None if empty or uses the pop method removing the last item in the list and returns it.
The peek method is created- It essentially does the same as the pop method but it does not remove the item from the list, allowing us to see the last item in the list.
The size method is created. It returns the length of the list.

Lastly, the reverse_list method is created. It takes a list as a parameter. A stack is created. A for loop is used to push each item in the list to the stack.
Then a while loop is used to pop each item from the stack and print it. This will print the list in reverse order.




"""
import math

#Question 1 a)
print(math.log2(102400))

#Question 1 b)
print(math.log2(480000))

#Question 2

class Node: #Data and pointer to next node
    def __init__(self, data):
        self.data = data
        self.next = None




    
class LinkedList: #Linked list class
    def __init__(self):
        self.head = None


    def print_list(self): #Node/element printing method
         node = self.head
         while node is not None:
             print(node.data)
             node = node.next



node1 = Node("A")
node2 = Node("B")
node3 = Node("C")

list_letters = LinkedList()
list_letters.head = node1
node1.next = node2
node2.next = node3

list_letters.print_list()

             
            
#Question 3

class Stack: #Stack class
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    

    def push(self, item):
        self.items.append(item)


    def pop(self):
        if self.is_empty():
            return None
        
        return self.items.pop()
    

    def peek(self):
        if self.is_empty():
            return None
        
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    





def reverse_list(list):
    stack = Stack()
    for item in list:
        stack.push(item)
    while not stack.is_empty():
        print(stack.pop())





my_list = [1, 2, 3, 4, 5]


reverse_list(my_list)
