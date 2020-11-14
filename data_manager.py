# importing necessary files/ modules
import csv
from csv_manager_class import Csv_manager

# instantiating the csv class to to be able to use it
db_instance = Csv_manager()

# uploading the csv to SQL server (the cleanup etc is all done through the class)
db_instance.upload_to_DB()

# importing data from our DB and saving it to a new file
with open("new_movie_file.csv","w") as new_file:
    # with information from our select statement
    info_from_db = db_instance.select_info(table_name,'*').fetchall()
    print(info_from_db) # to check things are working
    write_file = csv.writer(info_from_db, new_file)
    print("DB successfully exported to csv!")