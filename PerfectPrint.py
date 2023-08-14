import PyPDF2 #the library that supports PDF manipulation
import re #imports the regex that we are going to use
from docx import Document #the library that supports docx manipulation

file_raw_name = input("Please enter the name of the file that you want to alter. EXAMPLE: document.pdf ")
pattern = r'([\w\_\-]+)\.(\w+)' #This regex indicates any kind of alphanumerical number, and "-" or "_" characters, one time or more. Then, a single period. And finally, captures any alphanumerical text (hence, the extension)

file_groups = re.match(pattern, file_raw_name)
file_name = file_groups.group(1)
file_type = file_groups.group(2)


current_file_pages = []

if file_type == "pdf":
    with open(file_raw_name, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            current_file_pages.append(page.extract_text())

reversed_pages = current_file_pages[::-1]

output_file_name = file_name + "_REVERSED" + "." + file_type

print(output_file_name)
print(current_file_pages)