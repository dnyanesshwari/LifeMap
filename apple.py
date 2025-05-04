import streamlit as st

def check_password():
    def password_entered():
        if st.session_state["password"] == "lifemap123":
            st.session_state["password_correct"] = True
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        st.text_input("Enter Password:", type="password", on_change=password_entered, key="password")
        return False
    elif not st.session_state["password_correct"]:
        st.error("❌ Wrong password")
        return False
    else:
        return True