import PyPDF2
import os

merger = PyPDF2.PdfMerger()

listArq = os.listdir("files")
listArq.sort() #Ordena os arquivos
print (listArq)

for file in listArq:
    if ".pdf" in file:
        merger.append(f"files/{file}")
        
        
merger.write("PDF Final.pdf")

