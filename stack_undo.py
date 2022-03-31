def main():
    words = []
    while True:
# Get what the user wants to do.
        doing = input("""
Enter 'N' to add a new word.
Enter 'R' to remove a word. 
Enter 'E' to exit.
""")
#depending on the input, perform a function.
        if doing == 'n' or doing == 'N':
            # Add a word to the stack
            words.append(input("Enter a word: "))
        elif doing == 'r' or doing == 'R':
            # If there are words in the stack, remove the last one added.
            if len(words) == 0:
                print("no words in stack")
            else:
                words.pop()
        elif doing == 'e' or doing == 'E':
            # While there are words in the stack, print the first one, and remove it from the stack. 
            # Then exit the loop.
            while len(words) > 0:
                print(words.pop())
            break


if __name__ == "__main__":
    main()