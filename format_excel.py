from openpyxl import load_workbook
from openpyxl.styles import Font, PatternFill, Border, Side

def format(file_name):    
    # Load the existing excel worksheet
    wb = load_workbook(file_name)
    ws = wb.active

    # Make headers (first row) bold
    for cell in ws[1]:  # First row
        cell.font = Font(bold=True)

    # Increase width for columns, such that it accounts for text
    for col in ws.iter_cols(1, ws.max_column):
        if col[0].value == "Date":
            col_letter = col[0].column_letter
            ws.column_dimensions[col_letter].width = 15
        
        elif col[0].value == "Transaction Description":
            col_letter = col[0].column_letter
            ws.column_dimensions[col_letter].width = 60
        
        elif col[0].value == "Debit/Cheque":
            col_letter = col[0].column_letter
            ws.column_dimensions[col_letter].width = 15
        
        elif col[0].value == "Credit/Deposit":
            col_letter = col[0].column_letter
            ws.column_dimensions[col_letter].width = 15
        
        elif col[0].value == "Balance":
            col_letter = col[0].column_letter
            ws.column_dimensions[col_letter].width = 8

    # Currency formatting for debit, credit, and balance columns
    currency_fmt = "$#,##0.00"
    for row in ws.iter_rows(min_row=2, max_row=ws.max_row):
        for col_idx, cell in enumerate(row, start=1):
            header = ws.cell(1, col_idx).value
            if header in ["Debit/Cheque", "Credit/Deposit", "Balance"] and cell.value not in ("", None):
                cell.number_format = currency_fmt
    
    # Define gray fill & black border
    fill_gray = PatternFill(start_color="DDDDDD", end_color="DDDDDD", fill_type="solid")
    thin_border = Border(
        left=Side(style="thin", color="000000"),
        right=Side(style="thin", color="000000"),
        top=Side(style="thin", color="000000"),
        bottom=Side(style="thin", color="000000")
    )

    # Apply to every 2nd row
    for row in range(2, ws.max_row + 1):
        if row % 2 == 0:
            for cell in ws[row]:
                cell.fill = fill_gray
        cell.border = thin_border

    # Save changes
    wb.save(file_name)
