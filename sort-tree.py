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

            



Tree = tree()

Tree.add(5)

Tree.display()

Tree.add(6)
Tree.add(4) 
Tree.add(1)
Tree.display()