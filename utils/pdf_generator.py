from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

def generate_invoice_pdf(customer, address, items, filename):
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4

    c.setFont("Helvetica-Bold", 20)
    c.drawString(50, 800, "INVOICE")

    c.setFont("Helvetica", 12)
    c.drawString(50, 770, f"Customer: {customer}")
    c.drawString(50, 750, f"Address: {address}")

    y = 710
    total = 0

    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Item")
    c.drawString(300, y, "Price")
    c.line(50, y-5, 500, y-5)
    y -= 30

    c.setFont("Helvetica", 12)
    for item in items:
        c.drawString(50, y, item["item"])
        c.drawString(300, y, f"₹{item['price']}")
        total += item["price"]
        y -= 20

    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y-20, f"Total Amount: ₹{total}")

    c.save()
