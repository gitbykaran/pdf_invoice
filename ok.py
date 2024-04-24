from fpdf import FPDF
import streamlit as st
from datetime import date

c = date.today()
d = c.strftime('%d/%m/%Y')

img = 'export (1).png'

st.title('Invoice Genrerator ⚙️')

name = st.text_input('Enter the Invoice Receiver').upper()
address = st.text_input('Enter the Invoice Receivers Address').upper()
site = st.text_input('Enter the site name').upper()


# Instantiate PDF class
pdf = FPDF()
pdf.add_page()

# Set font for title
pdf.set_font('Arial', 'B', 26)
pdf.cell(0, 15, 'INVOICE', 0, 1, 'L')


# Set font for content
pdf.set_font('Arial', 'B', 11)
pdf.cell(0, 5, 'Karnail Singh Constructions', 0, 1, 'L')
pdf.set_font('Arial', '', 11)
pdf.cell(0, 5, 'Village Balongi, Mohali', 0, 1, 'L')
pdf.cell(0, 5, '9878010151', 0, 2, 'L')


pdf.ln(h='')

pdf.set_font('Arial', 'B', 11)
pdf.cell(0, 10, 'BILL TO:', 0, 0, 'L')

pdf.set_font('Arial', 'B', 11)
pdf.cell(0, 10, 'INVOICE DETAILS:', 0, 1, 'R')


# Set font for content
pdf.set_font('Arial', '', 11)
pdf.cell(0, 5, f"{name}", 0, 0, 'L')
pdf.cell(0, 5, f"Date: {d}", 0, 1, 'R')
pdf.cell(0, 5, f"{address}", 0, 0, 'L')
pdf.cell(0, 5, f"Site:{site}", 0, 1, 'R')

pdf.ln(h='')

pdf.image(img, w=190, h=110, type='png')
pdf.ln(h='')

pdf.set_font('Arial', 'B', 11)
pdf.cell(0, 10, 'SUB TOTAL:                       ', 0, 1, 'R')
pdf.ln(h='')

pdf.set_font('Arial', 'B', 11)
pdf.cell(0, 5, 'ADDITIONAL NOTES:', 0, 1, 'L')


# Save the PDF
pdf_file = "invoice.pdf"
pdf.output(pdf_file)

with open('invoice.pdf', 'rb') as p:
    st.download_button("Download Invoice", p, file_name='invoice.pdf')
