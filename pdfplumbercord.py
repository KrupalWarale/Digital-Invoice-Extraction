
import pdfplumber

def extract_coordinates(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        for page_num, page in enumerate(pdf.pages):
            print(f"--- Page {page_num + 1} ---")

            tables = page.find_tables()
            if tables:
                print(f"Number of tables found: {len(tables)}")
                for i, table in enumerate(tables):
                    print(f"Table {i + 1}:")
                    if table.rows:
                        for row_num, row in enumerate(table.rows):
                            row_coordinates = []
                            for cell_bbox in row.cells:
                                if cell_bbox is not None:
                                    x0, top, x1, bottom = cell_bbox
                                    row_coordinates.append(f"('{x0:.2f}, {top:.2f}'), ('{x1:.2f}, {bottom:.2f}')")
                                else:
                                    row_coordinates.append(None)
                            print(f"    Row {row_num}: {row_coordinates}")
                    else:
                        print(f"  No rows found for Table {i + 1}.")
            else:
                print("No tables found on this page.")

if __name__ == "__main__":
    pdf_file = "abc.pdf"
    extract_coordinates(pdf_file)

