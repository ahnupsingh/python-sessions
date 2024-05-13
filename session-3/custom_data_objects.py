
# Introduction to Custom Data Objects (10 minutes)
    # Overview of custom data objects and their importance in Python programming.
    # Explanation of how custom data objects can represent real-world entities or complex data structures.

# Defining Classes (15 minutes)
    # Understanding classes as blueprints for creating objects.
    # Syntax for defining classes in Python.
    # Creating class attributes and methods.
    # Creating Instances of Custom Objects (15 minutes)
    # Instantiating objects from custom classes.
    # Initializing object attributes using the __init__ method.
    # Accessing and modifying object attributes.

# Adding Methods to Custom Classes (15 minutes)
    # Defining instance methods to perform operations on custom objects.
    # Understanding the self parameter and its significance.
    # Calling methods on custom objects.

# Special Methods (20 minutes)
    # Introduction to special methods (dunder methods) in Python.
    # Overloading operators using special methods (e.g., __add__, __eq__).
    # Implementing string representation (__str__, __repr__) and other special methods.
    # Static method

# Best Practices for Custom Data Objects (10 minutes)
    # Following naming conventions and coding standards for classes and objects.
    # Writing clear and concise documentation for custom classes and methods.
    # Testing custom data objects to ensure correctness and reliability.

# Practical Examples and Exercises (30 minutes)
    # Hands-on exercises to create and manipulate custom data objects.
    # Implementing custom classes to represent various real-world scenarios.
    # Solving problems using custom data objects and inheritance.

# Conclusion and Q&A (10 minutes)
    # Summary of key concepts covered in the session.
    # Addressing any remaining questions or concerns from participants.
    # Providing additional resources for further learning and exploration.
    
class Contact:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self):
        return f"{self.name} - Email: {self.email}, Phone: {self.phone}"
    
    def __repr__(self):
        return f"{self.name} - Email: {self.email}, Phone: {self.phone}"

# [
#     {
#         "name": "C"
#         "contact": {
#             "email": "",
#             "phone": ""
#         }
#     },
#     {
#         "name": "B"
#         "contact": {
#             "email": "",
#             "phone": ""
#         }
#     },
#     {
#         "name": "A"
#         "contact": {
#             "email": "",
#             "phone": ""
#         }
#     },
# ]

# Finding any contact by name

# Contact Book
    # - Name 1 - Contact [Email, Phone]
    # - Name 2 - Contact [Email, Phone]
    # - Name 3 - Contact [Email, Phone]
    # - Name 4 - Contact [Email, Phone]
    # - Name 5 - Contact [Email, Phone]
    # - Name 6 - Contact [Email, Phone]



# Importance of custom data objects
    # Abstraction and Encapsulation
    # Modeling Real-World Entities
    # Data Integrity and Validation
    # Customization and Extensibility
    # Code Organization and Readability
    # Code Reusability
    # Interoperability and Integration
    
class AddressBook:
    def __init__(self):
        self.contacts = []
        self.meta = {
            "no_of_pages": 0,
            "last_edited_on": None
        }

    def add_contact(self, contact):
        self.contacts.append(contact)

        if len(self.contacts) >= 10:
            self.meta.update({**self.meta, "no_of_pages": self.meta.get("no_of_pages", 0) + 1})

    def find_contact_by_name(self, name):
        for contact in self.contacts:
            if contact.name == name:
                return contact
        return None

    def display_contacts(self):
        for contact in self.contacts:
            print(contact)


# Create some custom data objects representing contacts
contact1 = Contact("Anup Singh", "anup@example.com", "1234567890")
contact2 = Contact("Anuj Singh", "anuj@example.com", "9876543210")

# Create an address book and add contacts to it
address_book = AddressBook()
address_book.add_contact(contact1)
address_book.add_contact(contact2)

# page : 1- Concurrent user

# Display all contacts in the address book
print("Contacts in Address Book:")
address_book.display_contacts()

# Find a contact by name
search_name = "John Doe"
found_contact = address_book.find_contact_by_name(search_name)
if found_contact:
    print(f"Found contact: {found_contact}")
else:
    print(f"No contact found with name: {search_name}")

















































































