import re
import streamlit as st

st.set_page_config(page_title="Password Strenght Checker: ", page_icon="🔒",layout="centered")

st.markdown("""
<style>
            .main {text-align: center;}
            .stTextInput {width: 60% !important; margin: auto;}
            .stButton button {width: 50%; background-color #FF69B4; color: white; font-size: 18px;}
            .stButton button:hover { background-color: #FF69B4}
</style>
""", unsafe_allow_html=True)

st.title("Password strength Generator")
st.write("Enter your password below to check its security level.")

def check_password_strenght(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1 
    else:
        feedback.append("Password should be atleast be 8 character long!!")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Password should include both uppercase  [A-Z] & lowercase [a-z]")

    if re.search(r"\d", password):
        score += 1

    else:
        feedback.append("Password should include atleast(0-9) ")

    if re.search(r"[!@#$%^&]", password):
        score += 1
    else:
        feedback.append(" Include at least one special character (!@#$%^&)")

    if score == 4:
        st.success(" ✅ STRONGER PASSWORD - Your password is secure.")
    elif score == 3:
        st.info(" 📢 MODERATE PASSWORD - consider improving security by adding more feature")
    else:
        st.error("❌ WEAK PASSWORD - Follow the suggestion below to strenght it.")

    if feedback:
        with st.expander("Impove Your Password"):
            for item in feedback:
                st.write(item)
password = st.text_input("Enter your password", type="password", help="Ensure your password is strong")

if st.button("Check Strenght"):
    if password:
        check_password_strenght(password)
    else:
        st.warning("Please enter a password first!")

    

