"""
I used this website to help me visualize the graphs better:
https://csacademy.com/app/graph_editor/

This one i used with adjacency matrix:
https://visualgo.net/en/graphds



Question 1:

Out of these binary trees the ones that are considered full binary trees are:

Binary Tree 1, Binary Tree 2 and Binary Tree 3

They are a full binary tree because all the nodes have either 0 or 2 children.
Each interior node has 2 children and each leaf node has 0 children.

So this means all the binary trees provided here have the requirements for a full binary tree.

Question 2:

To answer this question i first made my own adjecency matrix from the graph.
I did this by simply checking which nodes connected to each other.
If they did i put a 1 in the matrix, if they didn't i put a 0.
This is a pointed graph so you can see the direction of the edges and you need to take that into account.

I then compared the adjacency matrix to the ones provided in the question.
The one that matched was the second (ii) adjacency matrix.

When i plotted the data into my visualzation tool it looks the same.


Question 3:

This was an implementation of a binary tree using lists of lists.
To create the binary tree as shown in the question i did the following:

I created the root of the tree with the value "1".
I then inserted the left child with the value "2" and the right child with the value "3".
I then inserted the left child of the left child with the value "4".
I then inserted the left child of the right child with the value "5" and the right child with the value "6".

This created the binary tree as shown in the question. All of this was stored in the function make_tree().


Question 4:
I created a graph using the implementation of the graph class and "DFS" and stored it in the function build_my_graph2().
It connects the nodes 'a', 'b', 'c', 'd' and 'e' in a pointed graph as shown in the question.
I then ran the depth first search on the graph starting from the node 'b'.
The result was the nodes visited in the order they were visited.


Question 5:
This was an implementation of a binary search tree.
I created the two new methods compute_sum() and compute_count().

The compute_sum() method computes the sum of all the node values in the binary search tree.
It checks if the tree is empty and if it is it returns 0.
If it is not empty it returns the sum of the value of the current node and the sums of the left and right subtrees.

The compute_count() method computes the total number of nodes in the binary search tree.
It checks if the tree is empty and if it is it returns 0.
If it is not empty it returns 1 and the count of the left and right subtrees.

We then get the result of the sum and the count when creating an instance of it.
"""

#Question3

def binary_tree(r): #Root
    return [r, [], []]

def get_left_child(root): #Left child
    return root[1]

def get_right_child(root): #Right child
    return root[2]


def insert_left_child(root, new_branch): #Inserts left child
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [new_branch, t, []])
    else:
        root.insert(1, [new_branch, [], []])
    return root

def insert_right_child(root, new_branch): #Inserts right child
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [new_branch, [], t])
    else:
        root.insert(2, [new_branch, [], []])
    return root


def make_tree(): #Makes the tree
    my_tree = binary_tree('1')

    insert_left_child(my_tree, '2')
    insert_right_child(my_tree, '3')

    insert_left_child(get_left_child(my_tree), '4')
    insert_left_child(get_right_child(my_tree), '5')
    insert_right_child(get_right_child(my_tree), '6')

    return my_tree

print(make_tree())

#Question 4


class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, from_vertex, to_vertex):
        if from_vertex not in self.graph:
            self.graph[from_vertex] = []
        self.graph[from_vertex].append(to_vertex)
        if to_vertex not in self.graph:
            self.add_vertex(to_vertex)

    def get_vertices(self):
        return list(self.graph.keys())
    
    def get_adjacency(self, vertex):
        return self.graph.get(vertex, [])
    
    def get_vertex(self, vertex_key):
        return self.graph.get(vertex_key, None)
    
    def __contains__(self, vertex):
        return vertex in self.graph
    
    def print_graph(self):
        for vertex, edges in self.graph.items():
            print(vertex + ": " + str(edges))

    def dfs(self, start):
        visited = []
        stack = [start]

        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.append(vertex)
                for x in self.graph.get(vertex, []):
                    if x not in visited:
                        stack.append(x)

        return visited





        
                
           



    
    def build_my_graph2(self): #Creates the graph and runs depth first search
        graph = Graph()
        graph.add_edge('b', 'a')
        graph.add_edge('a', 'c')
        graph.add_edge('c', 'b')
        graph.add_edge('a', 'd')
        graph.add_edge('d', 'e')
        graph.add_edge('e', 'a')

        graph.print_graph() #Prints the graph

        visited = graph.dfs('b') 
        print(visited) #Prints the nodes visited in the order they were visited

      


graph = Graph()
graph.build_my_graph2()



#Question 5

class BinarySearchTree:
    def __init__(self, value=None):
        self.value = value
        if self.value is not None:
            self.left_child = BinarySearchTree()
            self.right_child = BinarySearchTree()

        else:
            self.left_child = None
            self.right_child = None

    def is_empty(self):
        return self.value is None
    
    def insert(self, value):
        if self.is_empty():
            self.value = value
            self.left_child = BinarySearchTree()
            self.right_child = BinarySearchTree()

        elif value < self.value:
            self.left_child.insert(value)
        elif value > self.value:
            self.right_child.insert(value)

    def in_order(self):
        if self.is_empty():
            return []
        else:
            return self.left_child.in_order() + [self.value] + self.right_child.in_order()
        
    def print_tree(self):
        if not self.is_empty():
            print(self.in_order())

    def compute_sum(self): #New method
        if self.is_empty():
            return 0
        else:
            return self.value + self.left_child.compute_sum() + self.right_child.compute_sum()
        
    def compute_count(self): #New method
        if self.is_empty():
            return 0
        else:
            return 1 + self.left_child.compute_count() + self.right_child.compute_count()
        
        
    
my_tree = BinarySearchTree()

my_tree.insert(2)
my_tree.insert(4)
my_tree.insert(6)
my_tree.insert(8)
my_tree.insert(10)
my_tree.insert(12)

print("Sum", my_tree.compute_sum())
print("Number of nodes", my_tree.compute_count())
           


    

