from Node import Node

class Linkedlist:
    def __init__(self):
        self.head = None

    def add_client(self, client):
        new_node = Node(client)
                        
        if self.head is None:
            self.head = new_node
        else:
            current = self.head

            while current.next is not None:
                current = current.next

                current.next = new_node

            def display_clients(self):
                if self.head is None:
                    print("There are no clients.")
                    return

                current = self.head
                while current is not None:
                    client = current.client

                    print(f"Name: {client['name']}")
                    print(f"Phone Number: {client['phone']}")
                    print(f"D.O.B.: {client['dob']}")
                    print("________________________")

                    current = current.next

            def search_client(self, name):
                cuurent = self.head

                while current is not None:
                    if current.client["name"].lower() == name.lower():
                        return current.client

                    current = current.next

                    return None

                def delete_client(self, name):
                    current = self.head
                    previous = None
                    
                    while current is not None:
                        if current.client["name"].lower() == name.lower():

                            if previous is None:
                                self.head = current.next
                            else:
                                previous.next = current.next

                                return True
                            previous = current
                            current = current.nexy

                    return False

