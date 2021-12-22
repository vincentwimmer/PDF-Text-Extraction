import pdfplumber
import glob

path = 'C:/Path/To/Work/Folder/'
all_files = glob.glob(path + "*.pdf")
textFilePath = (path + "outPut.txt")

# Iterate through all PDFs and dump text to outPut.txt
for pdfFileName in all_files:
	pdfFile = pdfplumber.open(pdfFileName)
	pdfPage = pdfFile.pages[0]
	pdfText = pdfPage.extract_text()

	input_file = open(textFilePath, "a")
	input_file.write("\n" + pdfText + "\n")
	
	input_file.close()
	pdfFile.close()

	print(pdfFileName, "Done.")
