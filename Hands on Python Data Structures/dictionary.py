# Step 1: Creating a dictionary to store personal information
person_info = {
    "name": "Ramya",
    "age": 24,
    "city": "Guntur"
}
# Step 2: Adding a new key-value pair for favorite color
person_info["favorite color"] = "Blue"

# Step 3: Updating the "city" key with a new value
person_info["city"] = "Halifax"
# Step 4: Printing all the keys and values using a loop
print("Keys:-", ', '.join(person_info.keys()))
print("Values:-", ', '.join(str(value) for value in person_info.values()))
