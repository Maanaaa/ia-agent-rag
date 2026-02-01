import ollama
import os # Permet de manipuler les chemins de fichiers

def chatter():
    # Identité de l'IA
    instruction_agent = "Tu es un assistant expert en estimation de projets digitaux. Sois concis et pro."
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