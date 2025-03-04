import re
import random
import string
import streamlit as st

# List of common weak passwords
COMMON_PASSWORDS = {"password123", "12345678", "qwerty", "123456789", "letmein", "admin"}

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []
    
    # Custom scoring weights
    length_weight = 2
    case_weight = 1.5
    digit_weight = 1.5
    special_char_weight = 2
    
    # Check for common weak passwords
    if password in COMMON_PASSWORDS:
        return 0, ["❌ Your password is too common. Choose a more unique password."]
    
    # Length Check
    if len(password) >= 8:
        score += length_weight
    else:
        feedback.append("❌ Password should be at least 8 characters long.")
    
    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += case_weight
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")
    
    # Digit Check
    if re.search(r"\d", password):
        score += digit_weight
    else:
        feedback.append("❌ Add at least one number (0-9).")
    
    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += special_char_weight
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")
    
    return score, feedback

# Function to generate a strong password
def generate_password():
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(characters) for _ in range(12))

# Streamlit UI
st.title("🔐 Password Strength Meter")

# User input
password = st.text_input("Enter your password:", type="password")

if st.button("Check Password Strength"):
    if password:
        score, feedback = check_password_strength(password)
        
        # Display feedback with strength bar
        st.progress(score / 7, text=f"Password Strength: {score:.1f}/7")
        
        if score >= 6:
            st.success("✅ Strong Password!")
        elif score >= 4:
            st.warning("⚠️ Moderate Password - Consider adding more security features.")
        else:
            st.error("❌ Weak Password - Improve it using the suggestions below.")
        
        for item in feedback:
            st.write(item)
    else:
        st.error("Please enter a password to check.")

# Password Generator Section
st.subheader("🔑 Generate a Strong Password")
if st.button("Generate Strong Password"):
    strong_password = generate_password()
    st.text_input("Suggested Strong Password:", strong_password)
