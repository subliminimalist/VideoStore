import MainController

def main_menu():
    print("Options:\n")
    print("1. Search for Client by Id\n")
    print("2. Search for Client by email\n")
    return input("Enter Your Selection: ")

print("*******WELCOME TO OUR VIDEO STORE*********\n\n")

selection = main_menu()
customer = ''
if selection == '1':
    customer_id = input("Enter Customer Id: ")
    try:
        customer = MainController.get_customer_by_id(customer_id)
    except Exception as e:
        print(e)
        main_menu()

elif selection == '2':
    email = input("Enter email address: ")
    try:
        customer = MainController.get_customer_by_email(email)
    except Exception as e:
        print(e)
        main_menu()
print("Customer Found: " + customer.get_display_name())


