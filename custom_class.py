# Here’s a Python implementation of the Rectangle class based on the given requirements:

class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width
    
    def __iter__(self):
        # This allows iteration over the Rectangle instance
        yield {'length': self.length}
        yield {'width': self.width}
        
    def __repr__(self):
        return f"Rectangle(length={self.length}, width={self.width})"

# FOR EXECUTION
# Create a Rectangle instance
rect = Rectangle(10, 5)

# Iterate over the Rectangle instance
for attribute in rect:
    print(attribute)

# Print the Rectangle instance (will use __repr__)
print(rect)


# 1. The _init_ method initializes the Rectangle object with length and width as integers.
# 2. The _iter_ method is defined to make the object iterable. It yields the length first,
#  then the width, formatted as a dictionary ({'length': value}, {'width': value}).
# 3. The _repr_ method is included to provide a clean representation of the rectangle when printed.



# Example Output will be like this
# {'length': 5}
# {'width': 10}
# Rectangle(length=10, width=5)