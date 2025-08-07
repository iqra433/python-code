class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age=age  # private variable

    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        if new_age > 0:
            self.__age = new_age
        else:
            print("Age must be positive.")

# Using the class
p1 = Person("Iqra", 20)

print(p1.name)         # Output: Iqra
print(p1.get_age())    # Output: 20

p1.set_age(25)
print(p1.get_age())    # Output: 25

