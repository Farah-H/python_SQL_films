import pyodbc

# the purpose of this class is to estabish a connectinon with the Northwind DB
# and to contain CRUD functions
class DB_connection:

    # initialising the class with the login details 
    # this can be incremented to take them as user inputs, but i'll leave it for convenience
    def __init__(self):
        self.server = "databases1.spartaglobal.academy"
        self.database = "Northwind"
        self.username = "SA"
        self.password = "Passw0rd2018"


    # function to establish connection with the server
    def establish_connection(self):
        connection = pyodbc.connect(
            f"DRIVER=ODBC Driver 17 for SQL Server;SERVER={self.server};DATABASE={self.database};UID={self.username};PWD={self.password}"
        )
        cursor = connection.cursor()
        return cursor

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