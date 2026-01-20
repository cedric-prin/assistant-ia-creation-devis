import os

# ======================
# OPENAI
# ======================
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise RuntimeError("❌ OPENAI_API_KEY non définie")

# ======================
# ENTREPRISE
# ======================
ENTREPRISE = {
    "nom": "Nom de ton entreprise",
    "adresse": "Adresse de l'entreprise",
    "email": "contact@entreprise.fr",
    "telephone": "01 23 45 67 89",
    "tva": "FR123456789"
}

TVA_TAUX = 0.20
