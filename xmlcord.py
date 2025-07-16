import os
from bs4 import BeautifulSoup
from collections import defaultdict

def print_xml_coordinates_to_terminal(xml_path):
    try:
        with open(xml_path, "r", encoding="utf-8") as file:
            soup = BeautifulSoup(file, "xml")

        text_elements = soup.find_all("text")

        rows = defaultdict(list)
        if text_elements:
            for text_tag in text_elements:
                left = float(text_tag.get("left"))
                top = float(text_tag.get("top"))
                width = float(text_tag.get("width"))
                height = float(text_tag.get("height"))

                x0 = left
                y0 = top
                x1 = left + width
                y1 = top + height

                rows[int(top)].append((left, x0, y0, x1, y1))
        
        output_lines = []
        if rows:
            for top_val in sorted(rows.keys()):
                sorted_row = sorted(rows[top_val], key=lambda x: x[0])
                row_coordinates = []
                for left, x0, y0, x1, y1 in sorted_row:
                    row_coordinates.append(f"({x0:.2f}, {y0:.2f}, {x1:.2f}, {y1:.2f})")
                output_lines.append(f"[{', '.join(row_coordinates)}]")
        else:
            output_lines.append("No <text> elements found in the XML file.")

        output_file = "coordinates_output.txt"
        with open(output_file, "w", encoding="utf-8") as f:
            for line in output_lines:
                f.write(line + '\n')
        print(f"Output written to {output_file}")

    except FileNotFoundError:
        print(f"Error: The file {xml_path} was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    xml_file = "abc.xml"
    print_xml_coordinates_to_terminal(xml_file) 