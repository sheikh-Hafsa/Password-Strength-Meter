import re
import streamlit as st
#page styling
st.set_page_config(page_title="Password Strength Checker By Hafsa Sheikh", page_icon="🌘", layout="centered")
#custom css
st.markdown("""
<style>
    .main {text-align: center";}
    .stTextInput {width: 60% !important margin: auto; }
    .stButton button {width: 50%; background-color; blue color: white; font-size: 18px; }
    .stButton button:hover {background-color: red; color:white;}
    </style>
    """, unsafe_allow_html=True)

#page tittle and discription
st.title("🔒 Password Strength Generator")
st.write("Enter your Password below to check its security level. 🔍")

#Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1 #increase score by 1
    else:
        feedback.append("❌ Password should be **atleast 8 character long.**")
    
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ **both uppercase (A-Z) and lowercase (a-z) letters**")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Password should include **atleast one number (0-9)**.")

    #special character
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include **at least one special character(!@#$%^&*)**")

    #display password strength letter
    if score == 4:
        st.success("✅ **Strong password** - your password is secure")

    elif score == 3:
        st.info("⚠️**Moderrate Password** - Consider improving security by adding more feature")
    else:
        st.error("**Week Password** - follow the suggestion below to strength it.")

        #feedback
    if feedback:
        with st.expander("🔎**Improve Your Password**"):
            for item in feedback:
                st.write(item)
password = st.text_input("Enter Your Password:", type="password", help="Ensure your password is strong 🔐")

#button working
if st.button("Check Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("⚠️please enter a password first!") #show warning if password empty
