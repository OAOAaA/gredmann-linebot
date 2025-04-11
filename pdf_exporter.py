from fpdf import FPDF

def export_pdf(filename: str, content: str):
    pdf = FPDF()
    pdf.add_page()
    pdf.add_font("ArialUnicode", "", "./fonts/NotoSansTC-Regular.ttf", uni=True)
    pdf.set_font("ArialUnicode", size=12)
    lines = content.split("\n")
    for line in lines:
        pdf.multi_cell(0, 10, txt=line)
    output_path = f"./outputs/{filename}.pdf"
    pdf.output(output_path)
    return output_path
