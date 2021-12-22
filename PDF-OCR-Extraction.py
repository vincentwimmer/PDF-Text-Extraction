import pytesseract
import glob
import fitz

# (Default) Path to Tesseract installation - Download: https://digi.bib.uni-mannheim.de/tesseract/
pytesseract.pytesseract.tesseract_cmd=r'C:/Program Files/Tesseract-OCR/tesseract.exe'

# File Paths
path = 'C:/Path/To/Work/Folder/'
allPDFFiles = glob.glob(path + "*.pdf")
textFilePath = (path + "outPut.txt")

# Open PDF, Zoom in for more detail, Write each page to PNG file.
zoom_x = 2.0
zoom_y = 2.0
mat = fitz.Matrix(zoom_x, zoom_y)

for filename in allPDFFiles:
	doc = fitz.open(filename)
	for page in doc:
		pix = page.get_pixmap(matrix=mat)
		pix.save(filename[:-4] + "-page-%i.png" % page.number)


# Use Tesseract OCR and open each PNG file, Scrape text, Dump to text file.
allPNGFiles = glob.glob(path + "*.png")

for x in range(len(allPNGFiles)):
	img = allPNGFiles[x]

	print(img)
	
	# Adding custom options
	custom_config = r'--oem 3 --psm 6'

	input_file = open(textFilePath, "a")
	input_file.write("\n" + pytesseract.image_to_string(img, config=custom_config))
	input_file.close()

	print(img, "Done.")
