import PyPDF2
from PyPDF2 import PdfFileReader
import re

# optional get info method
def get_info(path):
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)
        info = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()

    print(info)
    print(pdf.numPages)

    author = info.author
    creator = info.creator
    producer = info.producer
    subject = info.subject
    title = info.title

# text extractor gist from some documentation for reference -- just notes
def text_extractor(path):
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)
        # get the first page
        page = pdf.getPage(1)
        print(page)
        print('Page type: {}'.format(str(type(page))))
        text = page.extractText().encode('utf-8')
        for i in text:
            print(i)


# in this case just run the file and change the two wordlists to your liking. one input txt file and one output
if __name__ == '__main__':
    path = './badmoms_merged_ultimate_find_nonNumerical_nonRomanNumeral_editable_foxitFormat_overwrite.pdf'
    with open(path, 'rb') as f:
        object = PyPDF2.PdfFileReader(f)
        number_of_pages = object.getNumPages()

        # Enter worlist consisting of one word per line -- no spaces for searching within every page of a pdf
        with open('./wordlists/wardrobe.txt', 'r') as wordlist_vehicles:
            wurd = list(wordlist_vehicles)
            for line in wurd:
                line = str(line.split())
                line = line.lstrip("['")
                line = line.rstrip("']")
                print(line)

                # alter range if you wish to specify pages
                for i in range(0, number_of_pages):
                    print(i)
                    page = object.getPage(i)
                    text = page.extractText()
                    search_text = text.lower().split()
                    # search within list of split words
                    for word in search_text:
                        if line in word:
                            print("FOUND---------------------")
                            # specify out file
                            f = open("./outputs/wardrobe.txt", 'a')
                            f.write("Pattern Found on Page: {}, {}\n".format(str(i), str(line)))

                            f.close()


