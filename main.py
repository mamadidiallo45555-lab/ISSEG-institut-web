import streamlit as st

def formulaire_inscription():
    st.title("🎓 Inscription à l'Institut")
    st.subheader("Créez votre compte pour accéder aux actualités")

    # Création des champs que tu as demandés
    with st.form("inscription_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            nom = st.text_input("Nom")
            prenom = st.text_input("Prénom")
            date_nays = st.date_input("Date de naissance")
            lieu_nays = st.text_input("Lieu de naissance")
            
        with col2:
            profession = st.text_input("Profession")
            ville = st.text_input("Ville")
            email = st.text_input("Email")
            password = st.text_input("Mot de passe", type="password")

        submit_button = st.form_submit_button("S'inscrire")

        if submit_button:
            # Ici, nous ajouterons la logique pour envoyer les données à Supabase
            st.success(f"Bienvenue {prenom} ! Votre profil est en cours de création.")

# Appel de la fonction
formulaire_inscription()
