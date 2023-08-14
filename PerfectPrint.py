import PyPDF2 #the library that supports PDF manipulation
import re #imports the regex that we are going to use
from docx import Document #the library that supports docx manipulation

file_name = input("Please enter the name of the file that you want to alter. EXAMPLE: document.pdf ")
pattern = r'[\w\_\-]+\.(\w+)' #This regex indicates any kind of alphanumerical number, and "-" or "_" characters, one time or more. Then, a single period. And finally, captures any alphanumerical text (hence, the extension)

file_type = re.match(pattern, file_name)

current_file_pages = []

if file_type.group(1) == "pdf":
    with open(file_name, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            current_file_pages.append(page.extract_text())

reversed_pages = current_file_pages[::-1]

output_file_name = file_name + "reversed"

def create_pdf(output_filename, pages):
    pdf_writer = PyPDF2.PdfWriter()

    for page_content in pages:
        pdf_page = PyPDF2.PageObject.create_text_page(page_content)
        pdf_writer.add_page(pdf_page)

    with open(output_filename, 'wb') as output_file:
        pdf_writer.write(output_file)

create_pdf(output_file_name, reversed_pages)