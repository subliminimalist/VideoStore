class Customer:
    def __init__(self, values):
        self.customer_id = values[0]
        self.store_id = values[1]
        self.first_name = values[2]
        self.last_name = values[3]
        self.email = values[4]
        self.address_id = values[5]
        self.activebool = values[6]
        self.create_date = values[7]
        self.last_update = values[8]
        self.active = values[9]

    def get_display_name(self):
        return self.first_name + " " + self.last_name
    
