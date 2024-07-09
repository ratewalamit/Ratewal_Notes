from pdfrw import PdfReader, PdfWriter, PageMerge

# Read the PDF pages
pdf1_pages = PdfReader('Astronomy_Concepts.pdf').pages
pdf2_pages = PdfReader('Weak_gravitational_lensing_IAGRG.pdf').pages
pages = pdf1_pages + pdf2_pages

# Initialize the PdfWriter
output = PdfWriter()

# Calculate the maximum width and height
rects = [[float(num) for num in page.MediaBox] for page in pages] 
height = max(x[3] - x[1] for x in rects)
width = max(x[2] - x[0] for x in rects)

# Define the MediaBox for the new pages
mbox = [0, 0, width, height]

for page in pages:
    newpage = PageMerge()
    newpage.mbox = mbox  # Set boundaries of output page
    
    # Add the old page to the new page
    newpage.add(page)
    image = newpage[0]  # Get image of old page (first item)
    
    # Calculate the scaling factor to stretch the width
    scale_factor = width / image.w
    
    # Scale the page to match the width of the widest page
    image.scale(scale_factor, 1)
    
    # Center the page horizontally and align it at the top vertically
    image.x = (width - image.w) / 2
    image.y = height - image.h
    
    # Add the transformed page to the output PDF
    output.addpage(newpage.render())

# Write the output PDF to a file
output.write('homeworks.pdf')
