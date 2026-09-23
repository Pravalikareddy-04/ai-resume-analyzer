import os


def extract_resume_text(file_path):

    extension = os.path.splitext(file_path)[1].lower()

    try:

        if extension == ".pdf":

            from pypdf import PdfReader

            reader = PdfReader(file_path)

            text = ""

            for page in reader.pages:

                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

            return text

        elif extension == ".docx":

            from docx import Document

            document = Document(file_path)

            text = ""

            for paragraph in document.paragraphs:

                text += paragraph.text + "\n"

            return text

        elif extension == ".txt":

            with open(
                file_path,
                "r",
                encoding="utf-8",
                errors="ignore"
            ) as file:

                return file.read()

        else:

            return ""

    except Exception as e:

        print("Resume parsing error:", e)

        return ""