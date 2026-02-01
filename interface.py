import streamlit as st
import ollama
import os

# Titre de la page
st.set_page_config(page_title="Estimation de projets web", page_icon=":computer:")

def load_data():
    with open("data/data.txt", "r", encoding="utf-8") as file:
        return file.read()


# Design
st.title("Assistant - Estimation de tarfis de projets web")
st.markdown("""Décivrez vos besoins, et obtenez une estimation de tarifs personnalisée en quelques secondes.""")

user_input = st.text_input("Votre demande :", placeholder="Exemple : Je veux un site vitrine avec 3 pages et un formulaire de contact")

if st.button("Estimer"):
    if user_input.strip() == "":
        st.warning("Veuillez entrer une demande valide.")
    else:
        with st.spinner("Calcul en cours..."):
            try:
                referentiel = load_data()
                instruction_agent = f"""Tu es un assistant expert en estimation de projets digitaux. Sois concis et pro. 
                Utilise ce référentiel uniquement : {referentiel} 
                Méthode de réponse : 
                1. Liste les éléments identifiés de la demande.
                2. Détaille le temps estimé pour chaque élément. 
                3. Applique les règles de calcul du référentiel.
                4. Termine par un récapitulatif clair. 
                5. Réponds en français, sans mise en forme."""

                response = ollama.generate(
                    model="gemma3:4b",
                    system=instruction_agent,
                    prompt=user_input,
                )

                st.subheader("Résultat de l'estimation :")
                st.write(response['response'])

            except Exception as e:
                st.error(f"Erreur : {e}")

st.sidebar.info("Application par Théo Manya, dans le but de tester l'intégration de l'IA dans un projet web.")