class node:
    def __init__(self, val = None):
        self.value = val
        self.left = None
        self.right = None

class tree:
    def __init__(self):
        self.root = node()
        self.curr_node = self.root
    # Function to add a node into the tree
    def add(self, val):
        # Until a break condition is met, keep going
        while True:
            # If the root is empty, insert the value, break loop
            if self.root.value == None:
                self.root.value = val
                break
            # if the value is less then that of current node, go to left pointer
            elif val < self.curr_node.value:
                # if there is no left on current node, make new node, and insert, break loop.
                if self.curr_node.left == None:
                    self.curr_node.left = node(val)
                    self.curr_node = self.root
                    break
                else:
                    self.curr_node = self.curr_node.left
            # if the value is greater than or equal to that of current node, go to right pointer
            elif val >= self.curr_node.value:
                # if there is no right on current node, make new node, and insert, break loop.
                if self.curr_node.right == None:
                    self.curr_node.right = node(val)
                    self.curr_node = self.root
                    break
                else:
                    self.curr_node = self.curr_node.right
    # Function for displaying the tree
    def display(self):
        if self.root.value != None:
            self.display_node(self.root)
    # Sub function for display
    def display_node(self, node):
        # If there is a node on the left, call display node on it
        if node.left != None:
            self.display_node(node.left)
        # print the nodes value
        print(node.value)
        # If there is a node on the right, call display node on it.
        if node.right != None:
            self.display_node(node.right)

    # Function used to find a number, and display the number of nodes gone through to get to it.
    def find(self, number):
        if self.root.value != None:
            print(f"used: {self.find_in_node(self.root, number, 0)}")
    # Takes a node, and checks checks it for a value
    def find_in_node(self, node, number, count):
        # if the value is in current node, do nothing
        if node.value == number:
            pass
        # if value is less then current node value, go left, or tell user value isn't in tree
        elif number < node.value: 
            # If value is less then current node value, but node left is none, value is not in tree
            if node.left == None:
                print(f"Number not in tree.")
            # If there is left, call find_in_node on left, and add its return to count
            else:
                count += self.find_in_node(node.left, number, count)
        # If number is greater than current node value, go right, or tell user value isn't in tree
        elif number > node.value: 
            # If value is greater then current node value, but node right is none, value is not in tree
            if node.right == None:
                print(f"Number not in tree.")
            # If there is right, call find_in_node on right, and add its return to count
            else:
                count += self.find_in_node(node.right, number, count)
        # Return count plus 1
        return count + 1



Tree = tree()

Tree.add(5)

Tree.display()

Tree.add(6)
Tree.add(4) 
Tree.add(1)
Tree.add(7)
Tree.add(2)
Tree.add(9)
Tree.display()

Tree.find(9)