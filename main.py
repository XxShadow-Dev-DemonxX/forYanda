import read_file
import format_table
import format_excel
import pandas as pd
import matplotlib.pyplot as plt
from openpyxl import load_workbook
from openpyxl.drawing.image import Image
import glob

# Loading CSV files
files = glob.glob("data/*.csv")

# Read csv file
metadata, table = read_file.parse_bank_csv("data/Export20250729150608.csv")
  
sheet = metadata["bank_info"].split(';')[2]

# Format
final_table = format_table.format(metadata, table)

# Output to excel
final_table.to_excel("formatted_statement.xlsx", index=False)
format_excel.format("formatted_statement.xlsx")
print("CSV file successfully written to xl")




