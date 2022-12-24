import Classss


class Person:
    def __init__(self, name, age):
        self.g = name
        self.age = age


p1 = Person("John", 36)
newObj = Classss.ChildReadme("Amai", "Ks", 2)
newObj.printAge()

print(p1.g)
print(p1.age)

print(dir(Classss))
