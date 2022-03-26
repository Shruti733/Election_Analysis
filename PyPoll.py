import csv
import os
#Assign a variable to load a file from a path
file_to_load = os.path.join('Resources','election_results.csv')
print(file_to_load)
election_data = open(file_to_load)
print(election_data)

file_to_save = os.path.join("Analysis","election_analysis.txt")
with open(file_to_save,"w") as Analysis_data:
    Analysis_data.write("Counties in the Election\n")
    Analysis_data.write("------------------------\n")
    Analysis_data.write("Arapahoe\n")
    Analysis_data.write("Devnver\n")
    Analysis_data.write("Jefferson\n")

 # To do: read and analyze the data here
# Read the file object with the reader function.
file_reader = csv.reader(election_data)
# print the header row
Headers = next(file_reader)
for Row in file_reader:
    print(Row)
    

 # Print each row in the CSV file.
