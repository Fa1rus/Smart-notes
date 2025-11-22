print("Hello, welcome to Smart Notes :)")

choices = {'Write':'w',
        'Show all notes': 's',
        'Delete a note' : 'd',
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

# Main loop
while True:
    # Show all modes in this program
    print("\n--- Smart Notes Menu ---")
    for key,value in choices.items():
        print(f'{key:15} [{value}]')

    # User choose the righ choices
    choice = check_choice()


    # Choice to open file mode
    
    # Mode write
    if choice == 'w':
        words = input("Write a note: ")
        with open(filename,'a') as f:
            f.write(words + '\n')
    
    # Mode show all notes
    elif choice == 's':
        try:
            with open(filename,'r') as f:
                print()
                print(f.read())
                print()
        except FileNotFoundError:
            print("No notes found yet.")

    # Mode delete
    elif choice == 'd':
        try:
            with open(filename,'r') as f:
                notes = f.readlines()
        except FileNotFoundError:
            print("No notes to delete.")
            continue

        # If file exist but empty
        if not notes:
            print("No notes to delete.")
            continue

        # Print all notes with number of lines
        print("Your notes:")
        for i,note in enumerate(notes,start=1):
            print(f'{i}. {note}',end='')
        print()

        # Loop to input valid number
        while True:
            if not notes:
                print("No notes to delete.")
                break
            else:
                delete = int(input('Enter a line number: '))
            
                if 1 <= delete <= len(note):
                    notes.pop(delete-1)
                    with open(filename,'w') as f:
                        f.writelines(notes)
                    print("Note deleted successfully.")
                    break
                elif delete > lines:
                    print("Invalid input")
                    continue

    elif choice == 'x':
        print("\nHave a nice day :)")
        break
