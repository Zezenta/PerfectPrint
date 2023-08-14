from PyPDF2 import PdfReader, PdfWriter #the library that supports PDF manipulation
import re #imports the regex that we are going to use
from docx import Document #the library that supports docx manipulation

file_raw_name = input("Please enter the name of the file that you want to alter. EXAMPLE: document.pdf ")
pattern = r'([\w\_\-]+)\.(\w+)' #This regex indicates any kind of alphanumerical number, and "-" or "_" characters, one time or more. Then, a single period. And finally, captures any alphanumerical text (hence, the extension)

file_groups = re.match(pattern, file_raw_name) #Apply the regex pattern to the file_raw_name
file_name = file_groups.group(1) #We extract the name of the file
file_type = file_groups.group(2) #We extract its type
current_file_pages = [] #The array that will contain the file's pages
output_file_name = file_name + "_REVERSED" + "." + file_type #The output file name is the file name with "_REVERSED" at the end

def create_pdf(output_filename, pages): #We declare a function called create_pdf
    writer = PdfWriter() #We declare a writer
    for x in pages: #For every page
        writer.add_page(x) #We add said page to the writer
    writer.write(output_filename) #We write a new file with the output_filename
    writer.close() #We close the writer

if file_type == "pdf": #If the filetype is pdf
    readed_pdf = PdfReader(file_raw_name) #We create a new pdfreader object that is the file itself
    for curr_page in range(len(readed_pdf.pages)): #For every page in the readed_pdf pages
        page = readed_pdf.pages[curr_page] #We get said page
        current_file_pages.append(page) #And we add it to the current_file_pages array
    reversed_pages = current_file_pages[::-1]
    create_pdf(output_file_name, reversed_pages) #Finally, we call the create_pdf function

print(output_file_name) #We just print the output filename