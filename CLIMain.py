import psycopg2
import psycopg2.extras
import Actor


def getActorList(conn, last_name, first_name):
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
        command = "select f.* from film_actor fa join film f on f.film_id = fa.film_id where fa.actor_id = " + str(actor.actor_id)
        film_cur.execute(command)
        for film in film_cur:
            actor.films.append(film)
        actor_array.append(actor)
    return actor_array


testing = True
if not testing:
    last_name = input("Input actor's last name: ")
    first_name = input("Input actor's first name: ")
else:
    last_name = "Guiness"
    first_name = "Penelope"
conn = psycopg2.connect("dbname=video_store host=video-store.cpcwhvi5lixx.us-east-2.rds.amazonaws.com user=dev password=admindev")
actor_list = getActorList(conn, last_name, first_name)
for actor in actor_list:
    print("Actor's name is: " + actor.getDisplayName())
    print("or maybe it's: " + actor.getReportName())
    print("He or she has been in these films: ")
    for film in actor.films:
        print("\t" + film[1] + ", " + str(film[3]))

