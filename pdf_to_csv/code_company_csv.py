import fitz
import pandas as pd
doc = fitz.open("company_data.pdf")

csv_file = "output_company.csv"

for a in range(len(doc)):
    page1=doc[a]
    table1 = page1.find_tables()
    tab = table1[0]
    df = tab.to_pandas()

    df.to_csv(csv_file, mode='a', header=False, index=False)

