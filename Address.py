class Address:
    def __init__(self, values):
        self.address = values[0]
        self.address2 = values[1]
        self.district = values[2]
        self.city_id= values[3]
        self.postal_code = values[4]
        self.phone = values[5]
        self.last_update = values[6]

    def add_address(self,conn):
        cur=conn.cursor()
        command = "INSERT INTO address (address,address2,district,city_id,postal_code,phone) VALUES (%s,%s,%s,%s,%s,%s) RETURNING id"
        cur.execute(command,(self.address,self.address2,self.district,self.city_id,self.postal_code,self.phone))
        return cur.fetchone()[0]
