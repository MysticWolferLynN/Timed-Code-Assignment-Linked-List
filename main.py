from LinkedList import Linkedlist

def main():
    clients = Linkedlist()

    while True:
        print("\nBoudreaux's Barbershop")
        print("Type the number for the action you wish to perform and then hit Enter.")
        print("1. Add a new client")
        print("2. Display a list of all current clients")
        print("3. Search for a client")
        print("4. Delete a client")
        print("5. Quit")

        choice = input("What do you want to do?").strip()

        if choice == "1":
            name = input("Provide the client's name: ").strip()
            phone = input("Provide the client's phone number: ").strip()
            dob = input(
                    "Provide the client's D.O.B. in MMDDYYYY format: "
            ).strip()

            if not name or not phone or not dob:
                print("All clients imformation is required.")
            else:
                client = {
                    "name": name,
                    "phone": phone,
                    "dob": dob
                }

                clients.add_client(client)
                print("You've added a new client!")

        elif choice == "2":
            clients.display_clients()

        elif choice == "3":
            name = input("Enter the client's name to search for: ").strip()

            client = clients.search_client(name)

            if client is not None:
                print("\nClient found!")
                print(f"Name: {client['name']}")
                print(f"Phone Number: {client['phone']}")
                print(f"D.O.B.: {client['phone']}")
            else:
                print("Client not found.")

        elif choice == "4":
            name = input("Enter the client's name to delete: ").strip()

            if clients.delete_client(name):
                print("Client deleted Successfully!")
            else:
                print("Client not found.")

        elif choice == "5":
            print("Thank you for using Boudreaux's Barbershop!")
            break

        else:
            print("I'm sorry, that is not an allowed action.")

if __name__ == "__main__":
    main()
