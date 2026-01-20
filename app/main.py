import streamlit as st
from datetime import datetime
import random
import json
import re

from ai import generer_devis
from pricing import calcul_prix
from pdf_generator import generer_pdf

def parse_json_safe(text):
    cleaned = re.sub(r"```json|```", "", text).strip()
    return json.loads(cleaned)

st.set_page_config("Générateur de devis", "📄")
st.title("📄 Générateur de devis intelligent")

with st.form("devis"):
    nom = st.text_input("Nom du client")
    email = st.text_input("Email")
    prestation = st.selectbox("Type de prestation", [
        "Site web", "Application mobile", "Maintenance", "Audit", "Autre"
    ])
    description = st.text_area("Description du besoin")
    budget = st.slider("Budget estimé (€)", 500, 20000, 2000)
    submit = st.form_submit_button("Générer le devis")

if submit:
    devis_json = generer_devis(nom, email, prestation, description, budget)

    try:
        devis = parse_json_safe(devis_json)
    except:
        st.error("JSON invalide généré par l'IA")
        st.code(devis_json)
        st.stop()

    lignes = devis["lignes"]
    prix = calcul_prix(lignes)

    st.subheader("📑 Détail du devis")
    st.table([
        {
            "Désignation": l["designation"],
            "Qté": l["quantite"],
            "PU (€)": l["prix_unitaire"],
            "Total (€)": l["quantite"] * l["prix_unitaire"]
        } for l in lignes
    ])

    st.markdown(f"""
**Total HT** : {prix['total_ht']} €  
**TVA (20%)** : {prix['tva']} €  
**Total TTC** : {prix['total_ttc']} €
""")

    pdf = generer_pdf(
        numero=f"D-{random.randint(1000,9999)}",
        date=datetime.now().strftime("%d/%m/%Y"),
        nom=nom,
        email=email,
        lignes=lignes,
        prix=prix
    )

    st.download_button("📥 Télécharger le devis PDF", pdf, "devis.pdf", "application/pdf")
