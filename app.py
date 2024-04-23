import streamlit as st
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.pdfgen import canvas
from datetime import date

today = date.today()

st.title('Generate Invoice')
receiver_name = st.text_input('Enter the Invoice Receiver Name').upper()
if receiver_name:
    receiver_address = st.text_input(
        'Enter the Invoice Receiver Address').upper()
    site = st.text_area('Enter the site name or location').upper()


def generate_pdf(data):
    doc = SimpleDocTemplate("invoice.pdf", pagesize=A4)

    # Define the style of the table
    style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                        ('GRID', (0, 0), (-1, -1), 1, colors.black)])

    # Create a table with the provided data
    table = Table(data)
    table.setStyle(style)

    # Add the table to the PDF document
    doc.build([table])

    # Add heading to the top-left corner
    c = canvas.Canvas("invoice.pdf", pagesize=A4)
    c.setFontSize(26)
    c.setFont("Helvetica-Bold", 26)
    c.drawString(50, 800, "INVOICE")


# Add name, address, and phone number
    c.setFontSize(12)
    c.setFont("Helvetica", 12)
    c.drawString(50, 770, "Karnail Singh")
    c.drawString(50, 750, "Balongi, Mohali")
    c.drawString(50, 730, "9878010151")

    # Add two headings aligned left and right
    heading1 = "INVOICE TO:"
    heading2 = "BILL DETAILS:"
    heading_width1 = c.stringWidth(heading1, "Helvetica-Bold", 12)
    heading_width2 = c.stringWidth(heading2, "Helvetica-Bold", 12)
    page_width = A4[0]

    # Align one heading to the left side
    x1 = 50
    y = 690

    # Align the other heading to the right side
    x2 = page_width - heading_width2 - 50

    # Draw the headings
    c.setFont("Helvetica-Bold", 12)
    c.drawString(x1, y, heading1)
    c.drawString(x2, y, heading2)

    c.setFont("Helvetica", 12)
    c.drawString(50, 670, f"{receiver_name}")
    c.drawString(50, 650, f"{receiver_address}")

    c.setFont("Helvetica", 12)
    c.drawString(x2, 670, f"Date: {today}")
    c.drawString(x2, 650, f"Site: {site}")

    c.save()


def main():
    # Sample data for the table
    data = [
        ["Item", "Description", "Quantity", "Price"],
        ["Item 1", "Description 1", "2", "$10"],
        ["Item 2", "Description 2", "1", "$20"],
        ["Item 3", "Description 3", "3", "$15"]
    ]

    # Generate the PDF
    generate_pdf(data)


if __name__ == "__main__":
    main()
