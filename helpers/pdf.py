from pypdf import PdfReader
import os
from helpers.exceptions import PdfError


class PdfExtractor:
    """
    A class to extract images and text from a PDF file

    Args:
        file_path (str): The path to the PDF file

    Raises:
        PdfError: If the file does not exist

    Attributes:
        file_path (str): The path to the PDF file
        pdf (PdfReader): The PDF file

    Methods:
        parse: Extracts images and text from the PDF file
    """

    def __init__(self, file_path: str):
        self.file_path = file_path

        if not os.path.exists(file_path):
            raise PdfError(file_path, "File does not exist")

        self.pdf = PdfReader(file_path)

    def extract(self):
        """
        Extracts images and text from the PDF file

        Returns:
            dict: A dictionary containing the following:

                - "imgs": A list of image names
                - "metadata": A dictionary containing the metadata of the PDF file
                - "pages": A list of strings, each containing the text of a page
                - "text": A string containing all the text of all the pages
        """
        imgs = []
        res = []
        for page in self.pdf.pages:
            imgs.extend(page.images.keys())
            res.append(page.extract_text())

        return {
            "imgs": imgs,
            "pages": res,
            "metadata": self.pdf.metadata,
            "text": "\n\n".join(res),
        }
