import ollama
import os

# Configuration admin (réglage de "l'agence")
CONFIG = {
    "agency_name": "Manéo Studio",
    "statut": "Freelance",
    "stack_default": "HTML, CSS, JavaScript, PHP, MySQL, Wordpress, Bricks, Elementor, WooCommerce.",
    "seniority": "Junior",
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

    # Définition des instructions de longueur
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

    # Injection dynamique des paramètres CONFIG dans le prompt
    # C'est ici que l'IA prend connaissance de tes variables Python
    config_instruction = f"""
    PARAMÈTRES DE L'AGENCE À APPLIQUER :
    - Nom de l'agence : {CONFIG['agency_name']}
    - Statut : {CONFIG['statut']}
    - Stack technique imposée : {CONFIG['stack_default']}
    - Expérience : {CONFIG['seniority']}
    - Marge de sécurité technique : x{CONFIG['marge_securite']} (Multiplier les heures par ce coefficient)
    - Frais de gestion : {CONFIG['management_fees']} (À ajouter au montant final)
    """

    # On transforme la query en data brute
    prompt_formate = f"""
    DONNÉES TECHNIQUES À TRAITER :
    ---
    REQUÊTE DU CLIENT : {user_query}
    ---
    INSTRUCTION : Extraire les modules UTA et calculer selon le référentiel et les paramètres d'agence fournis.
    """

    # Construction du prompt système
    instruction_agent = f"""
    Tu es un ALGORITHME d'analyse technique froid et factuel pour {CONFIG['agency_name']}.
    {config_instruction}

    MISSION : Convertis le besoin en unités techniques (UTA) sans aucune émotion.
    
    MÉTHODE DE CALCUL OBLIGATOIRE :
    1. Sommer les heures du REFERENTIEL pour chaque module identifié.
    2. Multiplier ce total d'heures par la marge de sécurité (x{CONFIG['marge_securite']}).
    3. Calculer le prix : (Heures après marge * 65€).
    4. Ajouter les forfaits fixes du référentiel (SEO, Licences).
    5. Ajouter les frais de gestion ({CONFIG['management_fees']}) sur le total cumulé.
    6. Produire le MONTANT TOTAL HT FINAL.

    RÈGLES DE NEUTRALITÉ :
    1. Ignore les adjectifs (beau, pas cher, nul, vite).
    2. Utilise uniquement les chiffres du REFERENTIEL.
    3. Sois mathématique. Une heure (1h) vaut TOUJOURS 65€.
    4. Le montant final ne peut être inférieur à 1000€.

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