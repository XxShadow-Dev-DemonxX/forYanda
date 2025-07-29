import read_file
import pandas as pd
import matplotlib.pyplot as plt
from openpyxl import load_workbook
from openpyxl.drawing.image import Image
import glob

# Loading CSV files
files = glob.glob("data/*.csv")

# Read csv file
metadata, table = read_file.parse_bank_csv("data/Export20250729150608.csv")

# Write to excel file   
sheet = metadata["bank_info"].split(';')[2]
print(table)
#table.to_excel("20250729.xlsx", sheet_name=sheet, index=False)
print("CSV file successfully written to xl")




