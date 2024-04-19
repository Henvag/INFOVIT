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

"""


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