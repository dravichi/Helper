"""
Make sure to follow this step before running the program:
1. Install some libraries that are used in this program
   pip install pdf2image PyPDF2
2. Download and install Poppler since pdf2image requires it, it can be downloaded from
   https://github.com/oschwartz10612/poppler-windows/releases/
"""

import os
from pdf2image import convert_from_path
from PyPDF2 import PdfReader

def pdf_to_images(pdf_path, output_folder, start_index, pages=None):
    try:
        # Convert the PDF to images at 300 DPI
        # Specify the pages to convert if given (pages is a list of page numbers)
        images = convert_from_path(pdf_path, dpi=300, first_page=pages[0] if pages else 1, last_page=pages[-1] if pages else None)
        
        # Save each page as an image with sequential naming
        for i, image in enumerate(images):
            output_image_path = os.path.join(output_folder, f"image_{start_index + i}.png")
            image.save(output_image_path, 'PNG')
            print(f"Saved: {output_image_path}")

        # Return the next start index for naming the next set of images
        return start_index + len(images)

    except Exception as e:
        print(f"Error processing {pdf_path}: {e}")
        return start_index

def convert(pdf_folder, output_folder='temp', pages_per_chunk=25):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Initialize the start index for naming the images
    start_index = 1
    
    # Loop through all PDF files in the specified folder
    for filename in os.listdir(pdf_folder):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(pdf_folder, filename)
            print(f"Converting: {pdf_path}")

            try:
                # Get the total number of pages in the PDF
                with open(pdf_path, 'rb') as f:
                    reader = PdfReader(f)
                    
                    # Check if the PDF is encrypted and try to decrypt it
                    if reader.is_encrypted:
                        print(f"PDF {pdf_path} is encrypted. Attempting to decrypt...")
                        try:
                            reader.decrypt("")  # Try decrypting with an empty password (if no password is set)
                        except Exception as decryption_error:
                            print(f"Failed to decrypt {pdf_path}: {decryption_error}")
                            continue  # Skip this encrypted PDF

                    total_pages = len(reader.pages)  # Get the number of pages in the PDF

                # Process the PDF in chunks of pages (e.g., 25 pages at a time)
                for i in range(0, total_pages, pages_per_chunk):
                    # Specify the pages to convert (ensure to handle last chunk if it's smaller)
                    pages = list(range(i + 1, min(i + pages_per_chunk, total_pages) + 1))
                    start_index = pdf_to_images(pdf_path, output_folder, start_index, pages)
                    
            except Exception as e:
                print(f"Error processing {pdf_path}: {e}")
                continue  # Skip to the next file if there's an error

if __name__ == "__main__":
    # Allow the user to define the input and output folder paths
    pdf_folder = input("Enter the path of the input folder containing PDFs: ")  # User-defined input folder
    output_folder = input("Enter the path of the output folder for images: ")  # User-defined output folder
    
    # Call the conversion function
    convert(pdf_folder, output_folder)
