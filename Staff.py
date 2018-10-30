import psycopg2
import psycopg2.extras


class Staff:
    def __init__(self, values):
        self.staff_id = values[0]
        self.first_name = values[1]
        self.last_name = values[2]
        self.password = values[3]
    def get_staff_by_ID(cur,staff_id):
        command = "Select staff_id, last_name, first_name, password from staff where staff_id = %s" % staff_id
        cur.execute(command)
        staff = cur.fetchone()

        check_password = input("Input your password:  ")
        print (staff[3])
        if check_password == staff[3]:
            print ("Welcome %s %s." % (staff[2],staff[1]))
        else:
            print("Password incorrect.")
    def get_staff_by_name(cur, last_name,first_name):
        command = "Select staff_id, last_name, first_name, password from staff where last_name = %s AND first_name = %s" % (last_name,first_name)
        print(command)
        cur.execute(command)
        staff = cur.fetchone()

        check_password = input("Input your password:  ")
        print (staff[3])
        if check_password == staff[3]:
            print ("Welcome %s %s." % (staff[2],staff[1]))
        else:
            print("Password incorrect.")
    def authenticate_user(self,password):
        return password == self.password
