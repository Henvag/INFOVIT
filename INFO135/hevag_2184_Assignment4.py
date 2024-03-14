"""
Task 1:

Given the Graph in the task i have concluded that the following set represents the "Edge set" of the graph:

d): { (v0,v1), (v1,v2), (v2,v3), (v3,v4), (v4,v0), (v0,v5), (v5,v4), (v3,v5), (v5,v2) }

I used this website to help me visualize the graph:
https://csacademy.com/app/graph_editor/

I simply compared the edges to the graph in the task and saw where they pointed to.

Task 2:

The shortest path from vertex A to vertex E according do "Dijikstra's Algorithm" is:

1) Shortest Path: A -> C -> D -> E, Distance: 19

Now let me explain how i got this answer. We first start at vertex A, where the distance to "B" is 7 and to "C" it's 13.
So we choose "B" which is the shortest path. Now we are at vertex "B" and the distance to "D" is 9 and to C it's 15.
Adding these to the path from A to B we get a distance of 16 with (A -> B -> D) and 22 with (A -> B -> C).
The shortest path to "C" is therefore still via "A" directly, so we update the shortest path to "D"
Now we are at vertex "C" which is connected to "D" with a weight of 1 and "E" with a weight of 11.
Adding these to the path from A to C we get a distance of 14 with (A -> C -> D) and 24 with (A -> C -> E)
We update the shortest path to "D". Now we are at vertex "D" which is connected to "E" with a weight of 5.
Adding this to the path from A to D we get a distance of 19 with (A -> C -> D -> E). This is the shortest path to "E"
Lastly we visit vertex "E" and we are done since there are no more connections.

So we ended up with the shortest path having a distance of 19 from A to E.

I still used the same website to visualize the graph and to help me calculate the shortest path:
https://csacademy.com/app/graph_editor/


Task 3:
I used the examples from the lecture 4 to fill out the "examine", "attacks" and "extend" functions.

When implementing the "is_solution" function we have to check if any of the two queens are attacking each other.
They attack each other if they are on the same row, column or diagonal according to the rules of chess.

So the function iterates through each queen on our chessboard with the candidate_solution. 
For each queen "i" it checks if any of the other queens "j" are attacking it.
The attack function is the one that checks if the queens are attacking each other.
If they are attacking each other it returns "Invalid!" and if they are not attacking each other it returns "Valid!".


#Task 4:

I have created a method that recieves a vertex as paramater and removes edges connected to that vertex

The method "remove_vertex" checks if the vertex is in the graph, if it is the vertex gets removed from the graph.
Then it iterates over all of the other vertices in the graph. 
Then it checks if the vertex being removed is in the list of edges for the current vertex.
If it is, that means there is an edge from the current vertex to the vertex being removed.
Lastly the edge from the current vertex to the vertex being removed gets removed. This means there will no longer be an edge from "other_vertex" to "vertex".





"""


#Task 3

COLUMNS = "abcde"
NUM_QUEENS = len(COLUMNS)
ACCEPT = 1
CONTINUE = 2
ABANDON = 3
all_solutions = []


def solve(partial_sol):
    exam = examine(partial_sol)
    if exam == ACCEPT:
        all_solutions.append(partial_sol)
    elif exam != ABANDON:
        for p in extend(partial_sol):
            solve(p)
    return all_solutions



def examine(partial_sol):
    for i in range(len(partial_sol)):
        for j in range(i + 1, len(partial_sol)):
            if attacks(partial_sol[i],
                        partial_sol[j]):
                return ABANDON
    if len(partial_sol) == NUM_QUEENS:
        return ACCEPT
    else:
        return CONTINUE
    


def attacks(p1, p2):
    column1 = COLUMNS.index(p1[0]) + 1
    row1 = int(p1[1])
    
    column2 = COLUMNS.index(p2[0]) + 1
    row2 = int(p2[1])
    
    return (row1 == row2 or
            column1 == column2 or
            abs(row1-row2) == abs(column1-column2))


def extend(partial_sol):
    results = []
    row = len(partial_sol) + 1
    for column in COLUMNS:
        new_solution = list(partial_sol)
        new_solution.append(column + str(row))
        results.append(new_solution)

    return results

def is_solution(candidate_solution): #The new function
    for i in range(NUM_QUEENS):
        for j in range(i + 1, NUM_QUEENS):
            if attacks(candidate_solution[i], candidate_solution[j]):
                return "Invalid!"
    return "Valid!"




candidate_solution1 = ['d3', 'c1', 'e5', 'b4', 'a2']
candidate_solution2 = ['e4', 'a1', 'c5', 'd2', 'b1']


result1 = is_solution(candidate_solution1)
result2 = is_solution(candidate_solution2)

print("Candidate Solution 1:", result1)
print("Candidate Solution 2:", result2)



#Task 4


class Graph:
    def __init__(self):
        self.graph = {}
 
    def add_vertex(self, vertex):
        if vertex not in self.graph:
           self.graph[vertex] = []
 
    def add_edge(self, from_vertex, to_vertex):
        if from_vertex not in self.graph:
            self.graph[from_vertex] = []
        if to_vertex not in self.graph:
            self.add_vertex(to_vertex)
        self.graph[from_vertex].append(to_vertex)
 
    def print_graph(self):
        for vertex, edges in self.graph.items():
            print(vertex + ": " + str(edges))
 
    def remove_vertex(self, vertex): #New method

        if vertex in self.graph:
            del self.graph[vertex] #Vertex gets removed

        for other_vertex, edges in self.graph.items(): #All of the edges from other vertices to this vertex gets removed
            if vertex in edges:
                edges.remove(vertex)
        
    




graph = Graph()
graph.add_edge('a', 'b')
graph.add_edge('a', 'c')
graph.add_edge('b', 'c')
graph.add_edge('b', 'd')
graph.add_edge('c', 'd')
graph.add_edge('d', 'e')

print("Before removal of vertex:")

graph.print_graph()

graph.remove_vertex('a')

print("After removal of vertex:")

graph.print_graph()