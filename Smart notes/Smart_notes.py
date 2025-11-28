import datetime

print("Hello, welcome to Smart Notes")

choices = {
    'Write':'w',
    'Show all notes': 's',
    'Delete a note' : 'd',
    'Search notes': 'f',
    'Edit': 'e',
    'Exit':'x'
}
categories = {
    '1': ("Personal", "personal.txt"),
    '2': ("Study", "study.txt"),
    '3': ("Work", "work.txt"),
    '4': ("Ideas", "ideas.txt")
}

filename = 'notes.txt'

def time():
    date = datetime.datetime.now()
    dateFormat = "%Y-%m-%d %H:%M"
    date = date.strftime(dateFormat)
    return date


# Check if users are choose the righ choice
def check_choice():
    while True:
        choice = input("Your choice: ").strip()
        if choice in choices.values():
            return choice
        else:
            print("Invalid option, Please Try again.")
            continue

def show_category(categories):
    for i,g in categories.items():
        print(f'{i}. {g[0]}',end='')
        print()

def choose_category():
    show_category(categories)
    print("Enter category number")
    while True:
        category = str(valid_number())
        if category in categories:
            return category
        else:
            print("Invalid choice.")
            continue
    
def valid_number():
    while True:
        numCheck = input("\tChoice: ")
        if not numCheck.isdigit():
            print("Invalid input.")
            continue
        else:
            return int(numCheck)

def write_note():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    words = input("Write a note: ")
    with open(filename,'a') as f:
        f.write(f'[{timestamp}] {words} \n')

def show_notes():
    try:
        with open(filename,'r') as f:
            print()
            note = f.read()
            if note == '':
                print("Nothing here.")
            else:
                print(note)
            print()
    except FileNotFoundError:
        print("No notes found yet.")
        return
        
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
            print('Enter a line number')
            delete = valid_number()
            
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
    try:
        with open(filename) as f:
            notes = f.readlines()
    except FileNotFoundError:
        print("No notes found yet.")
        return
    
    keyword = input('keyword to search: ').strip()
    
    found = False
    for i,note in enumerate(notes,start=1):
        if keyword.lower() in note.lower():
            found = True
            print(f'{i}. {note}')

    if not found:
        print("No matching notes.")

def edit_note():
    try:
        with open(filename) as f:
            notes = f.readlines()
    except FileNotFoundError:
        print("No notes found yet.")
        return

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
    if ChoiceInput == 'w':
        write_note()
    # Mode show all notes
    elif ChoiceInput == 's':
        show_notes()
    # Mode delete
    elif ChoiceInput == 'd':
        delete_note()
    # Mode search
    elif ChoiceInput == 'f':
        search_note()
    # Mode edit
    elif ChoiceInput == 'e':
        edit_note()
    elif ChoiceInput == 'x':
        print("\nHave a nice day :)")
        return 0
                
category = choose_category()
filename = categories[category][1]

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