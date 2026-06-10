import os
from pypdf import PdfMerger, PdfReader, PdfWriter

def merge_pdfs(pdf_list, output_filename):
    """Combines multiple PDFs into a single file."""
    merger = PdfMerger()
    
    for pdf in pdf_list:
        if os.path.exists(pdf):
            print(f"Adding: {pdf}")
            merger.append(pdf)
            
    merger.write(output_filename)
    merger.close()
    print(f"Congragulations Successfully created: {output_filename}\n")


def extract_pages(input_pdf, output_pdf, start_page, end_page):
    """Extracts a specific range of pages (0-indexed) into a new PDF."""
    reader = PdfReader(input_pdf)
    writer = PdfWriter()
    
    # Loop through the desired page range
    for page_num in range(start_page, end_page + 1):
        writer.add_page(reader.pages[page_num])
        
    with open(output_pdf, "wb") as f:
        writer.write(f)
    print(f"Extracted pages {start_page} to {end_page} into {output_pdf}")
