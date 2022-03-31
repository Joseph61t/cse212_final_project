# Linked List Tutorial

## Introduction
 In this tutorial, we will be going over how to utilize a linked list. We will go over how to create one, using nodes, and how to insert a new node/item in the list. 

 A node is a data structure that contains a value, and at least one pointer, typically to another node.

 There are two types of linked lists, single direction linked lists, and double, or doubly linked lists. The only difference between the two is that the doubly linked list can be accessed from both ends easily.

 These are the normal operations of a linked list, along with their efficiency.

 Operation   | Efficiency
------------|--------------
 Insert head | 0(1)
 Remove head | 0(1) 
 Insert (anywhere) | 0(n)
 Remove (anywhere) | 0(n)

The same efficiencies apply for a doubly linked list, except it has an insert and remove at tail with 0(1) efficiency.

## Usage
 Typically, Linked lists are used for shorter lists, like a shopping list, or to-do list. and other things that only need to access the last thing added to the list. 

 Linked lists save more memory then standard lists, because each item in the list has it's own position in memory, so no extra memory is made inherint to the list.

## Implementing A Linked List
 In this [code](todo_list.py) I will show how to make a to-do list using a singly linked list. 
 Once you have gone over that code, try and make a shopping list using a linked list. But, instead of just pointing to the next node, you should point to the previous one as well. You should also add tail functions rather then just having head ones.

 Here is my [version](shopping_list.py) of that code.