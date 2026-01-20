# Générateur de Devis Intelligent

## Présentation

Ce projet est une application web permettant de générer des devis professionnels de manière automatisée et intelligente grâce à l'IA (OpenAI). L'utilisateur renseigne les informations du client et la prestation souhaitée, l'IA propose un devis détaillé, calcule les prix, génère un PDF et sauvegarde le tout en base de données.

## Fonctionnalités

- Génération automatique de devis via OpenAI (GPT-4o)
- Calcul des prix HT, TVA et TTC
- Génération de devis au format PDF (ReportLab)
- Interface utilisateur simple via Streamlit
- Sauvegarde des devis en base SQLite
- Gestion des informations client et entreprise
- Personnalisation des prestations et du budget
- Téléchargement du devis PDF
- (À venir) Envoi du devis par email

## Structure du projet

```
app/
│   ai.py              # Génération du devis via OpenAI
│   config.py          # Configuration (API, entreprise, TVA)
│   email_sender.py    # Envoi du devis par email (à compléter)
│   main.py            # Application Streamlit (frontend)
│   pdf_generator.py   # Génération du PDF du devis
│   pricing.py         # Calcul des prix
│   storage.py         # Sauvegarde en base SQLite
│   assets/            # (Ressources statiques)
data/
	 devis.db           # Base de données SQLite (générée automatiquement)
requirements.txt       # Dépendances Python
README.md              # Documentation
```

## Installation

1. **Cloner le projet :**
	```bash
	git clone <url-du-repo>
	cd creation-devis
	```

2. **Créer un environnement virtuel :**
	```bash
	python -m venv venv
	source venv/Scripts/activate  # Windows
	```

3. **Installer les dépendances :**
	```bash
	pip install -r requirements.txt
	```

4. **Configurer la clé OpenAI :**
	- Créer un fichier `.env` à la racine :
	  ```
	  OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxx
	  ```
	- Ou définir la variable d'environnement `OPENAI_API_KEY`.

5. **Lancer l'application :**
	```bash
	streamlit run app/main.py
	```

## Utilisation

- Accéder à l'interface Streamlit.
- Remplir le formulaire client et prestation.
- Générer le devis.
- Télécharger le PDF.
- Les devis sont sauvegardés dans la base locale `data/devis.db`.

## Dépendances principales

- `streamlit` : Interface web
- `openai` : Génération IA
- `reportlab` : Génération PDF
- `sqlite3` : Base de données
- Autres : voir `requirements.txt`

## Personnalisation

- Modifier les infos d'entreprise dans `app/config.py`.
- Adapter le prompt IA dans `app/ai.py` pour personnaliser le style des devis.

## À venir

- Envoi automatique du devis par email (`app/email_sender.py`)
- Tableau de bord des devis générés
- Export CSV/Excel

## Contact

Pour toute question ou suggestion, contactez :  
**Email** : prin.cedric.34@gmail.com
