import streamlit as st



#set the title of the app
st.title("Welcome to My First Stream lit app")

#Add a text input
name= st.text_input("Enter your name:")

#display the name entered by the user
if name:
  st.write(f"Hello, {name}! Welcome to the app.")


# Writing dataframes
data = {
    "Column 1": [1, 2, 3, 4],
    "Column 2": [10, 20, 30, 40]
}
