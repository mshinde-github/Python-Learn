from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='P', format='A4', unit='mm')
pdf.set_auto_page_break(False, 0)

df = pd.read_csv("topic.csv")
for index, row in df.iterrows():
    pdf.add_page()

    pdf.set_font('Arial', 'B', 24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(0, 12, txt=row["Topic"], align='L',ln=1)
    for y in range(20,298,10):
        pdf.line(10, y, 200, y)
    pdf.line(10,21,200,21)

    pdf.ln(265)
    pdf.set_font('Arial', 'I', 8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(0, 12, txt=row["Topic"]+ "1", align='R', ln=1)

    for i in range(row['Pages']-1):
        pdf.add_page()
        pdf.ln(277)
        pdf.set_font('Arial', 'I', 8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(0, 12, txt=row["Topic"] + str(i+2), align='R', ln=1)
        for y in range(20, 298, 10):
            pdf.line(10, y, 200, y)
pdf.output('output.pdf')
