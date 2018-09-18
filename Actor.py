import psycopg2
import psycopg2.extras


class Actor:
    def __init__(self, actor_id,  first_name, last_name, last_update):
        self.actor_id = actor_id
        self.first_name = first_name
        self.last_name = last_name
        self.last_update = last_update
        self.films = []

    def getDisplayName(self):
        return self.first_name + ' ' + self.last_name

    def getReportName(self):
        return self.last_name + ', ' + self.first_name

    # @staticmethod
    # def getActorList(conn, last_name, first_name):
    #     cur = conn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    #     command = "Select * from actor where last_name = %s"
    #     if first_name:
    #         command = command + " and first_name = %s"
    #     data = (last_name, first_name, )
    #     cur.execute(command, data)
    #     actor_array = []
    #     for record in cur:
    #         actor_array.append(Actor.__init__(record['actor_id'], record['first_name'], record['last_name'],\
    #                                           record['last_update']))
    #     return actor_array
    #
