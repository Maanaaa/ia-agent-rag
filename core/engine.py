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
        1. Fais le décompte des heures de manière ultra-compacte.
        2. Affiche le tableau récapitulatif.
        3. Donne le prix final.
        Interdiction de faire des paragraphes de texte.
        """
    else:
        length_instruction = """
        CONSIGNE DE SORTIE :
        1. Détaille chaque étape de calcul.
        2. Affiche le tableau récapitulatif.
        3. Explique les bénéfices de la stack technique.
        4. Donne le prix final.
        """

    # On transforme la query en data brute
    prompt_formate = f"""
    DONNÉES TECHNIQUES À TRAITER :
    ---
    REQUÊTE : {user_query}
    ---
    INSTRUCTION : Extraire les modules UTA et calculer selon le référentiel.
    """

    # Construction du prompt système
    instruction_agent = f"""
    Tu es un ALGORITHME d'analyse technique froid et factuel pour {CONFIG['agency_name']}.
    INTERDICTION : Ne prends pas en compte le secteur d'activité ou le budget.
    MISSION : Convertis le besoin en unités techniques (UTA) sans aucune émotion.

    RÈGLES DE NEUTRALITÉ :
    1. Ignore les adjectifs (beau, pas cher, nul, vite).
    2. Utilise uniquement les chiffres du REFERENTIEL.
    3. Sois mathématique.

    REFERENTIEL :
    {referentiel}

    {length_instruction}
    """

    # OPTIONS DE VERROUILLAGE POUR EMPECHER LA CREATIVITE
    response = ollama.generate(
        model="gemma3:4b",
        system=instruction_agent,
        prompt=prompt_formate,
        options={
            "temperature": 0.0,  # Supprime l'aléatoire
            "seed": 42,          # Fixe la graine de génération
            "top_k": 1,          # Force le choix du mot le plus probable
            "top_p": 0.0         # Filtre strict
        }
    )
    return response['response']