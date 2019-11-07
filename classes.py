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


class Warrior(Person):
    has_shield = True
    has_knife  = True
    shield_on  = False
    
    def __init__(self, name, age = 20, strength=20, skill= 10):
        super().__init__(name, age)
        self.strength = strength
        self.skill = skill

    def fight(self, foe):
        warrior = self
        while True:

            warrior.strength = round(warrior.strength - (foe.skill * foe.strength)/100)
            print(warrior.name, "is attacking", foe.name)
            print(warrior.name, warrior.strength, foe.name, foe.strength)
            print()

            if warrior.strength <1:

                return

            warrior, foe = foe,warrior
            time.sleep(3)






new_person = Warrior(name = "John", age = 20, strength=20, skill= 10)
person2 = Warrior(name = "Solonicus", age = 20, strength=30, skill= 10)
new_person.walk(6)
new_person.fight(person2)
# person1 = Person(name = "John", age = 23)
# print(person1.name)
# print(person1.has_mouth)

# person2 = Person(name = "paul", age = 23)
# print("Before change of name : ", person2.name)
# person2.name = "John"
# print("After change of name : ",person2.name)
# (person2.has_mouth)
# person2.walk(steps= 10)
# (person2.walk())
# (person2.walk())

# names = "Ade", "shola", "Bola"
# people = []

# for name in names:
#     person = Person(name = name, age = 23)
#     people.append(person)

# print([(person.name, person.has_mouth) for person in people])