from pdfrw import PdfReader, PdfWriter
 
pages = PdfReader(r'book_008.pdf', decompress=False).pages
other_pages = PdfReader(r'WebSocket.pdf', decompress=False).pages
print type(pages)
#print pages[0]['/Parent']

writer = PdfWriter()
writer.addpages(pages)
writer.addpages(other_pages)

#print PdfReader('book_008.pdf').values
writer.write(r'out.pdf')
