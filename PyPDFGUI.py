from pypdf import *
import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox



# 612px x 792px
# TODO: Can i extract out the reader = PDFReader into a class attribute and just use .self
# TODO: Functionality for watermark
# TODO: Functionality to combine two pdfs

class PdfFunctions(object):
        
    #PDF That User Selects
    selectedFilePath = ""
    
    #Function to get information on PDF
    def get_info(pdf_path):
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
    def rotate_right_and_save(pdf_path):
        
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

    def rotate_left_and_save(pdf_path):

        reader = PdfReader(pdf_path)
        writer = PdfWriter()

        for page in range(0,len(reader.pages)):
            writer.add_page(reader.pages[page])
            writer.pages[page].rotate(-90)

        # Assert New File Name Field Is Not Empty
        assert newFileNameField.get()
        with open(f"{newFileNameField.get()}.pdf", 'wb') as fp:
            writer.write(fp)
            messagebox.showinfo(title= "Successful", message="Successfully Rotated File")
    

# Keeping Track of State
clicked = False
clickCounter = 0

def getFile():
    filePath = askopenfilename(title="Select File", filetypes=(("pdf files", "*.pdf"),("all files", ".**")))
    print(PdfFunctions.get_info(filePath))
    PdfFunctions.selectedFilePath = filePath
    global clicked
    clicked = True
    return filePath

# Had to abstract out functions because leaving them in the command makes them automatically run as the 
# program goes through it's main loop
def callRotateLeft():
    return PdfFunctions.rotate_left_and_save(PdfFunctions.selectedFilePath)

def callRotateRight():
    return PdfFunctions.rotate_right_and_save(PdfFunctions.selectedFilePath)

def callAddBlankPage():
    return PdfFunctions.add_blank_page(PdfFunctions.selectedFilePath)
    
def addRotateLeftandRotateRight():
    global clickCounter

    root.after(1000, addRotateLeftandRotateRight)
    if clicked and clickCounter == 0:

        # Tell user which PDF they selected
        filePathNameLabe = tk.Label(root, text=f"Selected: {PdfFunctions.selectedFilePath}", font=('Arial',12))
        filePathNameLabe.pack()

        # #Rotate Left and Save Button
        rotateLeftButton = tk.Button(root, text="Rotate Left and Save", command=callRotateLeft)
        rotateLeftButton.pack()
        clickCounter = 1

        # #Rotate Right and Save Button
        rotateRightButton = tk.Button(root, text="Rotate Right and Save", command=callRotateRight)
        rotateRightButton.pack()

#Creating TKinter Main Window
root = tk.Tk()
root.geometry("500x300")
root.title("Fix GERST PDFs")

# New PDF Name Label and Textfield
newFileNameLabel = tk.Label(root, text="Enter New Name for PDF", font=('Arial',18))
newFileNameLabel.pack(pady=10)
newFileNameField = tk.Entry(root, font=('Arial',16))
newFileNameField.pack()

# Select PDF Label and Button
selectPdfLabel = tk.Label(root, text="Select PDF to Fix", font=('Arial',18))
selectPdfLabel.pack(pady=10)
selectFileButton = tk.Button(root, text="Select PDF", command=getFile)
selectFileButton.pack()

addRotateLeftandRotateRight()
root.mainloop()