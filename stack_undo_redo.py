def main():
    words = []
    removed_words = []
    while True:
# Get what the user wants to do.
        doing = input("""
Enter 'N' to add a new word.
Enter 'R' to remove a word. 
Enter 'A' to re-add a word.
Enter 'E' to exit.
""")
        if doing == 'n' or doing == 'N':
            # Add a word to the stack.
            words.append(input("Enter a word: "))
        elif doing == 'r' or doing == 'R':
            # If there are words in the stack, remove the last one added.
            # and add it to the removed words stack.
            if len(words) == 0:
                print("no words in stack")
            else:
                removed_words.append(words.pop())
        elif doing == 'a' or doing == 'A':
            # If there are words in the removed words stack, remove the last one added.
            # and add it to the original stack
            if len(removed_words) == 0:
                print("No words to re-add.")
            else:
                words.append(removed_words.pop)
        elif doing == 'e' or doing == 'E':
            # While there are words in the stack, print the first one, and remove it from the stack. 
            # Then exit the loop.
            while len(words) > 0:
                print(words.pop())
            break


if __name__ == "__main__":
    main()