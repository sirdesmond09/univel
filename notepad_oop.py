class Notepad():

    def __init__(self, username):
        self.username = username
        


    def create(self, note):
        self.note = note

        fh       = open(f'{self.note}.txt', 'w')
        contents = input('Add some contents below:\n> ')
        fh.write(contents)
        fh.close()
        return 

    def view(self, username, note, notepads):
        account = {f"{self.username}": notepads}
        print("Here's a list of your notepads below")
        for i in account[f'{self.username}'] :
            print(i)

        note2read = input("Select a note to read\n> ").lower()

        if note2read in notepads:
            fh  = open(f"{note2read}.txt", 'r')
            print(fh.read())
        else:
            print("Note does not exist!")

    def edit(self, notepads):
        account = {f"{self.username}": notepads}
        print("Here's a list of your notepads below")
        for i in account[f'{self.username}'] :
            print(i)

        note2edit = input("Select a note to edit\n> ").lower()

        if note2edit in notepads:
            fh      = open(f"{self.note}.txt", 'a') 
            content = input('Add some more contents below:\n> ')
            fh.write(content)
            fh.close()
   


print('Welcome to Notepad World')
names = []
notepads = []

while True:
    if len(names) == 0:
        print('Please register your username below')
        user = input('User name: ').lower()
        names.append(user)
        print(f'Hi {user}, you have successfully been registered!')


    if len(names) >=1:
        login = input('Enter your username to login: ').lower()
        if login in names:
            logged_in = (Notepad(username= user)) 

            if len(notepads) == 0:
                print(f'welcome {logged_in.username}!')
                name_of_notepad = input('Enter name of notepad: ')
                logged_in.create(name_of_notepad)
                notepads.append(name_of_notepad)

            if len(notepads) >= 1:
                print(f'welcome back {logged_in.username}!')
                do_you = input("Do you have an existing note?y/n\n> ").lower()
                if do_you == 'y':
                    view = input("Do you want to view or edit your notepads?view/edit\n> ").lower()
                    if view == 'view':
                        logged_in.view(username= user, note= name_of_notepad, notepads= notepads)
                    if view == 'edit':
                        logged_in.edit(notepads= notepads)
                else:
                    print("Create a new notepad below")
                    name_of_notepad = input('Enter name of notepad: ')
                    logged_in.create(name_of_notepad)
                    notepads.append(name_of_notepad)
        else:
            print("Account doest not exist")            
            print('Please register your username below')
            user = input('User name: ').lower()
            names.append(user)
            print(f'Hi {user}, you have successfully been registered!')



