from prettytable import PrettyTable as pt


class ContactBook:
    def __init__(self):
        self.contacts : dict[int, dict] = {}

    def add_contact(self, id: int, name: str, phone: str = None, email: str = None):
        """Add a contact to the contact book.

        Args:
            id (int): id of contact to be added.
            name (str): name of the contact to be added.
            phone (str): phone of the contact to be added.
            email (str, optional): email of the contact to be added. Defaults to None.
        """
        # id is unique
        if id in self.contacts:
            print("Contacts Already Exists!")
            return

        self.contacts[id] = {'name': name, 'phone': phone, 'email': email}
        print("Contact added successfully!")

    def view_contact(self):
        """
        View all contacts in the contact book.
        """
        if not self.contacts:
            print("Contact book is empty.")
            return

        table = pt()
        table.field_names = ["Id", "Name", "Phone", "Email"]
        
        for id, info in self.contacts.items():
            table.add_row([id, info['name'], info['phone'], info['email'] or '-'])
        print(table)

    def delete_contact(self, id:int):
        """Delete a contact from the contact book.

        Args:
            id (int): id of the contact to the delete.
        """
        if id in self.contacts:
            del self.contacts[id]
            print("Contact deleted successfully!")
        else:
            print("Contact not found!")

    def update_contact(self, id:int, name:str = None, phone:str = None, email:str = None):
        """Update a contact in the contact book

        Args:
            id (int): id of the contact to be updated.
            name (str, optional): name of the contact to be updated. Defaults to None.
            phone (str, optional): phone of the contact to be updated. Defaults to None.
            email (str, optional): email of the contact to updated. Defaults to None.
        """
        if id in self.contacts:
            if name:
                self.contacts[id]['name'] = name
            if phone:
                self.contacts[id]['phone'] = phone
            if email:
                self.contacts[id]['email'] = email

            print("Contact updated successfully!")
            return

        print("Contact not found!")


if __name__ == "__main__":

    book = ContactBook()

    while True:
        print('\n\nwelcome to contacts book application!')
        print('1. Add contact\n2. Edit contact\n3. View contact\n4. Delete contact\n5. Quit')

        user_choice = input("please choose an option: ")
        if user_choice == '5':
            break

        if user_choice == '1':
            id = int(input("\nEnter contact id: "))
            name = input("Enter contact name: ")
            phone = input("Enter contact phone: ")
            email = input("Enter contact email: ")

            book.add_contact(id, name, phone, email)

        elif user_choice == '2':
            id = int(input("\nEnter contact id: "))
            name = input("Enter contact name: ")
            phone = input("Enter contact phone: ")
            email = input("Enter contact email: ")

            book.update_contact(id, name, phone, email)

        elif user_choice == '3':
            print("\n\nList of contacts: ")
            book.view_contact()

        elif user_choice == '4': 
            id = int(input("\nEnter contact id: "))
            book.delete_contact(id)
