
import tabula  # Import tabula for PDF table extraction
import pandas as pd  # Import pandas for data handling

# Read tables from PDF
df_list = tabula.read_pdf("abc.pdf", pages='all', multiple_tables=True)

# Loop through each DataFrame (table)
for df in df_list:
    table = df.dropna(how='all').values.tolist()  # Remove empty rows and convert to list
    print("[")  # Start of table
    for row in table:
        clean_row = [str(cell).strip() for cell in row if str(cell).strip() != 'nan']  # Clean each cell
        print(f"  {clean_row},")  # Print cleaned row
    print("]")  # End of table
