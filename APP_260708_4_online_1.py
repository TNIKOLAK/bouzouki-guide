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
    
    # Εισαγωγικό Video για τα Μουσικά Σχήματα (Πριν την προτροπή επιλογής καρτέλας)
    intro_video_file = "mousika_sximata_eisagogi.mp4"
    if os.path.exists(intro_video_file):
        with st.expander("🎬 Εισαγωγικό Video: Μουσικά Σχήματα"):
            st.video(intro_video_file)
            
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
            <div style="font-size: 0.73rem; opacity: 0.75;">🕒 <i>Τελ. τροποποίηση: 26/11/2026</i></div>
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

# Αντιστοίχιση δρόμων με τοπικά εκπαιδευτικά video
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

# YouTube τραγούδια ανά δρόμο (λίστα από λεξικά)
dromoi_youtube_songs = {
    "Νικρίζ (Ποιμενικό Μινόρε)": [
        {
            "title": "Ο Μάρκος πολυτεχνίτης του Μ. Βαμβακάρη - Δρόμος Νικρίζ",
            "url": "https://www.youtube.com/watch?v=qZ01ridF_SA&t=2s"
        },
        {
            "title": "Ο Θερμαστής του Γ. Μπάτη - Δρόμος Νικρίζ",
            "url": "https://www.youtube.com/watch?v=Qx_w4P2bF18"
        }
    ],
    "Ουσάκ": [
        {
            "title": "Εγώ Μάγκας Φαινόμουνα - του Μ. Βαμβακάρη - Δρόμος Ουσάκ",
            "url": "https://youtu.be/luUzPuX8nwI"
        },
        {
            "title": "Οι μάγκες δεν υπάρχουν πια - του Ν. Παπάζογλου - Δρόμος Ουσάκ",
            "url": "https://youtu.be/jSmPR1CwZqk"
        },
        {
            "title": "Παλαμάκια - Ουσάκ δρόμος.mp4",
            "url": "https://youtu.be/JiVFFzcWm_Q"
        }
    ],
    "Χιτζάζ": [
        {
            "title": "Μικρός Αρραβωνιάστηκα - Δρόμος Χιτζάζ",
            "url": "https://youtu.be/GGwnYugGWFw"
        },
        {
            "section_title": "Νύχτωσε χωρίς Φεγγάρι",
            "videos": [
                {
                    "title": "Νύχτωσε χωρίς Φεγγάρι 1 - εισαγωγή Χιτζάζ δρόμος.mp4",
                    "url": "https://youtu.be/xH8aw7RQk2k"
                },
                {
                    "title": "Νύχτωσε χωρίς Φεγγάρι 2 - λόγια Χιτζάζ δρόμος.mp4",
                    "url": "https://youtu.be/dFrl_i6rwbk"
                },
                {
                    "title": "Νύχτωσε χωρίς φεγγάρι 3 ολόκληρο με μετρονόμο - Χιτζάζ δρόμος.mp4",
                    "url": "https://youtu.be/U5f9941wPIA"
                }
            ]
        }
    ],
    "Χιτζασκιάρ": [
        {
            "title": "Η γάτα - Χιτζασκάρ δρόμος.mp4",
            "url": "https://youtu.be/23aWbGc84oI"
        }
    ],
    "Σαμπάχ": [
        {
            "title": "Ήσουνα τι ήσουνα - Σαμπάχ δρόμος.mp4",
            "url": "https://youtu.be/a4PKxYnYAV8"
        }
    ],
    "Αρμονικό Μινόρε": [
        {
            "title": "Όλοι οι ρεμπέτες του ντουνιά - Μινόρε Αρμονικό δρόμος.mp4",
            "url": "https://youtu.be/2AMZ9IslYNo"
        }
    ],
    "Νιαβέντ": [
        {
            "title": "Προύσα Νικρίζ - Νιαβέντ δρόμοι.mp4",
            "url": "https://youtu.be/6b6-bmAIcEs"
        }
    ],
    "Γιουρντί": [
        {
            "title": "Τα νειάτα τα μπερμπάντικα - Γκιουρντί δρόμος.mp4",
            "url": "https://youtu.be/7aRl7Go6Vz4"
        }
    ],
    "Φυσικό Μινόρε": [
        {
            "title": "Το δικό μου πάπλωμα - Μινόρε Φυσικό δρόμος.mp4",
            "url": "https://youtu.be/49yvnh2TJQ4"
        }
    ],
    "Χουζάμ": [
        {
            "title": "Το φεγγάρι κάνει βόλτα - Χουζάμ δρόμος.mp4",
            "url": "https://youtu.be/2BX40sadU6I"
        }
    ]
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
        "Μινόρε (7 Νότες)": "MINORE_7_notes.png",
        "Νικρίζ (6 Νότες)": "NIKRIZ_or_POIMENIKO_MINORE.png",
        "Νιαβέντ (6 Νότες)": "NIAVENT.png"
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
        "Χιτζάζ (6 Νότες)": "Xitzaz_6Notes.png",
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

# YouTube βίντεο / τραγούδια ανά σχήμα
sximata_youtube_videos = {
    "Ματζόρε / Ραστ (5 Νότες)": [
        {
            "title": "Σήκω Χόρεψε Κουκλί Μου - Δρόμος Ραστ/Ματζόρε",
            "url": "https://youtu.be/sN2qVlu5WFw"
        }
    ],
    "Χιτζάζ (6 Νότες)": [
        {
            "title": "Χιτζαζ σχήμα 6 νότες.mp4",
            "url": "https://youtu.be/yfygSXNWOwg"
        },
        {
            "title": "Κουλουριώτικο μετρονόμος 120 σχήμα Χιτζαζ 6 νότες.mp4",
            "url": "https://youtu.be/4mmLwltMk4M"
        }
    ],
    "Χιτζάζ (5 Νότες)": [
        {
            "title": "Μικρός αραβωνιάστηκα - Χιτζάζ σχήμα 5 νότες.mp4",
            "url": "https://youtu.be/GGwnYugGWFw"
        }
    ],
    "Νικρίζ (6 Νότες)": [
        {
            "title": "Μάρκος Πολυτεχνίτης - Νικρίζ σχήμα 6 νότες.mp4",
            "url": "https://youtu.be/8wxF1leRzq0"
        }
    ],
    "Μινόρε (6 Νότες)": [
        {
            "title": "Μίλησέ μου - Μινόρε σχήμα 6 νότες.mp4",
            "url": "https://youtu.be/ize5MmUxA3I"
        }
    ],
    "Νιαβέντ (6 Νότες)": [
        {
            "title": "Το μινόρε του τεκέ - Νιαβέντ σχήμα 6 νότες.mp4",
            "url": "https://youtu.be/Aztztt--dog"
        }
    ],
    "Ουσάκ (5 Νότες)": [
        {
            "section_title": "Οι μάγκες δεν υπάρχουν πια",
            "videos": [
                {
                    "title": "Οι μάγκες δεν υπάρχουν πια 1 - εισαγωγή & λόγια - Ουσάκ σχήμα 5 νότες.mp4",
                    "url": "https://youtu.be/fYGfBKCNawE"
                },
                {
                    "title": "Οι μάγκες δεν υπάρχουν πια 2 - ολόκληρο - Ουσάκ σχήμα 5 νότες.mp4",
                    "url": "https://youtu.be/4ssGWeEbwlg"
                }
            ]
        }
    ]
}

# Επίπεδη λίστα όλων των σχημάτων (για χρήση στο Quiz)
sximata_quiz_pool = {}
for group_members in omades_sximata.values():
    sximata_quiz_pool.update(group_members)

# 3. Ιεραρχική οργάνωση Ρυθμών
rythmoi_data = {
    "Ζεϊμπέκικο": {
        "Κλασσικό Ζεϊμπέκικο": "6. Ρυθμός Ζεϊμπέκικο.png",
        "Καμιλιέρικο Ζεϊμπέκικο": None
    },
    "Χασάπικο": None,
    "Τσιφτετέλι": None
}


def ληψη_εικόνας(όνομα_αρχείου):
    """Βοηθητική συνάρτηση για ασφαλή φόρτωση εικόνας"""
    if όνομα_αρχείου and os.path.exists(όνομα_αρχείου):
        return Image.open(όνομα_αρχείου)
    return None


def αποδοση_media_λίστας(items_list, expander_label="🎶 Χαρακτηριστικά τραγούδια / video"):
    """Εμφανίζει λίστα μεμονωμένων video ή υπο-ενότητες video σε expander"""
    with st.expander(expander_label):
        for item in items_list:
            if "videos" in item:
                with st.expander(f"🎵 {item['section_title']}"):
                    for vid in item["videos"]:
                        st.markdown(f"**{vid['title']}**")
                        st.video(vid["url"])
                        st.markdown("---")
            else:
                st.markdown(f"**🎵 {item['title']}**")
                st.video(item["url"])
                st.markdown("---")


# --- ΔΥΟ ΜΕΓΑΛΕΣ ΕΝΟΤΗΤΕΣ ΕΦΑΡΜΟΓΗΣ ---
main_tab_dromoi_sximata, main_tab_rythmoi = st.tabs(["🎼 ΔΡΟΜΟΙ & ΣΧΗΜΑΤΑ", "🥁 ΡΥΘΜΟΙ"])

# ==============================================================================
# ΜΕΓΑΛΗ ΕΝΟΤΗΤΑ 1: ΔΡΟΜΟΙ & ΣΧΗΜΑΤΑ
# ==============================================================================
with main_tab_dromoi_sximata:
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "🎼 Μουσικοί Δρόμοι",
        "📐 Σχήματα / Εκδοχές",
        "🎲 Τεστ Δρόμων",
        "🎲 Τεστ Σχημάτων",
        "🔍 Αναζήτηση"
    ])

    # --- TAB 1: ΜΟΥΣΙΚΟΙ ΔΡΟΜΟΙ (Ιεραρχικά Dropdowns, Video & YouTube Τραγούδια) ---
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

        # 1. Τοπικό επεξηγηματικό video μαθήματος
        if επιλογή_δρόμου in dromoi_videos:
            video_file = dromoi_videos[επιλογή_δρόμου]
            if os.path.exists(video_file):
                with st.expander("🎬 Δείτε το επεξηγηματικό video"):
                    st.video(video_file)
            else:
                st.warning(f"Το video '{video_file}' δεν βρέθηκε στον φάκελο.")

        # 2. YouTube Videos για χαρακτηριστικά τραγούδια
        if επιλογή_δρόμου in dromoi_youtube_songs:
            αποδοση_media_λίστας(dromoi_youtube_songs[επιλογή_δρόμου], "🎶 Χαρακτηριστικά τραγούδια στο δρόμο αυτό")

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

        # Αυτόματη αντιστοίχιση του τοπικού video με βάση το όνομα της εικόνας
        video_file_sxima = img_name.replace(".png", ".mp4")
        if os.path.exists(video_file_sxima):
            with st.expander("🎬 Δείτε το επεξηγηματικό video"):
                st.video(video_file_sxima)

        # YouTube video / τραγούδια συνδεδεμένα με το συγκεκριμένο σχήμα
        if επιλογή_σχήματος in sximata_youtube_videos:
            αποδοση_media_λίστας(sximata_youtube_videos[επιλογή_σχήματος], "🎶 Χαρακτηριστικά τραγούδια / video στο σχήμα αυτό")

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

    # --- TAB 5: ΑΝΑΖΗΤΗΣΗ ---
    with tab5:
        st.subheader("🔍 Αναζήτηση με Λέξεις-Κλειδιά")
        query = st.text_input(
            "Πληκτρολογήστε λέξεις-κλειδιά (π.χ. χιτζάζ, ουσακ, μάρκος, συνεφιασμένη, 6 νότες, ζεϊμπέκικο):",
            key="search_query"
        ).strip().lower()

        if query:
            keywords = [k for k in query.split() if k]
            matches_found = False

            def matches_keywords(text):
                haystack = text.lower()
                return all(k in haystack for k in keywords)

            # 1. Αναζήτηση σε Δρόμους & Τραγούδια Δρόμων
            for fam_name, dromoi_dict in oikogeneies_dromoi.items():
                for dromos_name, img_file in dromoi_dict.items():
                    song_titles = []
                    for item in dromoi_youtube_songs.get(dromos_name, []):
                        if "videos" in item:
                            song_titles.append(item.get("section_title", ""))
                            song_titles.extend(v.get("title", "") for v in item["videos"])
                        else:
                            song_titles.append(item.get("title", ""))

                    combined_dromos_text = f"{fam_name} {dromos_name} {' '.join(song_titles)}"
                    if matches_keywords(combined_dromos_text):
                        matches_found = True
                        with st.expander(f"🎼 Δρόμος: {dromos_name} ({fam_name})", expanded=True):
                            img = ληψη_εικόνας(img_file)
                            if img:
                                st.image(img, use_container_width=True)
                            if dromos_name in dromoi_youtube_songs:
                                for item in dromoi_youtube_songs[dromos_name]:
                                    if "videos" in item:
                                        st.markdown(f"**🎵 {item['section_title']}**")
                                        for vid in item["videos"]:
                                            st.markdown(f"- {vid['title']}")
                                            st.video(vid["url"])
                                    else:
                                        st.markdown(f"**🎵 {item['title']}**")
                                        st.video(item["url"])

            # 2. Αναζήτηση σε Σχήματα & Video Σχημάτων
            for grp_name, sximata_dict in omades_sximata.items():
                for sxima_name, img_file in sximata_dict.items():
                    vid_titles = []
                    for item in sximata_youtube_videos.get(sxima_name, []):
                        if "videos" in item:
                            vid_titles.append(item.get("section_title", ""))
                            vid_titles.extend(v.get("title", "") for v in item["videos"])
                        else:
                            vid_titles.append(item.get("title", ""))

                    combined_sxima_text = f"{grp_name} {sxima_name} {' '.join(vid_titles)}"
                    if matches_keywords(combined_sxima_text):
                        matches_found = True
                        with st.expander(f"📐 Σχήμα: {sxima_name} ({grp_name})", expanded=True):
                            img = ληψη_εικόνας(img_file)
                            if img:
                                st.image(img, use_container_width=True)
                            if sxima_name in sximata_youtube_videos:
                                for item in sximata_youtube_videos[sxima_name]:
                                    if "videos" in item:
                                        st.markdown(f"**🎵 {item['section_title']}**")
                                        for vid in item["videos"]:
                                            st.markdown(f"- {vid['title']}")
                                            st.video(vid["url"])
                                    else:
                                        st.markdown(f"**🎵 {item['title']}**")
                                        st.video(item["url"])

            # 3. Αναζήτηση σε Ρυθμούς
            for rythm_name, sub_content in rythmoi_data.items():
                if isinstance(sub_content, dict):
                    for sub_name, r_img in sub_content.items():
                        if matches_keywords(f"ρυθμός {rythm_name} {sub_name}"):
                            matches_found = True
                            with st.expander(f"🥁 Ρυθμός: {sub_name} ({rythm_name})", expanded=True):
                                img = ληψη_εικόνας(r_img)
                                if img:
                                    st.image(img, use_container_width=True)
                                else:
                                    st.info("Δεν υπάρχει ακόμη υλικό για αυτή την υποενότητα.")
                else:
                    if matches_keywords(f"ρυθμός {rythm_name}"):
                        matches_found = True
                        with st.expander(f"🥁 Ρυθμός: {rythm_name}", expanded=True):
                            st.info("Δεν υπάρχει ακόμη υλικό για αυτή την ενότητα.")

            if not matches_found:
                st.warning("Δεν βρέθηκαν αποτελέσματα για τις λέξεις-κλειδιά που εισαγάγατε.")


# ==============================================================================
# ΜΕΓΑΛΗ ΕΝΟΤΗΤΑ 2: ΡΥΘΜΟΙ
# ==============================================================================
with main_tab_rythmoi:
    st.subheader("🥁 Ρυθμοί")

    rythmos_tab_zeimpekiko, rythmos_tab_xasapiko, rythmos_tab_tsifteteli = st.tabs([
        "Ζεϊμπέκικο",
        "Χασάπικο",
        "Τσιφτετέλι"
    ])

    # --- ΥΠΟΕΝΟΤΗΤΑ: ΖΕΪΜΠΕΚΙΚΟ ---
    with rythmos_tab_zeimpekiko:
        sub_tab_klassiko, sub_tab_kamilieriko = st.tabs([
            "Κλασσικό Ζεϊμπέκικο",
            "Καμιλιέρικο Ζεϊμπέκικο"
        ])

        with sub_tab_klassiko:
            klassiko_img_name = rythmoi_data["Ζεϊμπέκικο"]["Κλασσικό Ζεϊμπέκικο"]
            img = ληψη_εικόνας(klassiko_img_name)
            if img:
                st.image(img, use_container_width=True)
            else:
                st.error(f"Δεν βρέθηκε η εικόνα: {klassiko_img_name}")

        with sub_tab_kamilieriko:
            pass

    # --- ΥΠΟΕΝΟΤΗΤΑ: ΧΑΣΑΠΙΚΟ ---
    with rythmos_tab_xasapiko:
        pass

    # --- ΥΠΟΕΝΟΤΗΤΑ: ΤΣΙΦΤΕΤΕΛΙ ---
    with rythmos_tab_tsifteteli:
        pass
