"""
To solve these questions i have read the lecture notes and the corresponding chapters in the book.

Question 1:

(I imported the math library to show the answer with code)

a) For the Italian dictionary it would take O(log2 102400) = 16.64
If we round up we get 17. So it would take 17 tries to find the word in the worst case.


b) For the French dictionary it would take O(log2 480000) = 18.87
If we round up we get 19. So it would take 19 tries to find the word in the worst case.


Question 2:

"""
import math

#Question 1 a)
print(math.log2(102400))

#Question 1 b)
print(math.log2(480000))

#Question 2

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None


    def print_list(self):
         node = self.head
         while node is not None:
             print(node.data)
             node = node.next
            








