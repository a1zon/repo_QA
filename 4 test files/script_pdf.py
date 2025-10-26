from pypdf import PdfReader

def extract_text_from_first_page(pdf_path):
    with open(pdf_path, "rb") as file:
        reader = PdfReader(file)
        first_page = reader.pages[0]
        return first_page.extract_text()
text = extract_text_from_first_page("__File__/tmp/sample.pdf")
print(text)