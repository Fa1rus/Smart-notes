print("Hello welcome to Smart notes :)")

choices = {'Write':'w',
        'Show all notes': 's',
        'Exit':'x'}

# Enter mode
while True:
    for key,value in choices.items():
        print(f'{key} [{value}]',end=' ')

    choice = input("Choice: ")
    if choice in choices.values():
        break
    else:
        print("Please enter in the choice!")
        continue

filename = input("file location to note:")

# Choice to open file mode
if choice == 'w':
    words = input("To notes: ")
    with open(filename,'a') as f:
        f.write(words)
elif choice == 's':
    with open(filename,'r') as f:
        f.read()
        print(f)