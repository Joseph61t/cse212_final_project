class Node:
    def __init__(self, Value):
        self.Value = Value
        self.next = None
class Singly_Linked_List:
    def __init__(self):
        self.head = None
    # Code to print out the entire list
    def print_list(self):
        node = self.head
        # while the node is not nothing, print the value of the node, and move to the next one. 
        while node != None:
            print(node.Value)
            node = node.next
    # function to add insert a new value at the head.
    def insert(self):
        # create a new node
        new_node = Node(input("what do you want to add? \n"))
        # point the next of the new node to the current head.
        new_node.next = self.head
        # set the head to the new node.
        self.head = new_node
    # function to remove the current head.
    def remove(self):
        if self.head != None:
            self.head = self.head.next

def main():
    # make a linked list
    todo_list = Singly_Linked_List()
    do = input("Add to list (a),\nremove from list (r), \nprint list (p), \nexit (e) \n ")
    # so long as exit is not chosen, keep doing things
    while True:
        # If exit was chosen, exit
        if do == "e" or do == "E":
            break
        # If add was chosen, insert a node at the head
        elif do == "a" or do == "A":
            todo_list.insert()
        # If remove was chosen, remove a node from the head
        elif do == "r" or do == "R":
            todo_list.remove()
        # If print was chosen, print the list
        elif do == "p" or do == "P":
            todo_list.print_list()
        do = input("Add to list (a),\nremove from list (r) \nprint list (p), \nexit (e) \n ")

if __name__ == "__main__":
    main()