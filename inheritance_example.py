class Parent:
    def __init__(self):
        print("Parent class is create")

    def speak(self):
        print("parent is speaking")


class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child class is create")

    def speak(self):
        super().speak()
        print("child is speaking")

child = Child()
child.speak()

