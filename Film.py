import psycopg2
import psycopg2.extras


class Film:
    def __init__(self, film_id,title,description,release_year,language_id,rental_duration,rental_rate,length,replacement_cost,rating,last_updated,special_features,fulltext):
        self.film_id = film_id
        self.title = title
        self.description = description
        self.release_year = release_year
        self.language_id = language_id
        self.rental_duration = rental_duration
        self.rental_rate = rental_rate
        self.length = length
        self.replacement_cost = replacement_cost
        self.rating = rating
        self.last_updated = last_updated
        self.special_features = special_features
        self.fulltext = fulltext
        self.films = []

    def getDisplayTitle(self):
        return self.title + ' ' + self.release_year

    def getReportName(self):
        return self.last_name + ', ' + self.first_name
