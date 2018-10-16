import psycopg2
import psycopg2.extras
import Actor
import Customer
import UtilityMethods

connection_string = "dbname=video_store host=video-store.cpcwhvi5lixx.us-east-2.rds.amazonaws.com user=dev password=admindev"

def get_actor_list(conn, last_name, first_name):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    command = "Select * from actor where last_name = %s"
    if first_name != '':
        command = command + " and first_name = %s"
    data = (last_name, first_name,)
    cur.execute(command, data)
    actor_array = []
    for record in cur:
        actor = Actor.Actor(record[0], record[1], record[2], record[3])
        film_cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        command = "select f.* from film_actor fa join film f on f.film_id = fa.film_id"
        film_cur.execute(command)
        for film in film_cur:
            actor.films.append(film)
        actor_array.append(actor)
    return actor_array

def get_connection():
    return psycopg2.connect(connection_string)


def get_customer_by_id(customer_id):
    conn = get_connection()
    cur = conn.cursor()
    statement = "select * from customer where customer_id = %s"
    cur.execute(statement, str(customer_id))
    if cur.rowcount > 1:
        raise Exception('Returned more than one record!')
    if cur.rowcount == 0:
        raise Exception('No results returned')
    if cur.rowcount == 1:
        return Customer.Customer(cur.fetchone())

def get_customer_by_email(email):
    if not UtilityMethods.is_email():
        raise Exception(email + 'is not a valid email')
    conn = get_connection()
    cur = conn.cursor()
    statement = "select * from customer where email = '" + UtilityMethods.sanitize_input(email) + "'"
    cur.execute(statement, email)
    if cur.rowcount > 1:
        raise Exception('Returned more than one record!')
    if cur.rowcount == 0:
        raise Exception('No results returned')
    if cur.rowcount == 1:
        return Customer.Customer(cur.fetchone())





#
# testing = True
# if not testing:
#     last_name = input("Input actor's last name: ")
#     first_name = input("Input actor's first name: ")
# else:
#     start = datetime.datetime.now()
#     last_name = "Guiness"
#     first_name = "Penelope"
# conn = psycopg2.connect("dbname=video_store host=video-store.cpcwhvi5lixx.us-east-2.rds.amazonaws.com user=dev password=admindev")
# actor_list = get_actor_list(conn, last_name, first_name)
# for actor in actor_list:
#     print("Actor's name is: " + actor.getDisplayName())
#     print("or maybe it's: " + actor.getReportName())
#     print("He or she has been in these films: ")
#     for film in actor.films:
#         print("\t" + film[1] + ", " + str(film[3]))
#     print(datetime.datetime.now() - start)
