# importing necessary files/ modules
import csv
from DB_connection_class import DB_connection

# instantiating the DB_connection class to to be able to use it
db_instance = DB_connection()

# this function will be used for csv formatting
def check_alpha(word):
    # checks that the word doesn't contain any illegal characters especially that weird i 
        output_word = []
        for letter in word:
            if letter.isalpha() and not in "´╗┐":
                output_word.append(letter)
        return "".join(output_word)
        

# reading the csv file
with open("imdbtitles.csv", "r") as csv_file:
    film_data = list(csv.reader(csv_file))
    print(film_data[0])
    # filmdata[0] is a list of column headings

    # make a table from the headings in the csv, it's aready comma seperated so don't need to join or amything
    # creating a list which contains 8 VARCHAR (255)
    # cleaner way would be to just make a row in the csv for datatypes but too lazy 
    data_types = ["VARCHAR (255)" for column in range(0,len(film_data[0]))]
    print(data_types)


    # using dictionary comprehension to convert lists to dictionary 
    # remembering that CREATE function takes a dict
    columns_dict = {film_data[0][i]: data_types[i] for i in range(len(film_data[0]))} 
    
    # cleanup for csv
    # this just removes any weird characters from the table_name
    for i in range(len(film_data[0])):
        film_data[0][i] = check_alpha(film_data[0][i])
    
    
    print(columns_dict)
    db_instance.create_table("farah_movies", columns_dict)
    print("Table successfully created.")
    



# writing new csv file
with open("new_movie_file.csv","w") as new_file:
    # with information from our select statement
    info_from_db = db_instance.select_info(table_name,'*').fetchall()
    print(info_from_db)
    write_file = csv.writer(info_from_db, new_file)
    print("DB successfully exported to csv!")