import pdfplumber
import glob

path = 'C:/Users/vwimmer/Documents/Git/Cooper/'
all_files = glob.glob(path + "*.pdf")
textFilePath = (path + "outPut.txt")

# Iterate through all PDFs and dump text to outPut.txt
for pdfFileName in all_files:
	pdfFile = pdfplumber.open(pdfFileName)
	
	for pdfPage in pdfFile.pages:
		pdfText = pdfPage.extract_text()
		input_file = open(textFilePath, "a")
		input_file.write("\n" + pdfText + "\n")
		input_file.close()

	pdfFile.close()
	print(pdfFileName, "Done.")
