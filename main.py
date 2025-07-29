import pandas as pd
import matplotlib.pyplot as plt
from openpyxl import load_workbook
from openpyxl.drawing.image import Image
import glob

def parse_bank_csv(filename):
    # Read the whole file as text
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # First few lines of CSV file are metadata - extract this info
    metadata = {}
    for line in lines:
        if line.startswith("Date,Unique Id"):  # this means the table starts here
            break
        # Parse known metadata patterns
        if line.startswith("Created date / time"):
            metadata["created"] = line.split(":")[1].strip()
        elif line.startswith("Bank"):
            metadata["bank_info"] = line.strip()
        elif line.startswith("From date"):
            metadata["from_date"] = line.split()[2].strip()
        elif line.startswith("To date"):
            metadata["to_date"] = line.split()[2].strip()
        elif line.startswith("Avail Bal"):
            metadata["avail_balance"] = line.split(":")[1].strip()
        elif line.startswith("Ledger Balance"):
            metadata["ledger_balance"] = line.split(":")[1].strip()

    # Find index of where table starts in lines
    start_index = next(i for i, line in enumerate(lines) if line.startswith("Date,Unique Id"))

    # Read table into pandas
    table = pd.read_csv(filename, skiprows=start_index)

    return metadata, table

# Loading CSV files
files = glob.glob("data/*.csv")

# Read csv file
metadata, table = parse_bank_csv("data/Export20250729150608.csv")

# Write to excel file   
table.to_excel("formatted_statement.xlsx", index=False)
print("CSV file successfully written to xl")




