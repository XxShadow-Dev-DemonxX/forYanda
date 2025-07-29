import pandas as pd

def format(metadata, table):
    # Format the date
    table['Date'] = pd.to_datetime(table['Date']).dt.strftime('%d %b %Y')

    # Combine Payee name and Memo, to form transaction description as formatted in bank statement
    table['Transaction Description'] = table['Payee'] + "\n" + table['Memo']

    # Differentiate between debit vs credit
    table['Debit/Cheque'] = table['Amount'].apply(lambda x: f"${abs(x):.2f}" if x < 0 else "")
    table['Credit/Deposit'] = table['Amount'].apply(lambda x: f"${x:.2f}" if x > 0 else "")

    # Get ledger balance
    ledger_balance = float(metadata["ledger_balance"].split()[0])

    # Convert Amount to float
    table['Amount'] = pd.to_numeric(table['Amount'], errors='coerce')

    # Drop any rows where Amount is NaN (if there were weird values)
    table = table.dropna(subset=['Amount'])

    # Calculate opening balance as ledger - all transactions = opening balance
    opening_balance = ledger_balance - table['Amount'].sum()

    # Running balance - this is the balance that is changing throughout transactions
    balance = opening_balance
    balances = []
    for amount in table['Amount']:
        balance += amount
        balances.append(f"${balance:.2f}")
    table['Balance'] = balances

    # Insert row for the opening balance
    opening_row = pd.DataFrame([{
        "Date": table['Date'][0],   # First transaction date
        "Transaction Description": "Opening Balance",
        "Debit/Cheque": "",
        "Credit/Deposit": "",
        "Balance": f"${opening_balance:.2f}"
    }])

    # Finalised formatted dataframe
    final_table = pd.concat([opening_row, table[['Date', 'Transaction Description', 'Debit/Cheque', 'Credit/Deposit', 'Balance']]], ignore_index=False)

    return final_table
