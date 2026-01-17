from contact import Contact

class Contact_List:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def display_contacts(self):
        print(f"{'Name':<15} {'Email':<25} {'Telephone'}")
        print("-" * 50)
        for contact in self.contacts:
            print(contact)
