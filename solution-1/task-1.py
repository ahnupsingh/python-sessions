class AddressBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email, address):
        self.contacts[name] = {'phone': phone, 'email': email, 'address': address}

    def get_contact(self, name):
        contact = self.contacts.get(name)
        if contact:
            return contact
        return "Contact not found"

    def update_contact(self, name, phone, email, address):
        if name in self.contacts:
            self.contacts[name] = {'phone': phone, 'email': email, 'address': address}
        else:
            return "Contact not found"

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
        else:
            return "Contact not found"


address_book = AddressBook()
address_book.add_contact("Alice", "123456789", "alice@example.com", "123 Street, City")
address_book.add_contact("Bob", "987654321", "bob@example.com", "456 Street, Town")

print(address_book.get_contact("Alice"))
print(address_book.get_contact("Charlie"))

address_book.update_contact("Bob", "111111111", "bob@example.com", "456 Street, Town")
print(address_book.get_contact("Bob"))

address_book.delete_contact("Alice")
print(address_book.get_contact("Alice")) 
