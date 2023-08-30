class Contact:

    def __init__(self, name, phone,email) -> None:
        self.name = name
        self.phone = phone
        self.email = email
    
    def __str__(self) -> str:
        return f"""
        name: {self.name}
        phone: {self.phone}
        email: {self.email}
        """
    @property
    def get_name(self):
        return self.name

class ContactManager:
    contacts_list = []

    @classmethod
    def add_contact(cls, name, number, email=None):
        contact = Contact(name,number,email)
        cls.contacts_list.append(contact)
        print(f"Contact '{name}' added successfully!")

    @classmethod
    def remove_contact(cls,name):
        for contact in cls.contacts_list:
            if contact.get_name == name:
                cls.contacts_list.remove(contact)
                print(f"Contact '{name}' deleted successfully!")
                return
        print(f"Contact '{name}' not found!")

    @classmethod
    def search_contact(cls,name): 
        for contact in cls.contacts_list:
            if contact.get_name == name:
                return contact
        return None
    
    @classmethod
    def display_contacts(cls):
            if len(cls.contacts_list) != 0:
                for contact in cls.contacts_list:
                    print(contact)
            else:
                print("No contacts found")


# c1 = Contact('ibrahim',775,'dss@sf')
# print(c1)
# ContactManager.add_contact('ibrahim',775,'dss@sf')
# ContactManager.add_contact('aswh',222)
# ContactManager.add_contact('khaled',222,'dss@wef')

# print("_"*40)

# print(ContactManager.search_contact('khaled'))
# print("_"*40)

# ContactManager.contacts_list.clear()
# ContactManager.display_contacts()

def main():

    while True:
        print('-'*50,"\nContact Manager")
        print("1. Add Contact")
        print("2. Remove Contact")
        print("3. Search Contact")
        print("4. Display Contacts")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        match choice:
            case '1':
                name = input("Enter name: ")
                number = input("Enter number: ")
                email = input("Enter Email: ")
                ContactManager.add_contact(name, number, email)
            case '2':
                name = input("Enter name: ")
                ContactManager.remove_contact(name)
            case '3':
                name = input("Enter name: ")
                print(ContactManager.search_contact(name))
            case '4':
                ContactManager.display_contacts()
            case '5':
                print("Exiting...")
                break
            case _:
                print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()