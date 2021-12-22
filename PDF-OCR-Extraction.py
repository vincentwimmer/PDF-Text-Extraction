import pytesseract
import glob
import fitz

# (Default) Path to Tesseract installation - Download: https://digi.bib.uni-mannheim.de/tesseract/
pytesseract.pytesseract.tesseract_cmd=r'C:/Program Files/Tesseract-OCR/tesseract.exe'

# Open PDF, Zoom in for more detail, Write each page to PNG file.
zoom_x = 2.0
zoom_y = 2.0
mat = fitz.Matrix(zoom_x, zoom_y)

path = 'C:/Path/To/Folder/'
all_files = glob.glob(path + "*.pdf")

for filename in all_files:
	doc = fitz.open(filename)  # open document
	for page in doc:  # iterate through the pages
		pix = page.get_pixmap(matrix=mat)  # render page to an image
		pix.save("C:/Path/To/Folder/page-%i.png" % page.number)  # store image as a PNG


# Use Tesseract OCR and open each PNG file, Scrape text, Dump to text file.
textFilePath = "C:/Path/To/Folder/outPut.txt"

for x in range(177):
	img = str('C:/Path/To/Folder/page-' + str(x) + ".png")
	
	# Adding custom options
	custom_config = r'--oem 3 --psm 6'

	input_file = open(textFilePath, "a")
	input_file.write("\n" + pytesseract.image_to_string(img, config=custom_config))
	input_file.close()

	print(img, "Done.")
