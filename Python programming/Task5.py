import json

# File to store contact data
CONTACT_FILE = 'contacts.json'

def load_contacts():
    """Load contacts from a JSON file."""
    try:
        with open(CONTACT_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_contacts(contacts):
    """Save contacts to a JSON file."""
    with open(CONTACT_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    """Add a new contact."""
    name = input("Enter the contact's name: ").strip()
    phone = input("Enter the contact's phone number: ").strip()
    email = input("Enter the contact's email: ").strip()
    address = input("Enter the contact's address: ").strip()
    
    contacts[name] = {
        'phone': phone,
        'email': email,
        'address': address
    }
    print(f"Contact '{name}' added successfully.")

def view_contacts(contacts):
    """Display all contacts."""
    if not contacts:
        print("No contacts found.")
        return

    print("\nContact List:")
    for name, info in contacts.items():
        print(f"Name: {name}, Phone: {info['phone']}")

def search_contact(contacts):
    """Search for a contact by name or phone number."""
    search_term = input("Enter name or phone number to search: ").strip()
    found = False

    for name, info in contacts.items():
        if search_term in name or search_term in info['phone']:
            print(f"\nName: {name}")
            print(f"Phone: {info['phone']}")
            print(f"Email: {info['email']}")
            print(f"Address: {info['address']}\n")
            found = True

    if not found:
        print("No contacts found with that search term.")

def update_contact(contacts):
    """Update an existing contact."""
    name = input("Enter the name of the contact to update: ").strip()
    
    if name in contacts:
        print(f"Updating contact '{name}'.")
        phone = input("Enter new phone number: ").strip()
        email = input("Enter new email: ").strip()
        address = input("Enter new address: ").strip()

        contacts[name] = {
            'phone': phone,
            'email': email,
            'address': address
        }
        print(f"Contact '{name}' updated successfully.")
    else:
        print(f"No contact found with the name '{name}'.")

def delete_contact(contacts):
    """Delete an existing contact."""
    name = input("Enter the name of the contact to delete: ").strip()
    
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully.")
    else:
        print(f"No contact found with the name '{name}'.")

def main():
    contacts = load_contacts()

    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Choose an option (1-6): ").strip()

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            save_contacts(contacts)
            print("Contacts saved. Exiting...")
            break
        else:
            print("Invalid choice. Please choose a number between 1 and 6.")

if __name__ == "__main__":
    main()
