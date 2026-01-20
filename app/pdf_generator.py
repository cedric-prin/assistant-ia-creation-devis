import io
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from reportlab.lib.colors import black, lightgrey

def generer_pdf(numero, date, nom, email, lignes, prix):
    buffer = io.BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4

    margin_x = 2 * cm
    y = height - 2 * cm

    # ======================
    # EN-TÊTE ENTREPRISE
    # ======================
    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(margin_x, y, "MON ENTREPRISE")
    y -= 14

    pdf.setFont("Helvetica", 9)
    pdf.drawString(margin_x, y, "Adresse de l'entreprise")
    y -= 12
    pdf.drawString(margin_x, y, "Email : contact@entreprise.fr")
    y -= 20

    # ======================
    # INFOS CLIENT
    # ======================
    pdf.setFont("Helvetica-Bold", 10)
    pdf.drawString(width - 9*cm, height - 2*cm, "Client :")
    pdf.setFont("Helvetica", 10)
    pdf.drawString(width - 9*cm, height - 2.7*cm, nom)
    pdf.drawString(width - 9*cm, height - 3.3*cm, email)

    # ======================
    # TITRE DEVIS
    # ======================
    y -= 10
    pdf.setFont("Helvetica-Bold", 18)
    pdf.drawString(margin_x, y, "DEVIS")
    y -= 20

    pdf.setFont("Helvetica", 10)
    pdf.drawString(margin_x, y, f"Numéro de devis : {numero}")
    y -= 14
    pdf.drawString(margin_x, y, f"Date : {date}")
    y -= 20

    # ======================
    # TABLEAU
    # ======================
    headers = [
        "Description", "Qté", "Unité", "Prix unitaire HT", "Total HT", "TVA"
    ]
    col_widths = [7*cm, 1.5*cm, 2*cm, 3*cm, 3*cm, 1.5*cm]

    pdf.setFont("Helvetica-Bold", 9)
    x = margin_x
    pdf.setFillColor(lightgrey)

    for i, h in enumerate(headers):
        pdf.rect(x, y, col_widths[i], 14, fill=1, stroke=1)
        pdf.setFillColor(black)
        pdf.drawString(x + 2, y + 4, h)
        x += col_widths[i]

    y -= 14
    pdf.setFont("Helvetica", 9)

    for l in lignes:
        x = margin_x
        total_ht_ligne = l["quantite"] * l["prix_unitaire"]

        values = [
            l["designation"],
            str(l["quantite"]),
            l.get("unite", ""),
            f"{l['prix_unitaire']:.2f} €",
            f"{total_ht_ligne:.2f} €",
            f"{l.get('tva', 20)} %"
        ]

        for i, v in enumerate(values):
            pdf.rect(x, y, col_widths[i], 14, stroke=1)
            pdf.drawString(x + 2, y + 4, v)
            x += col_widths[i]

        y -= 14

        if y < 4*cm:
            pdf.showPage()
            y = height - 2*cm
            pdf.setFont("Helvetica", 9)

    # ======================
    # TOTAUX
    # ======================
    y -= 20
    pdf.setFont("Helvetica-Bold", 10)
    pdf.drawRightString(width - margin_x, y, f"Total HT : {prix['total_ht']:.2f} €")
    y -= 14
    pdf.drawRightString(width - margin_x, y, f"TVA (20 %) : {prix['tva']:.2f} €")
    y -= 14
    pdf.drawRightString(width - margin_x, y, f"Total TTC : {prix['total_ttc']:.2f} €")

    # ======================
    # CONDITIONS
    # ======================
    y -= 30
    pdf.setFont("Helvetica", 9)
    pdf.drawString(margin_x, y, "Durée de validité : 30 jours")
    y -= 12
    pdf.drawString(margin_x, y, "Conditions de paiement : 30 % à la commande, solde à la livraison")

    # ======================
    # SIGNATURE
    # ======================
    y -= 30
    pdf.setFont("Helvetica-Bold", 9)
    pdf.drawString(margin_x, y, "Pour l'entreprise")
    pdf.drawString(width - 7*cm, y, "Pour le client")
    y -= 30
    pdf.drawString(margin_x, y, "Cachet & signature")
    pdf.drawString(width - 7*cm, y, "Lu et approuvé, bon pour accord")

    pdf.save()
    buffer.seek(0)
    return buffer
