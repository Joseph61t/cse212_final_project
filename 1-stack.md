# Stack Tutorial

## Introduction
 In this tutorial, we will be going over how to utilize a stack, both adding to and removing from the stack with an O(1) operation.

 These are the normal operations of a stack, along with their efficiency.

 Operation   |  Efficiency
------------|--------------
 Insert | 0(1)
 Remove | 0(1) 
 
## Usage
 Typically, stacks are used for history, undo/redo actions, and other things that only need to access the last thing added to the list. 

 We can think of a stack the same way we think of a stack of plates, only the top plate can be accessed at a time. You can remove a plate, and access the next one, or add a plate, removing access to the current plate.

## Implementing The Stack
 In this [code](stack_undo.py) I will show how to add to a list of words, and then return to a previous version of that list, removing a single word at a time. Once you have gone over that code, you should try and implement that same idea, but instead of just going back, you should make yours able to go forwards as well. (Adding the words that were removed back onto the stack.)

 (Hint, you need another stack.)

 Here is my [version](stack_undo_redo.py) of that code.