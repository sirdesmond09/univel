#OOP
import time

class Person:
    has_mouth = True
    has_eyes  = True
    has_shield = False
    has_knife  = True

    strength  = 20

    line1 = list(" 0                  ")
    line2 = list(" |                  ")
    line3 = list(" /\                 ")
    line4 = list("/__|________________")

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self, steps):
        self.display_position()

        for _ in range(steps):
            self.line1.pop(-1)
            self.line1.insert(0," ")
            self.line2.pop(-1)
            self.line2.insert(0," ")
            self.line3.pop(-1)
            self.line3.insert(0," ")
            self.line4.pop(-1)
            self.line4.insert(0,"_")
        self.display_position()
    
    def display_position(self):
        print(f'{"".join(self.line1)}\n{"".join(self.line2)}\n{"".join(self.line3)}\n{"".join(self.line4)}')

person1 = Person(name = "Mary", age = 30)
print(person1.has_eyes)
print(person1.name)


names = ["ade", "shola", "John"]
people = []

for name in names:
    person = Person(name = name, age=10)
    people.append(person)

for person in people:
    print(person.name, person.has_eyes)


class Warrior(Person):
    def __init__(self, name, age = 10, strength = 20, skill = 10):
        super().__init__(name, age)
        self.strength = strength
        self.skill = skill

    def go_to_war(self, foe):
        warrior = self
        while True:
            

            warrior.strength = round(warrior.strength - (foe.skill * foe.strength)/100)
            print(warrior.name, "is attacking", foe.name)
            print(warrior.name, warrior.strength, foe.name, foe.strength)
            print()

            if warrior.strength < 1:
                print(f"{foe.name} won the fight!!!")
                return

            warrior, foe = foe, warrior
            time.sleep(2.5)


user1 = Warrior(name = "Gladiator", strength = 50, skill = 33)
user2 = Warrior(name = "solodicus", strength= 60, skill = 43)


user1.go_to_war(user2)








# class AccountHolder():
    
#     def __init__(self, name, bal):
#         self.name = name
#         self.balance = bal

#     def cash_deposit(self, money):
#         self.balance = money + self.balance
#         print(f"Your account has been credited with ${money}\nCurrent balance is ${self.balance}")

#     def cash_withdraw(self, money):
#         if money > self.balance:
#             print("Insufficient Funds")
#         else:
#             self.balance = self.balance - money
#             print(f"Your account has been debited with ${money}\nCurrent balance is ${self.balance}")

# attah = AccountHolder(name= "desmond", bal = 0)
# attah.cash_deposit(40000)
# attah.cash_withdraw(50000)
# attah.cash_withdraw(24782)