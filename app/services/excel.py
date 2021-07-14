import pandas as pd

def run(excel_file, tab):
    """Run excel processing.

    This function read a Excel (xls) file, Convert the price and Number to 
    number and multipy them to create a new collun 'Total'

    Args:
        csv_file (file): the Excel file
        tab (string): name of tab

    Returns:
        dataframe: Pandas dataframe
        string: error message
    """
    try:
        df = pd.read_excel(excel_file.file, tab, dtype=str)
    except Exception as e:
        msg = str(e)
        return None, msg
    
    # Convert the price and number to number and multipy them to create a new collun 'Total'
    df[['Price', 'Number']] = df[['Price', 'Number']].apply(pd.to_numeric, errors='coerce')
    df['Total'] = df['Number'] * df['Price']

    return df, None
