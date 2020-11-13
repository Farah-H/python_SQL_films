# Python DB SQL Abstraction Task 
## Task 
- read the text file and create object
- save object in DB
- Load that from DB and create object
- output object to text file

### Acceptance Criteria:

- able to take in 10 film names in text file and save to db
- able to load data from DB and create text file with names
## Prerequisites
## Pre-Requisites
__Necessary:__ You must have python installed.  Also you must install pyodbc using `pip install pyodbc`in your terminal. 
__Optional:__ It is easier to complete this task when using a code editor, such as Visual Studio Code or PyCharm. You can learn how to [install VSC](https://docs.microsoft.com/en-us/visualstudio/install/install-visual-studio?view=vs-2019) or [install PyCharm](https://www.jetbrains.com/help/pycharm/quick-start-guide.html) using these hyperlinks. 


## Steps
1. Set up a class, in a new file, whose purpose is to establish a connection with the DB 
```python
# import the necessary modules
import pyodbc

# the purpose of this class is to estabish a connectinon with the Northwind DB
# and to contain CRUD functions
class DB_connection:

    # initialising the class with the login details 
    # this can be incremented to take them as user inputs, but i'll leave it for convenience
    def __init__(self):
        self.server = "databases1.spartaglobal.academy"
        self.database = "Northwind"
        self.username = "**"
        self.password = "****"
        
    # function to establish connection with the server
    def establish_connection(self):
        connection = pyodbc.connect(
            f"DRIVER=ODBC Driver 17 for SQL Server;SERVER={self.server};DATABASE={self.database};UID={self.username};PWD={self.password}"
        )
        cursor = connection.cursor()
        return cursor
```
2. In this class we have created functions for managing the database. This could (and probably should) have been done in a seperate class, which queries the database.
```python
# CREATE
    # takes in table_name and a dict of column_name:data_type k/v pairs
    def create_table(self,table_name, column_data):
        # establish connection
        cursor = self.establish_connection()
        # this splits the dict into two lists (keys and values), then combines these lists at their indexes to make a tuple
        # not necessary for there to be a tuple middleman, but zip does this combination easily
        # because join doesn't like dicts, so instead we give it a tuple of 'key value, key value , etc.'
        SQL_command = f"CREATE TABLE {table_name} ({', '.join([f'{key} {value}' for key, value in zip(column_data.keys(), column_data.values())])})"
        print(SQL_command)
        return cursor.execute(SQL_command)
    
    # INSERT
    # takes in table_name and a dict of column_name : data k/v pairs 
    def insert_info(self,table_name,**kwargs):
        # establish connection with DB
        cursor = self.establish_connection()
        # loops through dictionary to insert data, kind of inefficient but works 
        for column_name, data in kwargs.items():
            return cursor.execute(f"INSERT INTO {table_name} ({column_name}) VALUES ({data});")


    #SELECT
    def select_info(self,table_name,*args):
    # establish connection with DB
        cursor = self.establish_connection()
        return cursor.execute(f"SELECT {','.join(column_name for column_name in args)} FROM {table_name};")
    
    # UPDATE
    def update_info(self,column_name,new_info, condition_sring):
        cursor = self.establish_connection()
        return cursor.execute(f"UPDATE {table_name} SET {column_name} = {new_info} WHERE {condition_sring};")


    # DELETE
    def drop_table(self,table_name):
        cursor = self.establish_connection()
        return cursor.execute(f"DROP TABLE {table_name};")
```

3. Save the `imdb_films.csv`in the same folder as your `DB_connection` file.
4. In the same folder, create a file called `data_manager`, the purpose of which is to manage your csv (open , export etc)
5. Import the necessary modules, one of which is `csv`which should be automatically installed. Also, instantiate your DB_connection class.
```python
# importing necessary files/ modules
import csv
from DB_connection_class import DB_connection

# instantiating the DB_connection class to to be able to use it
db_instance = DB_connection()
```

6. There were some issues with the csv file, e.g characters which are not allowed in SQL, therefore create a function to deal with them: 
```python
# this function will be used for csv formatting
def check_alpha(word):
    # checks that the word doesn't contain any illegal characters especially that weird i 
        output_word = []
        for letter in word:
            if letter.isalpha() and not in "´╗┐":
                output_word.append(letter)
        return "".join(output_word)
```
7. Now we can open and read the csv file, using the `csv` module and its attributes:
```python
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
    # remembering that the CREATE function takes a dict
    columns_dict = {film_data[0][i]: data_types[i] for i in range(len(film_data[0]))} 
    
    # cleanup for csv
    # this just removes any weird characters from the table_name
    for i in range(len(film_data[0])):
        film_data[0][i] = check_alpha(film_data[0][i])
    
    
    print(columns_dict)
    db_instance.create_table("farah_movies", columns_dict)
    print("Table successfully created.")
```
8. Finally, the following function can be used to `SELECT` info from our new table, which is now in the DB, and export it to a csv file.
```python

# writing new csv file
with open("new_movie_file.csv","w") as new_file:
    # with information from our select statement
    info_from_db = db_instance.select_info(table_name,'*').fetchall()
    print(info_from_db)
    write_file = csv.writer(info_from_db, new_file)
    print("DB successfully exported to csv!")
```