class Node:
    def __init__(self, Value):
        self.Value = Value
        self.next = None
        self.prev = None
class Doubly_Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None
    # Code to print out the entire list
    def print_list(self):
        node = self.head
        # while the node is not nothing, print the value of the node, and move to the next one. 
        while node != None:
            print(node.Value)
            node = node.next
    # function to add insert a new value at the head.
    def h_insert(self, Value):
        # create a new node
        new_node = Node(Value)
        if self.head != None:
            # point the current head's prev to new node.
            self.head.prev = new_node
        # point the next of the new node to the current head.
        new_node.next = self.head
        # set the head to the new node.
        self.head = new_node
        if self.tail == None:
            self.tail = self.head
    # function to remove the current head.
    def h_remove(self):
        if self.head != None:
            self.head = self.head.next
            self.head.prev = None
    # function to add insert a new value at the tail.
    def t_insert(self, Value):
        # create a new node
        new_node = Node(Value)
        # if there is no tail, then there is no head,
        # so insert at the head instead. 
        if self.tail == None:
            self.h_insert(Value)
        else:
            # point the current tail's next to new node.
            self.tail.next = new_node
            # point the prev of the new node to the current tail.
            new_node.prev = self.tail
            # set the tail to the new node.
            self.tail = new_node
    # function to remove the current head.
    def t_remove(self):
        if self.head != None:
            self.tail = self.tail.prev
            self.tail.next = None

def main():
    # make a linked list
    todo_list = Doubly_Linked_List()
    # get what the user wants to do to the list
    do = input("Add to list (a),\nremove from list (r) \nprint list (p), \nexit (e) \n ")
    # So long as print was not chosen, ask for where to perform the action.
    if do != "p" or do != "P":
        where = input("Do you want to do that to the head (h) or tail (t)? ")
    while True:
        if do == "e" or do == "E":
            break
        # If tail was chosen, perform action at tail
        if where == "t" or where == "T":
            # If add was chosen, insert a node at the tail
            if do == "a" or do == "A":
                todo_list.t_insert(input("what do you want to add? \n"))
            # If remove was chosen, remove a node from the tail
            elif do == "r" or do == "R":
                todo_list.t_remove()
        # If head was chosen perform action at head
        elif where == "h" or where == "H":
            # If add was chosen, insert a node at the head
            if do == "a" or do == "A":
                todo_list.h_insert(input("what do you want to add? \n"))
            # If remove was chosen, remove a node from the head
            elif do == "r" or do == "R":
                todo_list.h_remove()
        # If print was chosen, print the list
        elif do == "p" or do == "P":
            todo_list.print_list()
        do = input("Add to list (a),\nremove from list (r) \nprint list (p), \nexit (e) \n ")
        # So long as print was not chosen, ask for where to perform the action.
        if do != "p" or do != "P":
            where = input("Do you want to do that to the head (h) or tail (t)? ")

if __name__ == "__main__":
    main()