import streamlit as st
import hashlib
import string
import time
from itertools import product

# --- Security/Ethics Disclaimer ---
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown("""
<div style='background-color:#fff3cd; color:#222; padding:10px; border-radius:5px; border:1px solid #ffeeba;'>
<b>Disclaimer:</b> This tool is for <b>educational purposes only</b>. Do not use it for unauthorized password cracking or malicious activities.
</div>
""", unsafe_allow_html=True)

st.title("🔐 Password Security Tool")
st.markdown("""
This web app helps you understand password security by:
- **Testing password strength** with instant feedback and suggestions.
""")

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

# --- Password to SHA-256 Hash Converter ---
st.header("1. Password to SHA-256 Hash Converter 🧮")
sha_password = st.text_input("Enter a password to convert to SHA-256 hash", key="sha_input", type="password")
go_sha = st.button("Go", key="go_sha")
if sha_password and go_sha:
    st.markdown("""
    See how your password is transformed into a secure, irreversible SHA-256 hash. This is how passwords are typically stored by websites.
    """)
    st.markdown(f"**SHA-256 Hash:** `{hashlib.sha256(sha_password.encode()).hexdigest()}`")

# --- Password Strength Tester ---
st.header("2. Password Strength Tester 🛡️")
st.markdown("""
Enter a password to test its strength. The tool checks for length, character variety, common patterns, and more.
""")
col1, col2 = st.columns([2,1])
with col1:
    password = st.text_input("Password", type="password", help="Type your password to see its strength.", key="strength_input")
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
        st.markdown("<br><b>How to Improve Your Password:</b>", unsafe_allow_html=True)
        for f in feedback:
            st.markdown(f"❌ {f}")
    else:
        st.markdown("<br><b>✅ Your password is strong! Good job!</b>", unsafe_allow_html=True) 