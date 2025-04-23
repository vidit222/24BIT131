"""
Implement a String class containing the following functions:

a. Overloaded += operator function to perform string concatenation

b. Method toLower() to convert upper case letters to lower case.

c. Method toUpper() to convert lower case letters to upper case.
"""


class String:
    def __init__(self, value):
        self.value = value

    def __iadd__(self, other):
        if isinstance(other, String):
            self.value += other.value
        else:
            self.value += str(other)
        return self

    def toLower(self):
        self.value = self.value.lower()
        return self

    def toUpper(self):
        self.value = self.value.upper()
        return self


# Example usage
if __name__ == "__main__":
    str1 = String("Hello")
    str2 = String(" World")
    str1 += str2
    print(str1.value)  # Output: Hello World

    str1.toLower()
    print(str1.value)  # Output: hello world

    str1.toUpper()
    print(str1.value)  # Output: HELLO WORLD
    str1 += "!"
    print(str1.value)  # Output: HELLO WORLD!
    str1 += 123
    print(str1.value)  # Output: HELLO WORLD!123
    str1 += str2
    print(str1.value)  # Output: HELLO WORLD!123 World
