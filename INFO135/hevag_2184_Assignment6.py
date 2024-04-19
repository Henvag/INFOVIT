"""
#Question 1

The sequence that determines the order in which the elements would be accessed during a Pre-order traversal of the tree is:

a) A B D G H E I C F J

Pre-order traversal visits the root node first, then recursively visits the left subtree and finally recursively visits the right subtree.

#Question 2
I tried visualizing the knapsack problem by making a table in excel.



So first we start off by making the class "QuizGift".
The class will have the following methods "compute_result" and "print_result".

The constructor will have the following attributes:
"questions" where each question is represented as a tuple with points and time.
"gifts" where each gift is represented as a tuple with points and gift.
I used float('inf') to represent infinity.

Next in the "compute_result" sets the time limit to 100
I created an array "dp" (dynamic programming) with the size "time_limit + 1"
Each element is supposed to represent the maximum points that can be obtained in the given time, from 0 to "time_limit".
We then iterate over every question. For each question we update dp[t] for all t from time_limit down to time.
Our new value is the maximum of the old value of dp[t] and dp[t - time] + points. 
This represents the maximum points that can be obtained from answering the qeustion.

Now that we have gone through all the questions, the maximum points that can be obtained is the maximum value in dp.
We then find the gift that corresponds to the points obtained. 


Finally we simply print the maximum points and the gift that Sara will receive.
And run the instance of the class.

#Question 3

a) I make the class "Square" and set "side_square" as a instance variable/attribute
I then make the compute method, which calculates the area of the square.
Then the value of the area is printed.

b) I make the class "Circle" and set "radius_circle" as a instance variable/attribute
I then make the compute method, which calculates the area of the circle.
Then the value of the area is printed.

c) b) I make the class "Triangle" and set "side1", "side2" and "side3" as a instance variables/attributes
I then make the compute method, which calculates the area of the traingle.
Then the value of the area is printed.



#Question 4


I make the class "House" and set the class variable "count" to 0.
This is so the variable is shared among all instances of the class.
Next we have the constructor with the attributes "owner", "condition" and "price".
And the house count is incremeneted by 1.

I then make the method "sell" which takes in the new owner of the house.
The owner is then changed to the new owner, the status of sold is changed to True.
Then the profit is calculated and printed.

I then make the method "change_price" which takes in the new price of the house.
If the house is sold, it prints "House has been sold".
Otherwise the price of the house is changed to the new price.

I then make the method 'renovate' which takes in the renovation expense and the new condition of the house.
The cost of the house is updated by adding the renovation expense to the current cost, and the condition of the house is updated to the new condition.
Then it prints "House renovated!".

I then make a method that prints the info of the house such as owner, condition and price.

Then we create two objects or instances of the class. Called "house1" and "house2".

We start off by printing the initial information of both houses.
We then renovate house1 by calling the method "renovate".
Then we sell house1 by calling the method "sell".
Then we print the updated information of house1.

Lastly the total number of houses is printed.

"""


#Question 2

class QuizGift:
    def __init__(self):
        self.questions = [(120, 15), (200, 20), (150, 40), (350, 50), (100, 20), (90, 10)]
        self.gifts = [(250, "watch"), (750, "smartphone"), (float('inf'), "laptop")]

    def compute_result(self):
        time_limit = 100
        dp = [0] * (time_limit + 1)
        for points, time in self.questions:
            for t in range(time_limit, time - 1, -1):
                dp[t] = max(dp[t], dp[t - time] + points)
        self.max_points = max(dp)
        self.gift = next(gift for points, gift in self.gifts if self.max_points < points)

    def print_result(self):
        print(f"The maximum number of points Sara can obtain is {self.max_points}.")
        print(f"The gift that Sara will receive is a {self.gift}.")



quiz_gift = QuizGift()
quiz_gift.compute_result()
quiz_gift.print_result()



#Question 3

#a)
class Square:
    def __init__(self, side_square):
        self.side = side_square


    def compute_area(self):
        self.area = self.side * self.side #Area of the square
        print(self.area)
    


#b)
class Circle:
    def __init__(self, radius_circle):
        self.radius = radius_circle


    def compute_area(self): #Area of the circle
        self.area = 3.14 * self.radius * self.radius
        print (self.area)
        

#c)
class Triangle:

    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

        

    def compute_area(self):
        self.area = self.side1 * self.side2 * self.side3 / 2
        print(self.area)




my_square = Square(2)
my_circle = Circle(2)
my_triangle = Triangle(5, 4, 3)


print('Area of square:', end=' ')
my_square.compute_area()

print('Area of circle:', end=' ')
my_circle.compute_area()

print('Area of triangle:', end=' ') 
my_triangle.compute_area()



#Question 4


class House:

    count = 0 #initial count of the houses

    def __init__(self,owner, condition, price):
        self.owner = owner
        self.condition = condition
        self.price = price
        self.cost = 0 #initial cost of the house
        self.sold = False #initially the house is not sold
        House.count += 1


    def sell(self, new_owner):
        self.owner = new_owner #change the owner of the house
        self.sold = True #change the status of the house to sold
        profit = self.price - self.cost #calculate the profit
        print(profit) #print the profit


    def change_price(self, new_price):
        if self.sold:
            print("House has been sold")
            
        else:
            self.price = new_price  # change the price of the house


    def renovate(self, expense, new_condition):
        self.cost += expense #updates the cost of the house
        self.condition = new_condition #updates the condition of the house
        print("House renovated!") #prints that the house has been renovated

    
    def print_info(self):
        print(f"Owner: {self.owner}")
        print(f"Condition: {self.condition}")
        print(f"Price: ${self.price}")



house1 = House("John", "Good", 100000)
house2 = House("Sara", "Bad", 250000)

#Print initial information for both houses
house1.print_info()
house2.print_info()

#Renovate house1
house1.renovate(50000, "Great")

#Sell house1
house1.sell("Leo")

#Print updated information for house1
house1.print_info()

#Print total number of houses
print(f"Total number of houses: {House.count}")
    
            
        
        
        
 
