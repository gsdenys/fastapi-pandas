import pandas as pd

def run(csv_file):
    """Run csv processing.

    This function read a csv file, Convert the price and Number to 
    number and multipy them to create a new collun 'Total'

    Args:
        csv_file (file): the CSV file
        tab (string): name of tab

    Returns:
        dataframe: Pandas dataframe
        string: error message
    """
    try:
        df = pd.read_csv(csv_file.file, dtype=str)
    except Exception as e:
        msg = str(e)
        return None, msg
    
    # Convert the price and number to number and multipy them to create a new collun 'Total'
    df[['Price', 'Number']] = df[['Price', 'Number']].apply(pd.to_numeric, errors='coerce')
    df['Total'] = df['Number'] * df['Price']

    return df, None
