class Readme:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def printSelfName(self):
        print(self.firstName, self.lastName)
        for i in range(6):
            print(self.firstName, self.lastName)


okay = Readme("AAmir", "KALIMI")
print(okay.firstName)
okay.printSelfName()


class ChildReadme(Readme):
    def __init__(self, firstName, lastName, age):
        super().__init__(firstName, firstName)
        self.age = age

    def printAge(self):
        print(self.age)

    def printSelfName(self):
        print(self.age)


letch = ChildReadme("Imran", "Kalimi", 24)
letch.printSelfName()
# letch.printAge()
letch.printSelfName()
