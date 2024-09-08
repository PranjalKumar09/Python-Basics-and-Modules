import pikepdf
from tkinter.filedialog  import *
"""
PyPDF is pure python package package that can be used to perform varous operation on PDF files like exxtracting docmuent information, rotating pages, merge pdf, split pdf

For text extractor do from pyPDF

"""
 
 
file= askopenfilename()

old_pdf = pikepdf.Pdf.open(file)


metadata = old_pdf.docinfo
print(metadata)

def rotate_pdf(pdf_path, output_path, rotation_angle):
    pdf = pikepdf.open(pdf_path)
    for page in pdf.pages:
        page.Rotate = rotation_angle
    pdf.save(output_path)

# Example usage
# rotate_pdf("input.pdf", "output.pdf", 90)  # Rotate by 90 degrees clockwise

def merge_pdfs(pdf_paths, output_path):
    pdf = pikepdf.new()
    for path in pdf_paths:
        pdf.pages.extend(pikepdf.Pdf.open(path).pages)
    pdf.save(output_path)

# Example usage
# merge_pdfs(["input1.pdf", "input2.pdf"], "output.pdf")

def extract_pages(pdf_path, output_path, page_numbers):
    pdf = pikepdf.open(pdf_path)
    new_pdf = pikepdf.new()
    for page_num in page_numbers:
        new_pdf.pages.append(pdf.pages[page_num])
    new_pdf.save(output_path)

# Example usage
# extract_pages("input.pdf", "output.pdf", [0, 2, 3])  # Extract pages 1, 3, and 4
def split_pdf(pdf_path, output_folder):
    # split means doing every pages to new pdf 
    pdf = pikepdf.open(pdf_path)
    for i, page in enumerate(pdf.pages):
        page_pdf = pikepdf.new()
        page_pdf.pages.append(page)
        page_pdf.save(f"{output_folder}/page_{i+1}.pdf")

# Example usage
# split_pdf("input.pdf", "output_folder")


def watermark_pdf(input_pdf_path, watermark_pdf_path, output_pdf_path):
    input_pdf = pikepdf.open(input_pdf_path)
    watermark_pdf = pikepdf.open(watermark_pdf_path)

    watermark_page = watermark_pdf.pages[0]  # Assuming the watermark PDF has only one page

    for page in input_pdf.pages:
        page.overlay(watermark_page)

    input_pdf.save(output_pdf_path)
    
# watermark_pdf("input.pdf", "watermark.pdf", "output.pdf")

def encrypt_pdf(pdf_path, output_path, user_password=None, owner_password=None):
    pdf = pikepdf.open(pdf_path)
    pdf.save(output_path, encryption=pikepdf.Encryption(user=user_password, owner=owner_password))

# Example usage
# encrypt_pdf("input.pdf", "output.pdf", "user_password", "owner_password")

from PIL import Image

def pdf_to_images(pdf_path, output_folder):
    pdf = pikepdf.open(pdf_path)
    for i, page in enumerate(pdf.pages):
        image = page.render()
        image.save(f"{output_folder}/page_{i+1}.png")

# Example usage
# pdf_to_images("input.pdf", "output_folder")

import img2pdf

def images_to_pdf(image_paths, output_pdf_path):
    with open(output_pdf_path, "wb") as f:
        f.write(img2pdf.convert(image_paths))

# Example usage
# image_paths = ["image1.png", "image2.jpg", "image3.jpeg"]
# output_pdf_path = "output.pdf"
# images_to_pdf(image_paths, output_pdf_path)