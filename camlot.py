import camelot  # Import the camelot library for PDF table extraction

# Extract tables from the PDF using the 'stream' flavor
tables = camelot.read_pdf("abc.pdf", pages="all", flavor="stream", strip_text='\n')

# Print the total number of tables extracted
print(f"Total tables extracted: {tables._tables}")
for i, table in enumerate(tables):  # Loop through each extracted table
    print(f"\n=== Table {i} ===")  # Print table index
    print(table.df.to_string(index=False, header=False))  # Print table data without index or header
