"""Demonstrating of dictionary capabilities."""

# Declaring the type of a dictonary 
schools: dict[str, int]

# Initialize to an empty dictonary
schools = dict()

# Set a key-value pairing in the dictionary
schools["UNC"] = 19400
schools["Duke"] = 6717
schools["NCSU"] = 26150

# Print a dictonary literal representation
print(schools)

# Access a value by its key -- "lookup", use subscription notation
# Use single quotation marks because within double quotation marks
print(f"UNC has {schools['UNC']} students")

# Remove a key-value pair from a dictionary
# by its key
schools.pop("Duke")

# Test for existence of a key
if "Duke" in schools:
    print("Found the key 'Duke' in schools.")
else:
    print("No key 'Duke' found in schools.")

# Update / Reassign a key-value pair
schools["UNC"] = 20000
schools["NCSU"] += 200

print(schools)

# Demonstration of dictionary literals
schools = {} 
# Same as dict()
print(schools)

# Alternatively, initialize key-value pairs
schools = {"UNC": 19400, "Dukie": 6717, "NCSU": 26150}
print(schools)

# What happens when a key does not exist
# print(schools["UNCC"])

# Example looping over keys of a dict
for school in schools:
    print(f"Key: {school} -> Value: {schools[school]}")
