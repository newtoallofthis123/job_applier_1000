import spacy
from helpers.file import setup_file_handlers
from helpers.pdf import PdfExtractor
from helpers.parsers.resume import ResumeParser

setup_file_handlers()

print("Hello World")

p = PdfExtractor("./IshanJoshi.resume.pdf")
extracted = p.extract()

r = ResumeParser(extracted["text"])
print(r.parse())
