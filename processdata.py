import pandas as pd

xl = pd.ExcelFile('Murders.xlsx');
print(xl.sheet_names)