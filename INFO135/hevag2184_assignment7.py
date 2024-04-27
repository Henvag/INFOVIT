"""
Question1:

The big O notation of the function is O(n^3).
This is because it is the one that grows the fastest when "n" increases out of the options.
Therefore it is the worst case scenario.


Question2:

Since the outer loop runs "n" times and the inner loop runs "log n" times we can say that the big O notation is O(n log n).
The reason the outer loop runs "n" times because it is the size of the input.
The reason the inner loop runs "log n" times is because the counter is multiplied by 2 each time the loop runs.
Therefore giving it a logarithmic time complexity.


Question 3:

The big O notation of this function is O(n^2).
The reason for this is because it has two nested loops where the worst case is "n" times each.
Therefore giving it a quadratic time complexity.


Question 4:
The time complexity of this function is O(n).
This is because the input is a list that has a length of "n".

So in the function S[i] is supposed to represent the daily usage of the website on day i.
A[i] is supposed to represent the average daily usage of the website up to and including day i.

A[i] is calculated by summing the usage for all days up to and including day i and dividing by i + 1.
Lastly the result is appended to the list A and returned.

"""

#Question 4
def solve_problem(S):
    A = []
    total_usage = 0
    for i in range(len(S)):
        total_usage += S[i]
        average_usage = total_usage / (i + 1)
        A.append(average_usage)
    return A