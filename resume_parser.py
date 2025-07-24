import fitz  

def parse_resume(file_path):
    try:
        doc = fitz.open(file_path)
        text = ""
        for page in doc:
            text += page.get_text()

        return {"text": text.strip()}
    except Exception as e:
        return {"error": str(e)}
