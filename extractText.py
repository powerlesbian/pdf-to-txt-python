from pypdf import PdfReader
#import re


fname = input("Enter .pdf file: ")
if '.pdf' not in fname: 
    print('no pdf file provided, using default file')
    fname = 'conference.pdf' 
#fh = open(fname)
reader = PdfReader(fname)

for i in range(len(reader.pages)):
    page = reader.pages[i]
    textWorking = page.extract_text()
    cleanText = ''
    for line in textWorking:
        line=line.rstrip() #removes spaces and line breaks
        cleanText = (cleanText+line)  #creates one huge long spaceless string for each page
    print('Currently on page',i+1,':', cleanText)    



''' figure out how to:

1. clean up extracted text line breaks
2.  save extracted text to a file
Done 3.  add file opener prompt
    '''

# extract only text oriented up
#print(page.extract_text(0))

# extract text oriented up and turned left
#print(page.extract_text((0, 90)))