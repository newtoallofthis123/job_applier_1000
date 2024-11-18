class PdfError(Exception):
    def __init__(self, filename: str, message: str):
        super().__init__(f"Error processing {filename}: {message}")

    def __str__(self):
        return self.args[0]