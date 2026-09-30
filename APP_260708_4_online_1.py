import streamlit as st
import random
from PIL import Image
import os

# Ρύθμιση της σελίδας (Τίτλος και Layout)
st.set_page_config(page_title="Οδηγός Μουσικών Δρόμων", layout="centered")

# --- HEADER: Τίτλος (Αριστερά) και Κάρτα Συντελεστών (Δεξιά) ---
col_title, col_credits = st.columns([5, 2], vertical_alignment="center")

with col_title:
    st.title("🎵 Οδηγός Μουσικών Δρόμων & Σχημάτων")
    st.write("Επιλέξτε μια ενότητα από τις παρακάτω καρτέλες για να ξεκινήσετε τη μελέτη.")

with col_credits:
    st.markdown(
        """
        <div style="
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.15);
            border-radius: 10px;
            padding: 10px 14px;
            font-size: 0.82rem;
            line-height: 1.45;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
        ">
            <div>🎼 <b>Μουσική επιμέλεια:</b><br>&nbsp;&nbsp;&nbsp;&nbsp;Θοδωρής Τζινέλλης</div>
            <div style="margin-top: 6px;">💻 <b>Ανάπτυξη εφαρμογής:</b><br>&nbsp;&nbsp;&nbsp;&nbsp;Θανάσης Νικολακόπουλος</div>
            <hr style="margin: 7px 0; border: 0; border-top: 1px solid rgba(255, 255, 255, 0.12);">
            <div style="font-size: 0.73rem; opacity: 0.75;">🕒 <i>Τελ. τροποποίηση: 29/09/2026</i></div>
        </div>
        """,
        unsafe_allow_html=True
    )

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
        "Ουσάκ": "OUSAK.png"
    },
    "Οικογένεια Σαμπάχ": {
        "Σαμπάχ": "SABAX.png"
    },
    "Οικογένεια Καρτσιγάρ": {
        "Καρτσιγάρ": "KARTSIGAR.png",
        "Γιουρντί": "GKOURNTI_1.png"
    }
}

# Αντιστοίχιση δρόμων με video
dromoi_videos = {
    "Φυσικό Μινόρε": "fysiko_minore_2.mp4",
    "Αρμονικό Μινόρε": "armoniko_minore_1.mp4",
    "Νιαβέντ": "niavent_1.mp4",
    "Νικρίζ (Ποιμενικό Μινόρε)": "nikriz_1.mp4",
    "Χιτζάζ": "xitzaz.mp4",
    "Χιτζασκιάρ": "xitzaskar_1.mp4",
    "Πειραιώτικος": "peiraiotikos.mp4",
    "Ραστ/Ματζόρε": "majore.mp4",
    "Χουζάμ": "xouzam.mp4",
    "Σεγκιάχ": "segiax.mp4",
    "Ουσάκ": "ousak.mp4",
    "Σαμπάχ": "sabax.mp4",
    "Καρτσιγάρ": "kartsigar.mp4",
    "Γιουρντί": "giournti_1.mp4"  
}

# Επίπεδη λίστα όλων των δρόμων (για χρήση στο Quiz)
dromoi_quiz_pool = {}
for family_members in oikogeneies_dromoi.values():
    dromoi_quiz_pool.update(family_members)

# 2. Ιεραρχική οργάνωση των Σχημάτων σε Ομάδες
omades_sximata = {
    "Ομάδα Ματζόρε / Ραστ": {
        "Ματζόρε / Ραστ (5 Νότες)": "MAJORE_or_RAST_5_notes.png",
        "Ματζόρε / Ραστ (7 Νότες)": "MAJORE_or_RAST_7_notes.png"
    },
    "Ομάδα Μινόρε": {
        "Μινόρε (6 Νότες)": "MINORE_6_notes.png",
        "Μινόρε (7 Νότες)": "MINORE_7_notes.png"
    },
    "Ομάδα Ουσάκ": {
        "Ουσάκ (5 Νότες)": "OUSAK_5_notes_1.png",
        "Ουσάκ (6 Νότες)": "OUSAK_6_notes.png",
        "Ουσάκ (7 Νότες - Εκδ. 1)": "OUSAK_7_notes_1.png",
        "Ουσάκ (7 Νότες - Εκδ. 2)": "OUSAK_7_notes_2.png"
    },
    "Ομάδα Πειραιώτικος": {
        "Πειραιώτικος (6 Νότες)": "PEIRAIOTIKOS_6_notes.png",
        "Πειραιώτικος (9 Νότες)": "PEIRAIOTIKOS_9_notes.png"
    },
    "Ομάδα Σαμπάχ": {
        "Σαμπάχ (5 Νότες)": "SABAX_5_notes.png",
        "Σαμπάχ (7 Νότες)": "SABAX_7_notes.png"
    },
    "Ομάδα Χιτζάζ": {
        "Χιτζάζ (5 Νότες)": "XITZAZ_5_notes.png",
        "Χιτζάζ (7 Νότες)": "XITZAZ_7_notes.png"
    },
    "Ομάδα Χουζάμ": {
        "Χουζάμ (5 Νότες)": "XOUZAM_5_notes.png",
        "Χουζάμ (7 Νότες)": "XOUZAM_7_notes.png"
    },
    "Ομάδα Γιουρντί": {
        "Γιουρντί (9 Νότες Εκδοχή 1)": "GIOURNTI_9_notes_1.png",
        "Γιουρντί (9 Νότες Εκδοχή 2)": "GIOURNTI_9_notes_2.png"
    }
}

# Επίπεδη λίστα όλων των σχημάτων (για χρήση στο Quiz)
sximata_quiz_pool = {}
for group_members in omades_sximata.values():
    sximata_quiz_pool.update(group_members)

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

    if επιλογή_δρόμου in dromoi_videos:
        video_file = dromoi_videos[επιλογή_δρόμου]
        if os.path.exists(video_file):
            with st.expander("🎬 Δείτε το επεξηγηματικό video"):
                st.video(video_file)
        else:
            st.warning(f"Το video '{video_file}' δεν βρέθηκε στον φάκελο.")

# --- TAB 2: ΣΧΗΜΑΤΑ (Ιεραρχικά Dropdowns & Video) ---
with tab2:
    επιλογή_ομάδας = st.selectbox(
        "Διαλέξτε Ομάδα Σχημάτων:", 
        list(omades_sximata.keys()), 
        key="group_select"
    )
    
    διαθέσιμα_σχήματα = omades_sximata[επιλογή_ομάδας]
    επιλογή_σχήματος = st.selectbox(
        "Διαλέξτε Σχήμα / Παραλλαγή:", 
        list(διαθέσιμα_σχήματα.keys()), 
        key="sximata_select"
    )
    
    img_name = διαθέσιμα_σχήματα[επιλογή_σχήματος]
    img = ληψη_εικόνας(img_name)
    if img:
        st.image(img, use_container_width=True)
    else:
        st.error(f"Δεν βρέθηκε η εικόνα: {img_name}")

    # Αυτόματη αντιστοίχιση του video με βάση το όνομα της εικόνας αλλάζοντας την κατάληξη σε .mp4
    video_file_sxima = img_name.replace(".png", ".mp4")
    if os.path.exists(video_file_sxima):
        with st.expander("🎬 Δείτε το επεξηγηματικό video"):
            st.video(video_file_sxima)

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
        st.session_state.quiz_name_s = random.choice(list(sximata_quiz_pool.keys()))
        st.session_state.show_img_s = False
        
    if "quiz_nota_s" in st.session_state:
        st.success(f"**ΠΑΙΞΤΕ:** Νότα **{st.session_state.quiz_nota_s}** και Σχήμα **{st.session_state.quiz_name_s}**")
        if st.button("👁️ Εμφάνιση Απάντησης / Δακτυλοθεσίας", key="btn_show_s"):
            st.session_state.show_img_s = True
            
        if st.session_state.get("show_img_s", False):
            img = ληψη_εικόνας(sximata_quiz_pool[st.session_state.quiz_name_s])
            if img:
                st.image(img, use_container_width=True)
