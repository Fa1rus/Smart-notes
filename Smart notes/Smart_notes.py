print("Hello, welcome to Smart Notes :)")

choices = {'Write':'w',
        'Show all notes': 's',
        'Delete a note' : 'd',
        'Search notes': 'f',
        'Edit': 'e',
        'Exit':'x'
}

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

def valid_number(numCheck):
    while True:
        if not numCheck.isdigit():
            continue
        else:
            return int(numCheck)

def write_note():
    words = input("Write a note: ")
    with open(filename,'a') as f:
        f.write(words + '\n')

def show_notes():
    try:
        with open(filename,'r') as f:
            print()
            print(f.read())
            print()
    except FileNotFoundError:
        print("No notes found yet.")
        
def delete_note():
    try:
        with open(filename,'r') as f:
            notes = f.readlines()
    except FileNotFoundError:
        print("No notes to delete.")
        return

    # If file exist but empty
    if not notes:
        print("No notes to delete.")
        return

    # Print all notes with number of lines
    print("\nYour notes:")
    for i,note in enumerate(notes,start=1):
        print(f'{i}. {note}',end='')
    print()

    # Loop to input valid number
    while True:
            delete_str = input('Enter a line number: ')
            delete = valid_number(delete_str)
            
            if 1 <= delete <= len(notes):
                notes.pop(delete-1)
                with open(filename,'w') as f:
                    f.writelines(notes)
                print("Note deleted successfully.")
                break
            else:
                print("Invalid choice. Try again.")
                continue
    
def search_note():
    with open(filename) as f:
        notes = f.readlines()
    
    keyword = input('keyword to search: ').strip()
    
    found = False
    for i,note in enumerate(notes,start=1):
        if keyword.lower() in note.lower():
            found = True
            print(f'{i}. {note}')

    if not found:
        print("No matching notes.")

def edit_note():
    with open(filename) as f:
        notes = f.readlines()
    if not notes:
        print('Note are empty')
        return
    for i,note in enumerate(notes,start=1):
        print(f"{i}. {note}",end='')
        print()

    while True:
        line_str = input("Enter a line number: ")
        if line_str.isdigit():
            line = int(line_str)
            if 1 <= line <= len(notes):
                break
        print("Invalid line number.")
    
    new_text = input("New text: ")
    notes[line -1 ] = new_text + "\n"
    
    with open(filename,'w') as f:
        f.writelines(notes)
    print("Note update successfully.")

def choose_mode(ChoiceInput):
    # Mode write
    if choice == 'w':
        write_note()
    
    # Mode show all notes
    elif choice == 's':
        show_notes()

    # Mode delete
    elif choice == 'd':
        delete_note()

    # Mode search
    elif choice == 'f':
        search_note()

    # Mode edit
    elif choice == 'e':
        edit_note()

    elif choice == 'x':
        print("\nHave a nice day :)")
        return 0
                
# Main loop
while True:
    # Show all modes in this program
    print("\n--- Smart Notes Menu ---")
    for key,value in choices.items():
        print(f'{key:15} [{value}]')

    # User choose the righ choices
    choice = check_choice()

    # Choice to open file mode
    if choose_mode(choice) == 0: break
    