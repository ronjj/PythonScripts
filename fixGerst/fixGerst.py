from pypdf import *
import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox

#Function to get pdf user wants to rotate
def files():
    filePath = askopenfilename(title="Select File", filetypes=(("pdf files", "*.pdf"),("all files", ".**")))
    print(__get_info(filePath))
    __rotate_pages(filePath)
    return filePath

#Function to get information on PDF
def __get_info(pdf_path):
    with open (pdf_path, 'rb') as f:
        pdf = PdfReader(f)
        title = pdf.metadata.title
        author = pdf.metadata.author
        number_of_pages = len(pdf.pages)
    
    text = f"""
    
    Selected: {pdf_path}
    
    Number of Pages: {number_of_pages}
    Title: {title}
    Author: {author}
    """
    
    return text

#Function to rotate the pages of the selected PDF
def __rotate_pages(pdf_path):
    reader = PdfReader(pdf_path)
    writer = PdfWriter()

    for page in range(0,len(reader.pages)):
        writer.add_page(reader.pages[page])
        writer.pages[page].rotate(90)

    # Assert New File Name Field Is Not Empty
    assert newFileNameField.get()
    with open(f"{newFileNameField.get()}.pdf", 'wb') as fp:
        writer.write(fp)
        messagebox.showinfo(title= "Successful", message="Successfully Rotated File")

#Creating TKinter Main Window
root = tk.Tk()
root.geometry("500x200")
root.title("Fix GERST PDFs")

# New PDF Name Label and Textfield
newFileNameLabel = tk.Label(root, text="Enter New Name for PDF", font=('Arial',18))
newFileNameLabel.pack(pady=10)
newFileNameField = tk.Entry(root, font=('Arial',16))
newFileNameField.pack()

# Select PDF Label and Button
selectPdfLabel = tk.Label(root, text="Select PDF to Fix", font=('Arial',18))
selectPdfLabel.pack(pady=10)
selectFileButton = tk.Button(root, text="Select and Fix PDF", command=files)
selectFileButton.pack()


root.mainloop()