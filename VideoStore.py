import MainController
import Customer
import Staff

staff = None
customer = None
store_id = 1
def login_menu():
    staff_id = int(input("Type your staff ID:  "))
    input_password = input("Type your password:  ")
    staff = MainController.get_staff_by_ID(staff_id)
    is_authenticated = staff.authenticate_user(input_password)
    return is_authenticated

def options_menu():
    print("1. Customer search menu\n")
    print("2. Video search menu\n")
    print("3. Add new customer\n")
    selection = input("Enter Your Selection: ")
    if selection == 1:
        customer_search_menu()
    elif selection == 2:
        #video_search_menu()
    elif selection == 3:
        add_customer():
    else:
        print("That is not a valid option.")
        options_menu()

def add_customer():
    last_name = input("Last name:  ")
    first_name = input("First name:  ")
    address = input("Street Address:  ")
    address2 = input("Apt. number:  ")
    city = input("city:  ")
    district = input("district/state:  ")
    postal_code = input("postal code:  ")
    email = input("email:  ")
    phone_number = input("phone number:  ")
    country = input("country:  ")

    MainController.add_new_customer(last_name,first_name,address,address2,city,district,postal_code,email,phone_number,store_id,country)

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
is_authenticated = False
while is_authenticated == False:
    is_authenticated = login_menu()
while is_authenticated == True:
    options_menu()

customer = customer_search_menu()

print("Customer Found: " + customer.get_display_name())


