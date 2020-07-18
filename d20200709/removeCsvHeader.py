# Remove the header from all CSV files in the current working directory.
import csv
import os

os.makedirs("headerRemoved", exist_ok=True)

# Loop through every file in the current working directory.
for csvFilename in os.listdir("."):
    if not csvFilename.endswith(".csv"):
        continue

    print("Removing header from" + csvFilename + "...")

    # Read the CSV file in (skipping first row).
    csvRows = []
    csvFileObj = open(csvFilename)
    readerObjs = csv.reader(csvFileObj)
    for readerObj in readerObjs:
        if readerObjs.line_num == 1:
            continue
        csvRows.append(readerObj)
    csvFileObj.close()

    # Write out the CSV file.
    csvFileObj = open(os.path.join("headerRemoved", csvFilename), "w", newline="")
    csvWriter = csv.writer(csvFileObj)
    for row in csvRows:
        csvWriter.writerow(row)
    csvFileObj.close()
