from pypdf import PdfReader
from pathlib import Path

#a py script that extracts each page of a PDF into separate txt files named from 1 onwards.


fname = input("Enter .pdf file: ")
if '.pdf' not in fname: 
    print('no pdf file provided, using default file')
    fname = 'conference.pdf' 
#fh = open(fname)
reader = PdfReader(fname)

for i in range(len(reader.pages)):
    page = reader.pages[i]
    textWorking = page.extract_text()
#    cleanText = ''
#    for line in textWorking:  #add below stuff to do or find by looping line by line
#        line=line.rstrip() #removes spaces and line breaks
#        cleanText = (cleanText+line)  #creates one huge long string for each page
    with open(str(i+1)+'pdf.txt', 'w') as currentFile:
        currentFile.write('Currently on page '+(str(i+1))+':  '+textWorking)
        #change new name and to 'a' for appends and delete str(i)+ if prefer single file, suggest to change file name with each use
#    print('Currently on page',i+1,':', cleanText)   
print(Path.cwd(), currentFile)

# extract only text oriented up
#print(page.extract_text(0))

# extract text oriented up and turned left
#print(page.extract_text((0, 90)))