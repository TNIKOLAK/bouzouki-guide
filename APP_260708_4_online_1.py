import streamlit as st
import random
from PIL import Image
import os

# Ρύθμιση της σελίδας (Τίτλος και Layout)
st.set_page_config(page_title="Οδηγός Μουσικών Δρόμων", layout="centered")

st.title("🎵 Οδηγός Μουσικών Δρόμων & Σχημάτων")
st.write("Μουσική επιμέλεια: Θοδωρής Τζινέλλης")
st.write("Ανάπτυξη εφαρμογής: Θανάσης Νικολακόπουλος")
st.write("Επιλέξτε μια ενότητα από τις παρακάτω καρτέλες για να ξεκινήσετε τη μελέτη.")

# Λίστα με τις νότες για το Quiz
notes = ["ΝΤΟ", "ΡΕ", "ΜΙ", "ΦΑ", "ΣΟΛ", "ΛΑ", "ΣΙ"]

# 1. Ιεραρχική οργάνωση των Δρόμων σε Οικογένειες
oikogeneies_dromoi = {
    "Οικογένεια Μινόρε": {
        "Φυσικό Μινόρε": "FYSIKO_MINORE.png",
        "Αρμονικό Μινόρε": "ARMONIKO_MINORE.png",
        "Νιαβέντ": "NIAVENT.png",
        "Νικρίζ (Ποιμενικό Μινόρε)": "NIKRIZ_or_POIMENIKO_MINORE.png"
    },
    "Οικογένεια Χιτζάζ": {
        "Χιτζάζ": "XITZAZ.png",
        "Χιτζασκιάρ": "XITZASKIAR.png",
        "Πειραιώτικος": "PEIRAIOTIKOS.png"
    },
    "Οικογένεια Ματζόρε": {
        "Ραστ/Ματζόρε": "MAJORE_or_RAST.png",
        "Χουζάμ": "XOUZAM.png",
        "Σεγκιάχ": "SEGKIAX.png"
    },
    "Οικογένεια Ουσάκ": {
        "Ουσάκ": "OUSAK.png",
        "Σαμπάχ": "SABAX.png"
    },
    "Οικογένεια Καρτσιγάρ": {
        "Καρτσιγάρ": "KARTSIGAR.png",
        "Γιουρντί (Εκδοχή 1)": "GIOURNTI_9_notes_1.png",
        "Γιουρντί (Εκδοχή 2)": "GIOURNTI_9_notes_2.png"
    }
}

# Αντιστοίχιση δρόμων με video (μπορείς να προσθέσεις κι άλλα στο μέλλον)
dromoi_videos = {
    "Φυσικό Μινόρε": "fysiko_minore_2.mp4",
    "Αρμονικό Μινόρε": "armoniko_minore_1.mp4",
    "Νιαβέντ": "niavent_1.mp4",
    "Νικρίζ (Ποιμενικό Μινόρε)": "nikriz_1.mp4"  
}

# Επίπεδη λίστα όλων των δρόμων (για χρήση στο Quiz)
dromoi_quiz_pool = {}
for family_members in oikogeneies_dromoi.values():
    dromoi_quiz_pool.update(family_members)

# 2. Λίστα με τα Σχήματα / Παραλλαγές
sximata = {
    "Ματζόρε / Ραστ (5 Νότες)": "MAJORE_or_RAST_5_notes.png",
    "Ματζόρε / Ραστ (7 Νότες)": "MAJORE_or_RAST_7_notes.png",
    "Μινόρε (5 Νότες)": "MINORE_5_notes.png",
    "Μινόρε (7 Νότες)": "MINORE_7_notes.png",
    "Ουσάκ (5 Νότες - Εκδ. 1)": "OUSAK_5_notes_1.png",
    "Ουσάκ (5 Νότες - Εκδ. 2)": "OUSAK_5_notes_2.png",
    "Ουσάκ (7 Νότες - Εκδ. 1)": "OUSAK_7_notes_1.png",
    "Ουσάκ (7 Νότες - Εκδ. 2)": "OUSAK_7_notes_2.png",
    "Πειραιώτικος (6 Νότες)": "PEIRAIOTIKOS_6_notes.png",
    "Πειραιώτικος (9 Νότες)": "PEIRAIOTIKOS_9_notes.png",
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

# --- TAB 1: ΜΟΥΣΙΚΟΙ ΔΡΟΜΟΙ (Ιεραρχικά Dropdowns & Video) ---
with tab1:
    επιλογή_οικογένειας = st.selectbox(
        "Διαλέξτε Οικογένεια Δρόμων:", 
        list(oikogeneies_dromoi.keys()), 
        key="family_select"
    )
    
    διαθέσιμοι_δρόμοι = oikogeneies_dromoi[επιλογή_οικογένειας]
    επιλογή_δρόμου = st.selectbox(
        "Διαλέξτε Δρόμο:", 
        list(διαθέσιμοι_δρόμοι.keys()), 
        key="dromoi_select"
    )
    
    img = ληψη_εικόνας(διαθέσιμοι_δρόμοι[επιλογή_δρόμου])
    if img:
        st.image(img, use_container_width=True)
    else:
        st.error(f"Δεν βρέθηκε η εικόνα: {διαθέσιμοι_δρόμοι[επιλογή_δρόμου]}")

    # Έλεγχος και εμφάνιση video αν υπάρχει συνδεδεμένο αρχείο για τον επιλεγμένο δρόμο
    if επιλογή_δρόμου in dromoi_videos:
        video_file = dromoi_videos[επιλογή_δρόμου]
        if os.path.exists(video_file):
            with st.expander("🎬 Δείτε το επεξηγηματικό video"):
                st.video(video_file)
        else:
            st.warning(f"Το video '{video_file}' δεν βρέθηκε στον φάκελο.")

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
        st.session_state.quiz_name_d = random.choice(list(dromoi_quiz_pool.keys()))
        st.session_state.show_img_d = False
    
    if "quiz_nota_d" in st.session_state:
        st.info(f"**ΠΑΙΞΤΕ:** Νότα **{st.session_state.quiz_nota_d}** και Δρόμο **{st.session_state.quiz_name_d}**")
        if st.button("👁️ Εμφάνιση Απάντησης / Δακτυλοθεσίας", key="btn_show_d"):
            st.session_state.show_img_d = True
            
        if st.session_state.get("show_img_d", False):
            img = ληψη_εικόνας(dromoi_quiz_pool[st.session_state.quiz_name_d])
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
