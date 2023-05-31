import pandas as pd
def merge_files(prodcuts, transactions):
    products = pd.read_csv('Product_range.csv')
    transactions = pd.read_csv('Transactions.csv')

    df_final = pd.merge(transactions, products, 
                        left_on='Product_code', 
                        right_on='Product_code', 
                        how='left')

    return df_final



