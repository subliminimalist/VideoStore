import MainController
import Customer

def customer_search_menu():
    print("Customer Search Options:\n")
    print("1. Search for Client by Id\n")
    print("2. Search for Client by email\n")
    return customer_search(input("Enter Your Selection (X to exit): "))



def customer_search(selection):
    if selection == '1':
        customer_id = input("Enter Customer Id: ")
        search_customer = MainController.get_customer_by_id(customer_id)
    elif selection == '2':
        email = input("Enter email address: ")
        search_customer = MainController.get_customer_by_email(email)
    return search_customer

print("*******WELCOME TO OUR VIDEO STORE*********\n\n")

customer = None
customer = customer_search_menu()

print("Customer Found: " + customer.get_display_name())


