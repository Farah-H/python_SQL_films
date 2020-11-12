import csv
import pydoc
from DB_connection_class import DB_connection

# instantiating the DB_connection class to to be able to use it 
db_instance = DB_connection()


with open("imdbtitles.csv", "r") as csv_file:
    film_data = csv.reader(csv_file)
    for row in film_data:
        print(row)

    # make a table from the headings in the csv 
    db_instance.create_table(farah_movies, film_data[0])

with open("new_movie_file.csv",)

# # template to write to file 
# with open ('new_json_file.json', 'w') as jsonfile: # w gives write permission
#     json.dump(car_data, jsonfile)
    