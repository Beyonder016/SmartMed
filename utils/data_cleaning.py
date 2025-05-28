# utils/data_cleaning.py

import pandas as pd

def clean_sales_data(df):
    """Cleans and formats the sales data for dashboard usage."""

    # Drop fully empty rows
    df.dropna(how='all', inplace=True)

    # Strip and sanitize column names
    df.columns = [str(col).strip().replace(" ", "_").replace(":", "") for col in df.columns]

    # 🔍 Debug log
    print("🧠 Cleaned Columns:", df.columns.tolist())

    # Check for key column existence with fallback options
    alt_names = ['Vch_date', 'Vchdate', 'Voucher_Date']
    found_date_col = next((col for col in df.columns if col in alt_names), None)
    if not found_date_col:
        raise ValueError("Missing expected column: 'Vch_date'")

    df.rename(columns={found_date_col: 'Vch_date'}, inplace=True)

    # Do same for Amount just in case
    if 'Amount' not in df.columns:
        raise ValueError("Missing expected column: 'Amount'")

    # Convert date columns
    df['Vch_date'] = pd.to_datetime(df['Vch_date'], errors='coerce')
    if 'Exp_date' in df.columns:
        df['Exp_date'] = pd.to_datetime(df['Exp_date'], errors='coerce')

    # Convert numerics
    for col in ['Qty', 'Scm_qty', 'Scm_disc', 'MRP', 'Amount']:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')

    # Fill scheme info
    df['Scm_qty'] = df.get('Scm_qty', 0).fillna(0)
    df['Scm_disc'] = df.get('Scm_disc', 0).fillna(0)

    return df
