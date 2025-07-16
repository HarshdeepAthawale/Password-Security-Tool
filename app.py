import streamlit as st
import hashlib
import string
import time
from itertools import product

# --- Security/Ethics Disclaimer ---
st.markdown("""
<div style='background-color:#fff3cd; color:#222; padding:10px; border-radius:5px; border:1px solid #ffeeba;'>
<b>Disclaimer:</b> This tool is for <b>educational purposes only</b>. Do not use it for unauthorized password cracking or malicious activities.
</div>
""", unsafe_allow_html=True)

st.title("🔐 Password Security Tool")
st.markdown("""
This web app helps you understand password security by:
- **Testing password strength** with instant feedback and suggestions.
- **Simulating password cracking** using dictionary and brute-force attacks.
""")

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# --- Helper Functions ---
def has_repeats(pw):
    return any(pw.count(c) > 2 for c in set(pw))

def has_keyboard_pattern(pw):
    patterns = ["qwerty", "asdf", "zxcv", "1234", "1111", "abcd"]
    pw_lower = pw.lower()
    return any(p in pw_lower for p in patterns)

def has_common_substitution(pw):
    subs = ["p@ssw0rd", "pa$$w0rd", "passw0rd", "p4ssword"]
    pw_lower = pw.lower()
    return any(s in pw_lower for s in subs)

def password_strength(pw, username=None):
    score = 0
    feedback = []
    if len(pw) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")
    if any(c.islower() for c in pw):
        score += 1
    else:
        feedback.append("Add lowercase letters.")
    if any(c.isupper() for c in pw):
        score += 1
    else:
        feedback.append("Add uppercase letters.")
    if any(c.isdigit() for c in pw):
        score += 1
    else:
        feedback.append("Add numbers.")
    if any(c in string.punctuation for c in pw):
        score += 1
    else:
        feedback.append("Add special symbols (e.g., !, @, #, etc.).")
    common_pw = ["password", "123456", "qwerty", "letmein", "admin", "welcome", "iloveyou"]
    if pw.lower() in common_pw:
        feedback.append("This is a very common password!")
        score = 1  # override to weak
    if has_repeats(pw):
        feedback.append("Avoid repeated characters (e.g., 'aaa', '111').")
        score = min(score, 2)
    if has_keyboard_pattern(pw):
        feedback.append("Avoid keyboard patterns (e.g., 'qwerty', 'asdf').")
        score = min(score, 2)
    if has_common_substitution(pw):
        feedback.append("Common substitutions like 'p@ssw0rd' are easily guessed.")
        score = min(score, 2)
    if username and username.lower() in pw.lower():
        feedback.append("Don't include your username in your password.")
        score = min(score, 2)
    return score, feedback

# --- Password Strength Tester ---
st.header("1. Password Strength Tester 🛡️")
st.markdown("""
Enter a password to test its strength. The tool checks for length, character variety, common patterns, and more.
""")
col1, col2 = st.columns([2,1])
with col1:
    password = st.text_input("Password", type="password", help="Type your password to see its strength.")
    username = st.text_input("(Optional) Username", help="Used to check if your password contains your username.")
    go_clicked = st.button("Go", key="go_strength")
with col2:
    st.markdown("**Strength Meter**")
    strength_bar = st.empty()

if password and go_clicked:
    score, feedback = password_strength(password, username)
    meter_color = ["#dc3545", "#fd7e14", "#ffc107", "#0d6efd", "#198754"]
    meter_labels = ["Very Weak", "Weak", "Moderate", "Strong", "Very Strong"]
    st.markdown(f"<div style='margin-top:10px;'><b>Strength:</b> <span style='color:{meter_color[score-1 if score>0 else 0]};'>{meter_labels[score-1 if score>0 else 0]}</span></div>", unsafe_allow_html=True)
    strength_bar.progress(score/5 if score<=5 else 1.0)
    if feedback:
        st.markdown("**Suggestions:**")
        for f in feedback:
            st.write(f"- {f}")

# --- Ethical Password Cracker ---
st.header("2. Ethical Password Cracker 🕵️‍♂️")
st.markdown("""
Enter a password to see its SHA-256 hash and try to crack it using a dictionary or brute-force attack. You can also upload your own dictionary file (one password per line).
""")
crack_password = st.text_input("Password to hash & crack", type="password", key="crack")
custom_dict = st.file_uploader("Upload custom dictionary (optional, .txt)", type=["txt"])
go_crack = st.button("Go", key="go_crack")

if crack_password and go_crack:
    hash_value = hashlib.sha256(crack_password.encode()).hexdigest()
    st.markdown(f"**SHA-256 Hash:** `{hash_value}`")
    st.markdown("---")
    st.markdown("### Try to crack the hash:")
    attack_type = st.radio("Choose attack type:", ("Dictionary Attack", "Brute-force Attack"))
    cracked = False
    attempt = None
    attempts = 0
    start_time = None
    end_time = None
    progress = st.empty()
    live_attempt = st.empty()
    if st.button("Start Attack"):
        with st.spinner("Cracking in progress..."):
            start_time = time.time()
            if attack_type == "Dictionary Attack":
                if custom_dict:
                    dictionary = [line.strip() for line in custom_dict.getvalue().decode("utf-8").splitlines() if line.strip()]
                else:
                    dictionary = ["password", "123456", "qwerty", "letmein", "admin", "welcome", "iloveyou", crack_password]
                total = len(dictionary)
                for idx, word in enumerate(dictionary):
                    attempts += 1
                    if hashlib.sha256(word.encode()).hexdigest() == hash_value:
                        cracked = True
                        attempt = word
                        break
                    if idx % 10 == 0 or idx == total-1:
                        progress.progress((idx+1)/total)
                        live_attempt.text(f"Tried: {word}")
                time.sleep(0.5)
            else:  # Brute-force Attack (up to 4 chars, a-z, 0-9)
                charset = string.ascii_lowercase + string.digits
                max_length = 4
                total = sum(len(charset)**l for l in range(1, max_length+1))
                count = 0
                for length in range(1, max_length+1):
                    for candidate in product(charset, repeat=length):
                        word = ''.join(candidate)
                        attempts += 1
                        count += 1
                        if hashlib.sha256(word.encode()).hexdigest() == hash_value:
                            cracked = True
                            attempt = word
                            break
                        if count % 1000 == 0 or count == total:
                            progress.progress(count/total)
                            live_attempt.text(f"Tried: {word}")
                    if cracked:
                        break
                time.sleep(0.5)
            end_time = time.time()
        progress.empty()
        live_attempt.empty()
        if cracked:
            st.success(f"Password cracked! The password is: '{attempt}' (Attempts: {attempts}, Time: {end_time-start_time:.2f}s)")
        else:
            st.error(f"Failed to crack the password after {attempts} attempts. (Time: {end_time-start_time:.2f}s)") 