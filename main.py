import read_file
import format_table
import format_excel
import pandas as pd
import glob
from datetime import datetime

def file_processing(files):
    # Read metadata from the first file to determine filename
    first_metadata, _ = read_file.parse_bank_csv(files[0])
    from_dt = datetime.strptime(first_metadata["from_date"], "%Y%m%d")
    to_dt = datetime.strptime(first_metadata["to_date"], "%Y%m%d")
    from_date = from_dt.strftime('%d %b %Y')
    to_date = to_dt.strftime('%d %b %Y')

    excel_filename = f"{from_date} to {to_date} Financial Statement.xlsx"

    # Create Excel file with multiple sheets
    with pd.ExcelWriter(excel_filename, engine="openpyxl") as writer:
        for file in files:
            metadata, table = read_file.parse_bank_csv(file)
            temp = metadata["bank_info"].split(';')[2]              
            temp = temp.split()
            sheet = ' '.join(temp[1:])
            final_table = format_table.format(metadata, table)
            final_table.to_excel(writer, sheet_name=sheet, index=False)

    # Apply formatting to all sheets in the Excel file
    format_excel.format(excel_filename)
