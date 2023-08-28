import tabula
import os
from tabula.io import read_pdf
import pandas as pd

file_path = input('Enter a file path: ')

if os.path.exists(file_path):
    pages = input("Enter page numbers or enter all for all pages (Eg.: 1, '1-2,3', 'all' or [1,2]. Default is 1): ")
    dfs = tabula.read_pdf(file_path, stream=True,pages=pages,encoding='cp1252')
    df_csv_append = pd.DataFrame()
    for df in dfs:
        df_csv_append = pd.concat([df_csv_append, df], ignore_index=False)
    df_csv_append.to_csv(os.getcwd() + "\\file.csv")
else:
    print('The specified file does NOT exist')