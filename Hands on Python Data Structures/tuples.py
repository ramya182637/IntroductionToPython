# Step 1: Creating a tuple with three elements
favorite_things = ('Inception', 'Bohemian Rhapsody', '1984')

# Step 2: Trying to change one of the elements
try:
    favorite_things[0] = 'The Matrix' 

except TypeError:
    print("Oops! Tuples cannot be changed.")

# Step 3: Printing the length of the tuple using len()
print("Favorite things:", favorite_things)
print("Length of tuple:", len(favorite_things))
