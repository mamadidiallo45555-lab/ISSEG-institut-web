import streamlit as st

def formulaire_inscription():
    st.title("🎓 Inscription à l'Institut")
    st.subheader("Créez votre compte pour accéder aux actualités")

    # Création du formulaire d'inscription
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

        # --- SECTION AJOUTÉE : PHOTO DE PROFIL ---
        st.write("---")
        st.write("📸 **Ma Photo de Profil**")
        photo_profil = st.file_uploader("Choisissez une image (JPG, PNG)", type=['png', 'jpg', 'jpeg'])
        
        # Petit aperçu si l'étudiant choisit une photo
        if photo_profil is not None:
            st.image(photo_profil, caption="Aperçu de votre photo", width=150)
        # ------------------------------------------

        submit_button = st.form_submit_button("S'inscrire")

        if submit_button:
            # Pour l'instant, on simule la réussite
            if nom and prenom and email and password:
                st.success(f"Bienvenue {prenom} ! Votre profil avec photo est prêt à être enregistré.")
            else:
                st.error("Veuillez remplir les champs obligatoires (Nom, Prénom, Email, Mot de passe).")

# Appel de la fonction pour afficher le formulaire
formulaire_inscription()
