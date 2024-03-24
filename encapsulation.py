class Encapsulation:
    def __init__(self):
        self.public = "I am public"
        self._protected = "I am protected"
        self.__private = "I am private"

    @property
    def private(self):
        return self.__private

    @private.setter
    def private(self, value):
        self.__private = value


encapsulated_object = Encapsulation()
print(encapsulated_object.public)
print(encapsulated_object._protected)
encapsulated_object.private = "I have been changed"
print(encapsulated_object.private)


