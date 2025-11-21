print("Hello, welcome to Smart Notes :)")

choices = {'Write':'w',
        'Show all notes': 's',
        'Exit':'x'}

filename = '/home/fa1rusz/p/py_basic/Smart notes/notes.txt'

# Check if users are choose the righ choice
def check_choice():
    while True:
        choice = input("Your choice: ").strip()
        if choice in choices.values():
            return choice
        else:
            print("Please choose a valid option!")
            continue

# Enter mode
while True:
    print("\n--- Smart Notes Menu ---")
    for key,value in choices.items():
        print(f'{key:15} [{value}]')

    # User choose the righ choices
    choice = check_choice()


    # Choice to open file mode
    if choice == 'w':
        words = input("Write a note: ")
        with open(filename,'a') as f:
            f.write(words + '\n')
    elif choice == 's':
        try:
            with open(filename,'r') as f:
                print(f.read())
                print()
        except FileNotFoundError:
            print("No notes found yet.")
    elif choice == 'x':
        break
