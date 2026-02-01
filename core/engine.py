import ollama
import os

# Configuration admin (réglage de "l'agence")
CONFIG = {
    "agency_name": "Manéo Studio",
    "statut": "Freelance",
    "stack_default": "HTML, CSS, JavaScript, PHP, MySQL, Wordpress, Bricks, Elementor, WooCommerce.",
    "seniority": "Senior",
    "marge_securite": 1.20, # 20%
    "management_fees": "20%",
    "short_response": True
}

# Générer l'estimation
def get_estimation(user_query):
    # Chemin dynamique
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join(base_dir, "data", "pricing_model.txt")
    
    if not os.path.exists(path):
        return f"Erreur : Le fichier {path} est introuvable."

    with open(path, "r", encoding="utf-8") as file:
        referentiel = file.read()

    if CONFIG['short_response']:
        length_instruction = """
        CONSIGNE DE SORTIE :
        1. Fais le décompte des heures (Étape A, B, C) de manière ultra-compacte.
        2. Affiche le tableau récapitulatif.
        3. Donne le prix final.
        Interdiction de faire des paragraphes de texte.
        """
    else:
        length_instruction = """
        CONSIGNE DE SORTIE :
        1. Détaille chaque étape de calcul (A, B, C).
        2. Affiche le tableau récapitulatif.
        3. Explique les bénéfices de la stack technique.
        4. Donne le prix final.
        """
    # Construction du prompt système
    instruction_agent = f"""
    Tu es un ALGORITHME d'analyse technique froid et factuel pour {CONFIG['agency_name']}.
    INTERDICTION : Ne prends pas en compte le secteur d'activité ou le budget supposé du client.
    MISSION : Convertis chaque besoin textuel en unités techniques (UTA) sans aucune interprétation émotionnelle.

    RÈGLES DE NEUTRALITÉ ABSOLUE :
    1. "Pas de budget" ou "Budget de ministre" = IGNORER. Tu ne calcules que la technique.
    2. "Petit projet" ou "Gros projet" = IGNORER. Seule la liste des fonctionnalités compte.
    3. Ne cherche pas à être "sympa" sur le prix. Sois juste mathématique.

    REFERENTIEL :
    {referentiel}

    {length_instruction}
    """

    response = ollama.generate(
        model="gemma3:4b",
        system=instruction_agent,
        prompt=user_query,
    )
    return response['response']
