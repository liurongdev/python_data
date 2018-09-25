

import csv


filename="data/sitka_weather_07-2014.csv"

with open(filename) as f:
    content=csv.reader(f)
    header_row=next(content)

    for index,column_header in enumerate(header_row):
        print(index,column_header)

