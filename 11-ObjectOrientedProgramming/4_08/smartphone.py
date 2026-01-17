from contact import Contact
from contact_list import Contact_List

def main():
    my_contacts = Contact_List()

    my_contacts.add_contact(Contact("Adam Małysz", "adam.malysz@onet.pl", "555234000"))
    my_contacts.add_contact(Contact("Mariusz Pudzianowski", "mariusz.pudzianowski@o2.pl", "232000199"))
    my_contacts.add_contact(Contact("Leo Messi", "leo.messi@gmail.com", "222999100"))
    my_contacts.add_contact(Contact("Krystyna Śmigło", "krystyna.smiglo@poczta.pl", "100200300"))

    my_contacts.display_contacts()

if __name__ == "__main__":
    main()
