import streamlit as st

1. CONFIGURATION
st.set_page_config(page_title="Réseau Social Institut", layout="centered")

2. MENU LATÉRAL
st.sidebar.title("Navigation")
page = st.sidebar.radio("Aller vers :", ["Connexion", "Inscription"])

3. PAGE D'INSCRIPTION
def afficher_inscription():
    st.title("🎓 Inscription")
    with st.form("inscription_form"):
        col1, col2 = st.columns(2)
        with col1:
            nom = st.text_input("Nom")
            prenom = st.text_input("Prénom")
            date_nays = st.date_input("Date de naissance")
        with col2:
            profession = st.text_input("Profession")
            ville = st.text_input("Ville")
            email = st.text_input("Email")
        password = st.text_input("Mot de passe", type="password")
        st.write("---")
        photo = st.file_uploader("📸 Photo de profil", type=['png', 'jpg'])
        submit = st.form_submit_button("S'inscrire")
        if submit:
            st.success("Compte créé !")

4. PAGE DE CONNEXION
def afficher_connexion():
    st.title("🔑 Connexion")
    with st.form("form_connexion"):
        email_log = st.text_input("Email")
        pass_log = st.text_input("Mot de passe", type="password")
        bouton_log = st.form_submit_button("Se connecter")
        if bouton_log:
            st.success("Connexion réussie !")

5. LOGIQUE D'AFFICHAGE
if page == "Inscription":
    afficher_inscription()
else:
    afficher_connexion()
