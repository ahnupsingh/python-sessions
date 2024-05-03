## Task 1 - Dictionaries

### Problem: Write a Python program to implement a simple address book application. 

Implement a class called AddressBook that allows users to store and retrieve contact information. The AddressBook class should have methods to add a new contact, retrieve contact details by name, update contact information, and delete a contact. Each contact should have attributes such as name, phone number, email, and address.

Requirements:

Implement a class called AddressBook with methods add_contact(name, phone, email, address), get_contact(name), update_contact(name, phone, email, address), and delete_contact(name).
The add_contact method should add a new contact to the address book. If a contact with the same name already exists, it should update the existing contact information.
The get_contact method should retrieve contact details (phone, email, address) by name. If the contact is not found, it should return "Contact not found".
The update_contact method should update the contact information (phone, email, address) for a given name. If the contact is not found, it should return "Contact not found".
The delete_contact method should delete a contact by name. If the contact is not found, it should return "Contact not found".
Use a dictionary to store contact information, with the contact name as the key and a dictionary containing phone, email, and address as the value.

### Learnings

- use dictionaries to store and manipulate data in real-world applications, such as an address book
- implement basic CRUD (Create, Read, Update, Delete) operations


### Problem: Find Most Frequently Repeating Number in a List

You are given a list of integers, and your task is to write a Python program to find the number that repeats most frequently in the list.

Your program should implement a function called find_most_frequent(numbers) that takes a list of integers numbers as input and returns the number that repeats most frequently. If there are multiple numbers with the same maximum frequency, your program should return any one of them.


## Task 2 - Recursion

### Problem: Write a recursive program to flatten a nested dictionary. The dictionary can be nested to any levels.

### Problem: Write a Python program to implement a file search tool that searches for a specific file name in a directory and its subdirectories.

Implement a function called search_file(directory, filename) that takes the path to a directory and a target file name as input and recursively searches for the file in the directory and all its subdirectories. If the file is found, the function should return the full path to the file. If the file is not found, the function should return "File not found".

### Requirements:

- Implement a recursive function search_file(directory, filename) that takes a directory path (directory) and a target file name (filename) as input and returns the full path to the file if found, or "File not found" if not found.
- The function should search for the target file (filename) in the specified directory and all its subdirectories recursively.
- If the target file is found in any of the subdirectories, the function should return the full path to the file.
- If the target file is not found in any of the directories, the function should return "File not found".
- Handle errors such as invalid directory paths or permissions issues by raising appropriate exceptions and providing informative error messages.

### Learnings

- Recursion concepts to traverse directory structures and search for specific files
- handle errors and edge cases


## Task 2 - 