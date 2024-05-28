class AddressBook:

    def __init__(self):
        self.address_book = {}

    def add_contact(self, name, phone, email, address):
        self.address_book.update(
            {name: {"phone": phone, "email": email, "address": address}}
        )

    def get_contact(self, name):
        if name in self.address_book.keys():
            return self.address_book[name]
        else:
            print("Contact not found")

    def update_contact(self, name, phone, email, address):
        if name in self.address_book.keys():
            self.address_book.update(
                {name: {"phone": phone, "email": email, "address": address}}
            )
        else:
            print("Contact not found")

    def delete_contact(self, name):
        if name in self.address_book.keys():
            self.address_book.pop(name)
        else:
            print("Contact not found")


add1 = AddressBook() # Initialize an address book object
add1.add_contact("Arya", 9812345678, "aserar@adsad.com", "Jawalakhel")
add1.add_contact("Ram", 9854123654, "dar@ad.com", "Gwarko")
print(add1.get_contact("Arya"))
print(add1.address_book)
add1.update_contact("Arya", 9845511616, "Arays@jknasfd.com", "asknds")
print(add1.address_book)
add1.delete_contact("Aasdrya")
print(add1.address_book)
