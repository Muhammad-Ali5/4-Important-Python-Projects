from PyPDF2 import PdfReader, PdfWriter, PdfMerger  # Import the necessary classes from the PyPDF2 library

pdfs = ["pdf1.pdf", "pdf2.pdf"]  # Create a list of PDF filenames to merge

with PdfMerger() as merger:      # Open a PdfMerger object using a context manager
    for pdf in pdfs:             # Loop through each PDF in the list
        merger.append(pdf)       # Add the current PDF to the merger
    merger.write("merged-pdf-jani.pdf")  # Write the merged PDF to a new file
    merger.close()       # Close the merger (optional in a context manager but included for clarity)


# merger = PdfWriter()

# for pdf in ["pdf1.pdf", "pdf2.pdf"]:
#     merger.append(pdf)

# merger.write("merged-pdf.pdf")
# merger.close()