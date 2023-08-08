my_dict = {}
num_entries = int(input("Enter the number of entries to add: "))
for i in range(num_entries):
    key = input("Enter key for entry {}: ".format(i + 1))
    value = input("Enter value for entry {}: ".format(i + 1))
    my_dict[key] = value
print("Dictionary:", my_dict)
print("Values:", my_dict.values())
key_to_change = input("Enter key to change: ")
if key_to_change in my_dict:
    new_value = input("Enter new value: ")
    my_dict[key_to_change] = new_value
else:
    print("Key not found in dictionary.")
print("Number of entries:", len(my_dict))
key_to_check = input("Enter key to check: ")
if key_to_check in my_dict:
    print("Entry with key '{}' exists.".format(key_to_check))
else:
    print("Entry with key '{}' does not exist.".format(key_to_check))
