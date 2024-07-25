import xml.etree.ElementTree as ET
from openpyxl import Workbook

# Parses the XML file
def xml_to_excel(xml_file, excel_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    workbook = Workbook()
    sheet = workbook.active
    
    # Go through XML and write to Excel
    header = [elem.tag for elem in root[0]]
    sheet.append(header)
    
    for child in root:
        row = [elem.text for elem in child]
        sheet.append(row)
    
    workbook.save(excel_file)
    print(f"Data successfully written to {excel_file}")

# Example usage
xml_file = 'sample_xml_file'
excel_file = 'sample_data.xlsx'
xml_to_excel(xml_file, excel_file)
