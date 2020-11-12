import csv

with open('imdbtitles.csv', newline= '') as csv:
    read_file = csv.reader(csv, dialect='excel')
    for row in read_file:
        print(', '.join(row))