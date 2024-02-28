"""
While answering these questions i have taken inspiration from the lecture notes and the book.
I have also learned more about hash tables while watching some websites and youtube videos which i will link below.

Videos:

Linear Probing: https://www.youtube.com/watch?v=2BldESGZKB8
Hashing in Python: https://www.youtube.com/watch?v=i-h0CtKde6w&t=610s

Websites:
Python hashlib module: https://ioflood.com/blog/python-hashlib/


When answering each question i try to explain step by step how the code/concept works to the best of my ability.



Question 1:

I chose to make a function to show how i got my answer, meaning it returns the same indexes as the answer.
I first make a function called "hash_function" which takes in a key as a parameter.
I then make a variable called "m" and set it to 13, which is the size of the hash table explained in question 1
I then return the key modulo m, which is the hash function.

Lastly i print both of the function calls by giving the keys "27" and "130" as arguments to the function.
This prints "1" and "0" which is the indexes of the hash table for the keys "27" and "130".

Meaning my answer to this question is:

b) 1, 0


Question 2:

Q1: To answer what the "Load Factor" is i chose to make a function as well.
First i made a list called "keys" which contains the keys from the question.
Then i made a variable called "keys_amount" which stores the length of the list "keys".
I then made a variable called "m" which is the size of the hash table.

Now onto the function itself. I made a function called "check_load_factor" that takes "elements" and "size" as parameters. 
I then return the elements divided by the size. That is how the load factor is calculated.

The number of items/elements divided by the number of slots/size of the hash table is how we get the load factor.
Lastly i print the function call with the arguments "keys_amount" and "m" and rounded the answer to 2 decimal places.
I used the "round()" function to do this.

Meaning my answer to this question is:

The Load Factor after all the keys have been inserted is 9/11 = 0.82



Q2: Here is how i would find out which of the following options represents the contents of the hash table after being insterted with "Linear Probing"


I first make a list called "hash_table" which contains "None" times the size of the hash table. Basically 11 "None" values.

I then make a function called "hash_function_new" that contains the same hash function as in question 1.
I just need to modify the size of the hash table to "11", because that is the size of the hash table in this question.

I then make a function called "linear_probing" which takes in "key" and "hash_table" as parameters.
I then make a variable called "index" and set it to the hash function with the key as an argument.

I then make a while loop that runs as long as the hash table at the index is not "None". It moves on to the next if the slot is taken.
The probe sequence is then calculated by adding 1 to the index and then taking the modulo of the size of the hash table.
It goes through the hash table and finds the next available slot to insert the key.
The index is then returned. 

Lastly i make a for loop that goes through the keys and inserts them into the hash table using the linear probing function.
I then print the hash table.


Meaning my answer to this question is:

D) [11, 12, None, 14, 25, None, 17, 18, 19, 20, 21]



Question 3:

Here is how i went about creating the "Hashclass". 
I first made a class called "Hashclass" that takes "id_num" as a parameter.
I then created the constructor "__init__" which takes "id_num" as a parameter/attribute.
I then made another attribute called "hash_num" and set it to "None".

I then made a function called "hash_it" which takes no parameters.
It stores a random integer between 1 and 1000 in the variable called "salt".
I imported the random module to use the "randint()" method.
I then made a variable called "id_and_salt" and set it to the "id_num" plus the "salt", made into a string and encoded it.
The encode() method is used to convert the string into bytes to be acceptable by "sha1" hahs algorithm im using
Lastly i hash the "id_and_salt" bytes using the "sha1" algorithm and use the hexdigest() method to get the hexadecimal representation of the hash.
I then store the hash in the "hash_num" attribute that i created earlier.

I then made a function called "print_it" which takes no parameters.
It simply prints the "hash_num" attribute storing the hash.


Question 4:

Here is how i went about creating the function to find the most frequent integer in the list using a dictionary.

I first made a list called "integer_list" which contains the integers from the question.

Then i made a function called "most_frequent_integer" which takes "integer_list" as a parameter.
I then made a dictionary called "frequency" which is empty.
I made a for loop that iterates through the "integer_list".
Inside the for loop is a if statement that checks if the number is a key in the dictionary.
If it is the frequency of the number is increased by 1.
If it is not a new key value pair is created with the number as the key and 1 as the value.
Then i find the key with the highest value/frequency by using the "max()" function.
The get() method is used to get the value of the key.
I then return the key with the highest frequency.

Lastly i print the function call with the "integer_list" as an argument.
And the most frequent integer seems to be "5"









"""
import hashlib #Imported for Question 3
import random #Imported for Question 3


#Question 1
def hash_function(key): #Hash function
    m = 13
    return key % m

print(hash_function(27))
print(hash_function(130))


#Question 2 (Q1)

keys = [11, 12, 14, 17, 18, 19, 20, 21, 25]
keys_amount = len(keys)

m = 11


def check_load_factor(elements, size): #Function to check the load factor

    return elements/size

print(round(check_load_factor(keys_amount, m), 2)) #Rounded the answer to 2 decimal places


#Question 2 (Q2)

hash_table = [None] * m


def hash_function_new(key): #Hash function
    m = 11 #Modified the size
    return key % m


def linear_probing(key, hash_table):
    index = hash_function_new(key)
    while hash_table[index] is not None:
        index = (index + 1) % m
    return index



for key in keys:
    index = linear_probing(key, hash_table)
    hash_table[index] = key

print(hash_table)


#Question 3

class HashClass:
    def __init__(self, id_num):
        self.id_num = id_num
        self.hash_num = None


    def hash_it(self):
        salt = random.randint(1, 1000)
        id_and_salt = str(self.id_num + salt).encode()
        self.hash_num = hashlib.sha1(id_and_salt).hexdigest()


    def print_it(self):
        print(self.hash_num)


    


my_hash = HashClass(11011999) #Creates instance of the class

my_hash.hash_it() #Uses the hash_it method to hash the id number

my_hash.print_it() #Prints it


#Question 4


integer_list = [10, 2, 5, 2, 0, 5, 6, 8, 5, 10]



def most_frequent_integer(integer_list):
    frequency = {} 
    for num in integer_list:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    most_frequent = max(frequency, key=frequency.get)

    return most_frequent


result = most_frequent_integer(integer_list)

print(result) #Prints the most frequent integer in the list



    

    

