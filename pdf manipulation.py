# merger code :

  from PyPDF2 import PdfMerger

def merge_pdfs(pdf_files, output_file):
pdf_merger = PdfMerger()


    for pdf_file in pdf_files:
pdf_merger.append(pdf_file)


    with open(output_file, 'wb') as output:
pdf_merger.write(output)

print(f'Merged PDFs into {output_file}')

num_pdfs = int(input("Enter the number of PDFs to merge: "))
pdf_files = [input(f"Enter the path of PDF {i + 1}: ") for i in range(num_pdfs)]
output_file = input("Enter the name of the output merged PDF file: ")
merge_pdfs(pdf_files, output_file)



# encryption code :

from PyPDF2 import PdfWriter, PdfReader

def encrypt_pdf(input_file, password):

    out = PdfWriter()

    try:

        file = PdfReader(input_file)
        num = len(file.pages)
        for idx in range(num):
            page = file.pages[idx]
out.add_page(page)    
out.encrypt(password)

output_file = input_file.replace('.pdf', '_encrypted.pdf')


        with open(output_file, "wb") as f:

out.write(f)

print(f"Success: PDF file encrypted and saved as {output_file}")

    except Exception as e:
print(f"Error: {e}")


file_path = input("Enter the path of the PDF file: ")
password = input("Enter the password for encryption: ")

encrypt_pdf(file_path, password)




# decryption code :

from PyPDF2 import PdfWriter, PdfReader

def decrypt_pdf(input_file, password):
pdf_reader = PdfReader(input_file)

    try:
        if pdf_reader.is_encrypted:
            if pdf_reader.decrypt(password):

pdf_writer = PdfWriter() 
                num = len(pdf_reader.pages) 

                for idx in range(num):
                    page = pdf_reader.pages[idx]
pdf_writer.add_page(page)

output_file = input_file.replace('_encrypted.pdf', '_decrypted.pdf')

                with open(output_file, "wb") as f:
pdf_writer.write(f)

print(f"Success: PDF file decrypted and saved as {output_file}")
            else:
print("Error: Incorrect password. Decryption failed.")
        else:
print("Error: The provided PDF file is not encrypted.")

    except Exception as e:
print(f"Error: {e}")


file_path = input("Enter the path of the PDF file: ")
password = input("Enter the password for decryption: ")

decrypt_pdf(file_path, password)
