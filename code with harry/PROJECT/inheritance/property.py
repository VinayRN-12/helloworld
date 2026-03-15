class Dog:
    def __init__(self, name):
        self._name = name

    @property               # Getter method
    def name(self):
        return self._name

    @name.setter            # Setter method for same property
    def name(self, new_name):
        self._name = new_name


d = Dog("Tommy")
print(d.name)   # Getter runs → "Tommy"

d.name = "Bruno"  # Setter runs → updates _name
print(d.name)   # Getter runs again → "Bruno"
