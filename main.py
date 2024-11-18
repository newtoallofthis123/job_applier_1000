from helpers.pdf import PdfExtractor
from parsers.resume import ResumeParser

print("Hello World")

p = PdfExtractor("./IshanJoshi.pdf")
extracted = p.extract()

r = ResumeParser(extracted["text"])
print(r.parse())
