try:
    # Intentional IndexError: Accessing an invalid list index
    my_list = [1, 2, 3]
    print(my_list[5])  # Index 5 does not exist, will raise IndexError

except IndexError:
    # Handling IndexError: The index is out of range for the list
    print("IndexError occurred! List index out of range.")

try:
    # Intentional KeyError: Trying to access a non-existent key in a dictionary
    my_dict = {'name': 'John', 'age': 25}
    print(my_dict['address'])  # 'address' key does not exist, will raise KeyError

except KeyError:
    # Handling KeyError: The key is not found in the dictionary
    print("KeyError occurred! Key not found in the dictionary.")

try:
    # Intentional TypeError: Adding a string and an integer
    result = "Hello" + 5  # Cannot add a string and an integer, will raise TypeError

except TypeError:
    # Handling TypeError: Unsupported operand types
    print("TypeError occurred! Unsupported operand types.")
