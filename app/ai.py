from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def generer_devis(nom, email, prestation, description, budget):
    prompt = f"""
IMPORTANT :
Tu dois répondre UNIQUEMENT avec un JSON VALIDE.
AUCUN texte avant ou après.
PAS de ```json
PAS de commentaires.

Structure OBLIGATOIRE :

{{
  "lignes": [
    {{
      "designation": "string",
      "quantite": 1,
      "prix_unitaire": 1000.0
    }}
  ],
  "delai": "string",
  "conditions": "string"
}}

Contraintes :
- Total proche de {budget} €
- Prestations réalistes
- Français professionnel

Client : {nom} ({email})
Prestation : {prestation}
Description : {description}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    return response.choices[0].message.content
