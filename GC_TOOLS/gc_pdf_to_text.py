import PyPDF2

def pdf_to_text(pdf_path, text_path):
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        # Estrai il testo da ogni pagina
        text_content = ""
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text_content += page.extract_text()

        # Salva il testo in un file di testo
        with open(text_path, 'w', encoding='utf-8') as text_file:
            text_file.write(text_content)




# Esempio di utilizzo
pdf_to_text('GC_TOOLS/DATA/test.pdf', 'GC_TOOLS/DATA/test.txt')
