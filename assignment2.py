def create(name):
    fh = open(f'{name}.txt', 'w')
    contents = input('Add some contents below:\n> ')
    fh.write(contents)
    fh.close()
    return 

print('Welsome to Notepad World')
names = []
print('Please register your username below')
user = input('User name: ').lower()
names.append(user)
print(f'Hi {user}, you have successfully been registered!')

notepads = []
account = {f"{user}": notepads}

login = input('Enter your username to login: ').lower()

if login in names and len(notepads) == 0:
    print(f'welcome {user}!\nYou do not have an existing notepad, create one below!')
    name_of_notepad = input('Enter name of notepad: ')
    create(name_of_notepad)
    notepads.append(name_of_notepad)

    choice = ['y', 'n']
    cont = input("Click 'y' to do more stuff!").lower()

    if cont == choice[0] and login in names:
        select = ['c', 'v']
        choose= input(f"Click 'C' to create a new notepad or 'V' to view existing ones!\n> ").lower()
        if choose == select[0]:
            name_of_notepad = input('Enter name of notepad: ')
            create(name_of_notepad)
            notepads.append(name_of_notepad)
        elif choose == select[1]:
            print(f"Here's a list of your notepads below\n{account[f'{user}']}") 
        

else:
    print('Sorry you dont have an account\n')
    