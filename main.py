import re
import random
import string
import streamlit as st

# List of common weak passwords
COMMON_PASSWORDS = {"password123", "12345678", "qwerty", "123456789", "letmein", "admin"}

# Initialize session state for password history
if "password_history" not in st.session_state:
    st.session_state.password_history = []

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []
    
    length_weight = 2
    case_weight = 1.5
    digit_weight = 1.5
    special_char_weight = 2
    
    if password in COMMON_PASSWORDS:
        return 0, ["❌ Your password is too common. Choose a more unique password."]
    
    if len(password) >= 8:
        score += length_weight
    else:
        feedback.append("❌ Password should be at least 8 characters long.")
    
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += case_weight
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")
    
    if re.search(r"\d", password):
        score += digit_weight
    else:
        feedback.append("❌ Add at least one number (0-9).")
    
    if re.search(r"[!@#$%^&*]", password):
        score += special_char_weight
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")
    
    return score, feedback

# Function to generate a strong password
def generate_password(length):
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(characters) for _ in range(length))

# Streamlit UI
st.set_page_config(page_title="Password Manager", page_icon="🔐", layout="wide")

# Sidebar Navigation
st.sidebar.title("🔐 Secure Password Manager")
st.sidebar.markdown("Navigate through the sections below:")
section = st.sidebar.radio("Go to:", ["Home", "Password Strength Checker", "Password Generator", "History"])

# Main Content
st.title("🔑 Secure Your Passwords with Ease")
st.markdown("---")

if section == "Home":
    st.subheader("Welcome to the Password Manager!")
    st.write("✔️ Check your password strength")
    st.write("✔️ Generate strong passwords with ease")
    st.write("✔️ Keep track of generated passwords")
    st.write("---")
    st.write("Select an option from the sidebar to get started.")

elif section == "Password Strength Checker":
    st.subheader("🔍 Check Password Strength")
    password = st.text_input("Enter your password:", type="password")
    
    # Toggle button to show/hide password
    if st.toggle("Show Password"):
        if password:
            st.write(f'🔒 Password: {password}')
        else:
            st.warning("⚠️ Please enter a password first.")
    
    if st.button("Check Password Strength"):
        if password:
            score, feedback = check_password_strength(password)
            strength_color = "red" if score < 4 else "orange" if score < 6 else "green"
            st.progress(score / 7)
            st.markdown(f"<p style='color:{strength_color}; font-weight:bold;'>Password Strength: {score}/7</p>", unsafe_allow_html=True)
            
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
            
    

elif section == "Password Generator":
    st.subheader("🔑 Generate a Strong Password")
    password_length = st.slider("Select Password Length:", 8, 20, 12)
    
    if st.button("Generate Strong Password"):
        strong_password = generate_password(password_length)
        st.session_state.password_history.append(strong_password)
        st.text_input("Suggested Strong Password:", strong_password)
        if st.button("Copy to Clipboard"):
            st.toast("Password copied to clipboard!", icon="✅")

elif section == "History":
    st.subheader("📜 Generated Passwords History")
    if st.session_state.password_history:
        for p in reversed(st.session_state.password_history):
            st.write(f"🔹 {p}")
    else:
        st.info("No passwords generated yet.")
    
    if st.button("🗑️ Clear Password History"):
        st.session_state.password_history.clear()
        if st.session_state.password_history == []:
            st.success("Password history cleared successfully!")
    
# Footer
st.markdown("<p style='text-align:center; font-weight:bold;'>Made by Kulsoom Adnan</p>", unsafe_allow_html=True)





# import re
# import random
# import string
# import streamlit as st

# # List of common weak passwords
# COMMON_PASSWORDS = {"password123", "12345678", "qwerty", "123456789", "letmein", "admin"}

# # Function to check password strength
# def check_password_strength(password):
#     score = 0
#     feedback = []
    
#     # Custom scoring weights
#     length_weight = 2
#     case_weight = 1.5
#     digit_weight = 1.5
#     special_char_weight = 2
    
#     # Check for common weak passwords
#     if password in COMMON_PASSWORDS:
#         return 0, ["❌ Your password is too common. Choose a more unique password."]
    
#     # Length Check
#     if len(password) >= 8:
#         score += length_weight
#     else:
#         feedback.append("❌ Password should be at least 8 characters long.")
    
#     # Upper & Lowercase Check
#     if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
#         score += case_weight
#     else:
#         feedback.append("❌ Include both uppercase and lowercase letters.")
    
#     # Digit Check
#     if re.search(r"\d", password):
#         score += digit_weight
#     else:
#         feedback.append("❌ Add at least one number (0-9).")
    
#     # Special Character Check
#     if re.search(r"[!@#$%^&*]", password):
#         score += special_char_weight
#     else:
#         feedback.append("❌ Include at least one special character (!@#$%^&*).")
    
#     return score, feedback

# # Function to generate a strong password
# def generate_password():
#     characters = string.ascii_letters + string.digits + "!@#$%^&*"
#     return ''.join(random.choice(characters) for _ in range(12))

# # Streamlit UI
# st.title("🔐 Password Strength Meter")

# # User input
# password = st.text_input("Enter your password:", type="password")

# if st.button("Check Password Strength"):
#     if password:
#         score, feedback = check_password_strength(password)
        
#         # Display feedback with strength bar
#         st.progress(score / 7, text=f"Password Strength: {score}/7")
        
#         if score >= 6:
#             st.success("✅ Strong Password!")
#         elif score >= 4:
#             st.warning("⚠️ Moderate Password - Consider adding more security features.")
#         else:
#             st.error("❌ Weak Password - Improve it using the suggestions below.")
        
#         for item in feedback:
#             st.write(item)
#     else:
#         st.error("Please enter a password to check.")

# # Password Generator Section
# st.subheader("🔑 Generate a Strong Password")
# if st.button("Generate Strong Password"):
#     strong_password = generate_password()
#     st.text_input("Suggested Strong Password:", strong_password)
# # 