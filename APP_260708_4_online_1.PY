# python APP_260708_4_online_1.PY
# pyinstaller --onefile --windowed APP_260708_4.py
# streamlit run APP_260708_4_online_1.py

import streamlit as st
import random
from PIL import Image
import os

# Ρύθμιση της σελίδας (Τίτλος και Layout)
st.set_page_config(page_title="Οδηγός Μουσικών Δρόμων", layout="centered")

st.title("🎵 Οδηγός Μουσικών Δρόμων & Σχημάτων")
st.write("Επιλέξτε μια ενότητα από τις παρακάτω καρτέλες για να ξεκινήσετε τη μελέτη.")

# Λίστα με τις νότες για το Quiz
notes = ["ΝΤΟ", "ΡΕ", "ΜΙ", "ΦΑ", "ΣΟΛ", "ΛΑ", "ΣΙ"]

# 1. Λίστα με τους πλήρεις Δρόμους
dromoi = {
    "Αρμονικό Μινόρε": "ARMONIKO_MINORE.png",
    "Φυσικό Μινόρε": "FYSIKO_MINORE.png",
    "Γιουρού (Εκδοχή 1)": "GIOURNTI_9_notes_1.png",
    "Γιουρού (Εκδοχή 2)": "GIOURNTI_9_notes_2.png",
    "Καρτσιγάρ": "KARTSIGAR.png",
    "Νιαβέντ": "NIAVENT.png",
    "Νικρίζ (Ποιμενικό Μινόρε)": "NIKRIZ_or_POIMENIKO_MINORE.png",
    "Ραστ / Ματζόρε": "MAJORE_or_RAST.png",
    "Σεγκιάχ": "SEGKIAX.png",
    "Χιτζασκιάρ": "XITZASKIAR.png",
    "Χιτζάζ": "XITZAZ.png",
    "Χουζάμ": "XOUZAM.png"
}

# 2. Λίστα με τα Σχήματα / Παραλλαγές
sximata = {
    "Ματζόρε / Ραστ (5 Νότες)": "MAJORE_or_RAST_5_notes.png",
    "Ματζόρε / Ραστ (7 Νότες)": "MAJORE_or_RAST_7_notes.png",
    "Μινόρε (5 Νότες)": "MINORE_5_notes.png",
    "Μινόρε (7 Νότες)": "MINORE_7_notes.png",
    "Ουσάκ (Γενικό)": "OUSAK.png",
    "Ουσάκ (5 Νότες - Εκδ. 1)": "OUSAK_5_notes_1.png",
    "Ουσάκ (5 Νότες - Εκδ. 2)": "OUSAK_5_notes_2.png",
    "Ουσάκ (7 Νότες - Εκδ. 1)": "OUSAK_7_notes_1.png",
    "Ουσάκ (7 Νότες - Εκδ. 2)": "OUSAK_7_notes_2.png",
    "Πειραιώτικος (Γενικό)": "PEIRAIOTIKOS.png",
    "Πειραιώτικος (6 Νότες)": "PEIRAIOTIKOS_6_notes.png",
    "Πειραιώτικος (9 Νότες)": "PEIRAIOTIKOS_9_notes.png",
    "Σαμπάχ (Γενικό)": "SABAX.png",
    "Σαμπάχ (5 Νότες)": "SABAX_5_notes.png",
    "Σαμπάχ (7 Νότες)": "SABAX_7_notes.png",
    "Χιτζάζ (5 Νότες)": "XITZAZ_5_notes.png",
    "Χιτζάζ (7 Νότες)": "XITZAZ_7_notes.png",
    "Χουζάμ (5 Νότες)": "XOUZAM_5_notes.png",
    "Χουζάμ (7 Νότες)": "XOUZAM_7_notes.png"
}

# Δημιουργία των 4 Καρτελών (Tabs) στην κορυφή της ιστοσελίδας
tab1, tab2, tab3, tab4 = st.tabs(["🎼 Μουσικοί Δρόμοι", "📐 Σχήματα / Εκδοχές", "🎲 Τεστ Δρόμων", "🎲 Τεστ Σχημάτων"])

def ληψη_εικόνας(όνομα_αρχείου):
    """Βοηθητική συνάρτηση για ασφαλή φόρτωση εικόνας"""
    if os.path.exists(όνομα_αρχείου):
        return Image.open(όνομα_αρχείου)
    else:
        return None

# --- TAB 1: ΜΟΥΣΙΚΟΙ ΔΡΟΜΟΙ ---
with tab1:
    επιλογή_δρόμου = st.selectbox("Διαλέξτε Δρόμο:", list(dromoi.keys()), key="dromoi_select")
    img = ληψη_εικόνας(dromoi[επιλογή_δρόμου])
    if img:
        st.image(img, use_container_width=True)
    else:
        st.error(f"Δεν βρέθηκε η εικόνα: {dromoi[επιλογή_δρόμου]}")

# --- TAB 2: ΣΧΗΜΑΤΑ ---
with tab2:
    επιλογή_σχήματος = st.selectbox("Διαλέξτε Σχήμα / Παραλλαγή:", list(sximata.keys()), key="sximata_select")
    img = ληψη_εικόνας(sximata[επιλογή_σχήματος])
    if img:
        st.image(img, use_container_width=True)
    else:
        st.error(f"Δεν βρέθηκε η εικόνα: {sximata[επιλογή_σχήματος]}")

# --- TAB 3: ΤΕΣΤ ΔΡΟΜΩΝ ---
with tab3:
    st.subheader("🎲 Τυχαία Εξάσκηση στους Δρόμους")
    if st.button("🎲 Νέα Τυχαία Επιλογή Δρόμου", key="btn_quiz_d"):
        st.session_state.quiz_nota_d = random.choice(notes)
        st.session_state.quiz_name_d = random.choice(list(dromoi.keys()))
        st.session_state.show_img_d = False # Κρύψε την προηγούμενη εικόνα
    
    if "quiz_nota_d" in st.session_state:
        st.info(f"**ΠΑΙΞΤΕ:** Νότα **{st.session_state.quiz_nota_d}** και Δρόμο **{st.session_state.quiz_name_d}**")
        if st.button("👁️ Εμφάνιση Απάντησης / Δακτυλοθεσίας", key="btn_show_d"):
            st.session_state.show_img_d = True
            
        if st.session_state.get("show_img_d", False):
            img = ληψη_εικόνας(dromoi[st.session_state.quiz_name_d])
            if img:
                st.image(img, use_container_width=True)

# --- TAB 4: ΤΕΣΤ ΣΧΗΜΑΤΩΝ ---
with tab4:
    st.subheader("🎲 Τυχαία Εξάσκηση στα Σχήματα")
    if st.button("🎲 Νέα Τυχαία Επιλογή Σχήματος", key="btn_quiz_s"):
        st.session_state.quiz_nota_s = random.choice(notes)
        st.session_state.quiz_name_s = random.choice(list(sximata.keys()))
        st.session_state.show_img_s = False
        
    if "quiz_nota_s" in st.session_state:
        st.success(f"**ΠΑΙΞΤΕ:** Νότα **{st.session_state.quiz_nota_s}** και Σχήμα **{st.session_state.quiz_name_s}**")
        if st.button("👁️ Εμφάνιση Απάντησης / Δακτυλοθεσίας", key="btn_show_s"):
            st.session_state.show_img_s = True
            
        if st.session_state.get("show_img_s", False):
            img = ληψη_εικόνας(sximata[st.session_state.quiz_name_s])
            if img:
                st.image(img, use_container_width=True)