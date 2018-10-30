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

    def __init__(self, values):
        self.store_id = values[0]
        self.first_name = values[1]
        self.last_name = values[2]
        self.email = values[3]
        self.address_id = values[4]

    def add_customer(self,conn):
        cur=conn.cursor()
        command = "INSERT INTO customer (store_id,first_name,last_name,email,address_id) VALUES (%s,%s,%s,%s,%s)"
        cur.execute(command,(self.store_id,self.first_name,self.last_name,self.email,self.address_id))


    def get_display_name(self):
        return self.first_name + " " + self.last_name
