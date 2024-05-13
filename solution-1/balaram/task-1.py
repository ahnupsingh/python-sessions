# AddressBook class

class AddressBook:

    def __init__(self):
        self.address_book = {}

    def add_contact(self, name: str, phone: str=None, email: str=None, address: str=None) -> None:
        """
        Takes name, phone, email and address and creates a new record in address_book
        Arguments:
            name (str): Name of the contact
            phone (str): Phone of the contact
            email (str): Email of the contact
            address (str): Address of the contact
        Return:
            (str): Message  
        """
        if name in self.address_book:
            self.success("Create Duplicate Data")
        else:
            self.success("Create New Data")
        
        self.address_book[name] = {
                'phone': phone,
                'email': email,
                'address': address
            }

        return None

    def get_contact(self, name: str) -> dict:
        if not self.contact_in_address_book(name):
            return self.raise_contact_not_found()
        else:
            return {name: self.address_book[name]}

    def update_contact(self, name: str, phone: str=None, email: str=None, address: str=None):
        if phone is None:
            phone = self.address_book[name]['phone'] 
        if email is None:
            email = self.address_book[name]['email'] 
        if address is None:
            address = self.address_book[name]['address'] 

        if self.contact_in_address_book(name):
            self.address_book[name] = {
                'phone': phone,
                'email': email,
                'address': address
            }
        else:
            return self.raise_contact_not_found()

    
    def contact_in_address_book(self, name: str) -> bool:
        if self.address_book.get(name) is not None:
            return True
        return False
    

    def delete_contact(self, name: str) -> str:
        if self.contact_in_address_book(name):
            self.address_book.pop(name)
            self.success("Delete")
        else:
            return self.raise_contact_not_found() 

    @staticmethod
    def success(activity_name: str) -> None:
        print(f"{activity_name} Success")
        return None

    @staticmethod
    def raise_contact_not_found() -> str:
        msg =  "Contact Not Found"
        print(msg)
        return msg
    






book1 = AddressBook()
book1.add_contact('anish', '984747', 'email@email.com', 'here')
book1.add_contact('hari', '984747', 'email@email.com', 'here')
# print(book1.get_contact("anish"))
book1.delete_contact('hari')
book1.update_contact("anish", "9999", email='nebulaanish@gmail.com')

