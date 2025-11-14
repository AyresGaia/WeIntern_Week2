from flask import Flask, render_template, request, send_file
from utils.pdf_generator import generate_invoice_pdf
from utils.db import insert_invoice, get_last_invoice_id
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    customer = request.form["customer"]
    address = request.form["address"]
    items = request.form.getlist("item")
    prices = request.form.getlist("price")

    # Convert to structured list
    invoice_items = [
        {"item": items[i], "price": float(prices[i])}
        for i in range(len(items))
    ]

    invoice_id = get_last_invoice_id() + 1
    filename = f"invoices/invoice_{invoice_id}.pdf"

    # Generate PDF
    generate_invoice_pdf(customer, address, invoice_items, filename)

    # Store in DB
    insert_invoice(invoice_id, customer, filename)

    return send_file(filename, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
