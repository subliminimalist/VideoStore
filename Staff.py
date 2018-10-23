import psycopg2
import psycopg2.extras


class Staff:
    def __init__(self, staff_id,  first_name, last_name, password):
        self.staff_id = staff_id
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
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
