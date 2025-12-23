from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Helvetica', 'B', 12)
        self.cell(0, 10, 'SciPhy Audiobook Text', align='C')
        self.ln(20)

    def footer(self):
        self.set_y(-15)
        self.set_font('Helvetica', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', align='C')

def create_pdf(input_file, output_file):
    pdf = PDF()
    pdf.add_page()
    pdf.set_font("Courier", size=10) # Using Courier for better ASCII art representation/alignment if any

    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            # Replace unsupported characters if necessary
            # Latin-1 is default for FPDF, so we might need to handle unicode characters
            # or use a unicode font. For now, let's try to encode/decode to latin-1
            # and replace errors, or use a unicode compatible font if available.
            # However, standard FPDF fonts are not full unicode.
            # Given the text is mostly ASCII/Scientific notation, it might be fine.
            # Let's sanitize just in case.

            # Using encode('latin-1', 'replace') to handle characters that aren't in Latin-1
            sanitized_line = line.encode('latin-1', 'replace').decode('latin-1')
            pdf.multi_cell(0, 5, sanitized_line)

    pdf.output(output_file)
    print(f"PDF generated: {output_file}")

if __name__ == '__main__':
    create_pdf('audiobook.txt', 'audiobook.pdf')
