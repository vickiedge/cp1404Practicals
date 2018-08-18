#error message for line for - Q not defined - ??

def main():
    name = input("What is your name? ")
    choice = input("(H)ello\n(G)oodbye\n(Q)uit").upper()
    while choice != Q:
        if choice == "H":
            print("Hello ",name)
        elif choice == "G":
            print("Goodbye ",name)
        else:
            print("Invalid menu choice")
        choice = input("(H)ello \n (G)oodbye \n(Q)uit: ").lower()
    print("Finished")
main()