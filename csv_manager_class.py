import csv 
from DB_connection_class import DB_connection

class Csv_manager(DB_connection):

    # initialising child class
    def __init__(self):
        super().__init__()
    

    # checks the the word doesn't contain any characters which aren't allowed in SQL
    # if a character isn't allowed, it just ignores it
    def check_alpha(word):
        output_word = []
        for letter in word:
            if letter.isalpha() and letter not in "´'╗┐`":
                output_word.append(letter)
        # really wish this wasn't necessary
        return "".join(output_word)
    
    def open_csv(self):
        # reading and putting the csv file into a list 
        with open("imdbtitles.csv", "r") as csv_file:
            film_data = list(csv.reader(csv_file))
            print(film_data[0])
            return film_data
            # filmdata[0] is a list of column headings
             
    
    # cleanup for csv
    # this just removes any weird characters from the table_name   
    def clean_csv(self):
        film_data = self.open_csv()
        for i in range(len(film_data[0])):
            film_data[0][i] = check_alpha(film_data[0][i])
        return  film_data

    # make a table from the headings in the csv and add info to it
    def upload_to_DB(self):
        
        film_data = self.clean_csv
        # creating a list which contains VARCHAR (255) for datatypes
        data_types = ["VARCHAR (255)" for column in range(0,len(film_data[0]))]

        # using dictionary comprehension to convert lists to dictionary 
        # remembering that CREATE function takes a dict
        columns_dict = {film_data[0][i]: data_types[i] for i in range(len(film_data[0]))} 
        self.create_table("farah_movies", columns_dict)
        print("Table successfully created.")
    

