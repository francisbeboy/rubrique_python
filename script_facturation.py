```python
from fpdf import fpdf, FPDF
from datetime import datetime





class InvoiceGenerator:
    def __init__(self, customer_name,customer_address, items,tax_rate=0.0 ):
        self.customer_name = customer_name
        self.customer_address = customer_address
        self.items = items #list of items [{}]
        self.tax_rate = tax_rate
        self.invoice_number = datetime.now().strftime("%Y%m%d%H%M%S")
        self.date = datetime.now().strftime("%Y-%m-%d")
        self.filename = self.get_file_name()
    def get_file_name(self):
        """Génère un nom de fichier unique pour la facture"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        return f"facture_{timestamp}.pdf"  # Format: facture_YYYYMMDD_HHMMSS.pdf


    def  calculate_total(self):

        """Calcule le total de la facture, la taxe, et la somme totale"""
        subtotal = sum(item["price"]* item["quantity"] for item in self.items)
        tax = subtotal * self.tax_rate
        total = subtotal + tax
        return subtotal, tax, total

    def generate_invoice(self,filename=None):
        if filename is None:
            filename = self.filename
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        # Header
        pdf.cell(200, 10, txt="DevGroupe Invoice System", ln=1, align='C')
        pdf.ln(10)

        # Invoice info
        pdf.cell(200, 10, txt=f"Facture #Numero: {self.invoice_number}", ln=1)
        pdf.cell(200, 10, txt=f"Date: {self.date}", ln=1)
        pdf.ln(5)

        # Customer info
        pdf.cell(200, 10, txt=f"Nom du client: {self.customer_name}", ln=1)
        pdf.cell(200, 10, txt=f"Address du client: {self.customer_address}", ln=1)
        pdf.ln(10)

        # Items table header
        pdf.cell(100, 10, txt="Description", border=1)
        pdf.cell(30, 10, txt="Price", border=1)
        pdf.cell(30, 10, txt="Quantity", border=1)
        pdf.cell(30, 10, txt="Amount", border=1, ln=1)

        #items
        for item in self.items:
            amount= item['price'] * item['quantity']
            pdf.cell(100,10,txt= item['name'],border=1)
            pdf.cell(30, 10, f"${item['price']:.2f}", border=1)
            pdf.cell(30,10,txt= str(item['quantity']),border=1)
            pdf.cell(30, 10, f"${amount:.2f}", border=1,ln=1)

        #total
        subtotal, tax, total = self.calculate_total()
        pdf.ln(10)
        pdf.cell(160, 10, "Subtotal",align="R")
        pdf.cell(30,10,txt=f"${subtotal:.2f}", ln=1)
        pdf.cell(160, 10, txt=f"Tax ({self.tax_rate*100}%):",align="R")
        pdf.cell(30,10,txt=f"${tax:.2f}", ln=1)
        pdf.cell(160,10,txt = "Total:",align="R")
        pdf.cell(30,10,txt=f"${total:.2f}", ln=1)

        pdf.output(filename)
        print(f"Invoice saved as {filename}")
if __name__ == "__main__":
    items = [
        {"name": "Formation Cyber-Sécurité", "price": 150.99, "quantity": 2},
        {"name": "formation de la Cyber-Attack", "price": 153.75, "quantity": 7},
        {"name": "Certification AWS ", "price": 50.3, "quantity": 3},
        {"name": "Certification Pirate éthique", "price": 50.3, "quantity": 1},
        {"name": "Certification Python ", "price": 15.99, "quantity": 2},
        {"name": "Certification  développeur java ", "price": 38.3, "quantity": 1},
        {"name": "Certification Oracle", "price": 1500.93, "quantity": 1}
    ]
    invoice_generator = InvoiceGenerator("Diomande Francis", "Cocody Abidjan", items=items, tax_rate=5.08)
    invoice_generator.generate_invoice()
```
