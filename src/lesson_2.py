class Employee:

    def __init__(self, first, last):
        self.first = first
        self.__last = last

    @property
    def email(self):
        return f"{self.first}.{self.__last}@gmail.com"

    @property
    def fullname(self):
        return f"{self.first} {self.__last}"

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.__last = last

    @fullname.deleter
    def fullname(self):
        print("данные удалены")
        self.first = None
        self.__last = None


emp = Employee("Vova", "Teslenko")
print(emp.fullname)

emp.fullname = "Lena Ustimenko"

print(emp.fullname)


print(dir(emp))
print(emp._Employee__last)
