"""
I have taken inspiration from the lecture notes, the book and some videos on youtube.
For the selection sort algorithm I have used the following video from "Amigoscode":
(https://www.youtube.com/watch?v=kZH0vWXs_Bk)
For the bubble sort algorithm I have used the following video from "Real Python":
(https://www.youtube.com/watch?v=KLvH6yi5YYU)





Question 1:

After 3 passes of selection sort the list: [1502, 1560, 1600, 1540, 100, 1660, 1700, 2024]
Will look like this: [100, 1502, 1540, 1560, 1600, 1660, 1700, 2024]

I have implemented a selection sort algorithm in the function "selection_sort".
It takes a list as input and returns the sorted list.
The algorithm works by iterating through the list and finding the minimum value.
It then swaps the minimum value with the current index and continues until the list is sorted.

Question 2
After 3 passes of bubble sort the list: [400, 10, 210, 160, 70, 220, 280, 380, 180, 260, 540]
Will look like this: [10, 70, 160, 180, 210, 220, 260, 280, 380, 400, 540]

I have implemented a bubble sort algorithm in the function "bubble_sort".
It takes a list as input and returns the sorted list.
The algorithm works by iterating through the list and comparing adjacent elements.
If the element to the left is greater than the element to the right, it swaps them and continues until the list is sorted.


Question 3: 
I have implemented a function called "sort_and_rem_dup".
This function takes a list as input and returns the sorted list with duplicates removed.
The function first sorts the list using the selection sort algorithm.
Then it iterates through the list and removes any duplicates.
The function then returns the sorted list with duplicates removed.

So in summary it does the selection sort, checks for duplicates by iterating through the list and deletes if it is the same one.
And it does not use any built-in functions or the "set" data type.

Question 4:
I have implemented a function called "check_palindrome".
This function takes a word as input and checks if it is a palindrome.
The function first creates a stack and a queue from the word.
It then iterates through the stack and queue and checks if the word is a palindrome.
If the word is a palindrome, it prints that the word is a palindrome.
If the word is not a palindrome, it prints that the word is not a palindrome.

Note: I used a list to simulate the behavior of a stack and a queue.




"""

#Question 1
def selection_sort(list):
    for i in range(3): #Makes 3 passes instead of the entire list
        min_index = i
        for j in range(i+1, len(list)):
            if list[min_index] > list[j]:
                min_index = j
        list[i], list[min_index] = list[min_index], list[i]
    return list


list1 = [1502, 1560, 1600, 1540, 100, 1660, 1700, 2024]
print(selection_sort(list1))







#Question 2
def bubble_sort(list):
    for i in range(3): #Makes 3 passes instead of the entire list
        for j in range(len(list)-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list


list2 = [400, 10, 210, 160, 70, 220, 280, 380, 180, 260, 540]
print(bubble_sort(list2)) 


#Question 3
def sort_and_rem_dup(list):
    # Selection sort
    for i in range(len(list)):
        min_index = i
        for j in range(i+1, len(list)):
            if list[min_index] > list[j]:
                min_index = j
        list[i], list[min_index] = list[min_index], list[i]


    # Remove duplicates
    i = 0
    while i < len(list)-1:
        if list[i] == list[i+1]:
            del list[i]
        else:
            i += 1

    return list


my_list = [5, 4, 3, 2, 1, 2, 3, 4, 5]

print(sort_and_rem_dup(my_list))

#Question 4



def check_palindrome(word):
    # Creates a stack and a queue
    stack = list(word)
    queue = list(word)

    # Checks if the word is a palindrome
    while stack:
        if stack.pop() != queue.pop(0):
            print(f"{word} is not a palindrome.")
            return
    print(f"{word} is a palindrome.")


check_palindrome("racecar")