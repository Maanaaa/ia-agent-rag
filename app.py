import ollama
import os # Permet de manipuler les chemins de fichiers

def load_data():
    with open("data/data.txt", "r", encoding="utf-8") as file:
        return file.read()

def chatter():
    referentiel = load_data()
    # Identité de l'IA
    instruction_agent = f"""Tu es un assistant expert en estimation de projets digitaux. Sois concis et pro. 
    Utilise ce référentiel uniquement : {referentiel} 
    Méthode de réponse : 
    1. Liste les éléments identifiés de la demande.
    2. Détaille le temps estimé pour chaque élément. 
    3. Applique les règles de calcul du référentiel.
    4. Termine par un récapitulatif clair. 
    5. Réponds en français, sans mise en forme."""
    print("Chatter avec l'IA")
    print("(Tape quitter pour arrêter)")

    while True:
        user_input = input("Vous : ")

        if user_input.lower() == "quitter":
            print("Stop")
            break
        
        try:
            # Envoyer la requête à l'IA
            response = ollama.generate(
                model="gemma3:4b",
                system=instruction_agent,
                prompt=user_input,
            )

            print(f"IA : {response['response']}\n")
            # Séparation entre les messages
            print("-"*30) 
        except Exception as e:
            print(f"Erreur : {e}")
            break

if __name__ == "__main__":
    chatter()