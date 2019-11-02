# Import requests, shutil python module.
import csv

with open('results.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        print(row[0])
csvFile.close()