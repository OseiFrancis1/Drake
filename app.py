import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from transformers import pipeline

# Initialize chat history
if "history" not in st.session_state:
    st.session_state.history = []

# Initialize the chatbot pipeline
chat_pipeline = pipeline("text-generation", model="gpt2")

# Streamlit app
st.title("Chatbot with CSV Interaction and Data Analysis")

# Create a sidebar for the chat messages
with st.sidebar:
    st.write("Chat History")
    messages = st.container()

# File uploader
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file:
    # Read the CSV file into a DataFrame
    df = pd.read_csv(uploaded_file)

    # Display the DataFrame
    st.write("Data Preview:")
    st.dataframe(df)

    # Plot charts and perform data analysis based on commands
    if not df.empty:
        st.write("Charts and Analysis:")

        # Chat input
        prompt = st.text_input("Say something")

        # Process the input and generate a chatbot response
        if prompt:
            # Display user message
            with messages:
                st.chat_message("user").write(prompt)

            # Append user message to history
            st.session_state.history.append({"role": "user", "content": prompt})

            # Basic command parsing
            response = ""
            if "histogram" in prompt.lower():
                num_cols = df.select_dtypes(include=['number']).columns
                if len(num_cols) > 0:
                    col = num_cols[0]  # Default to first numerical column
                    response = f"Showing histogram for {col}."
                    fig, ax = plt.subplots()
                    sns.histplot(df[col], kde=True, ax=ax)
                    st.pyplot(fig)
                else:
                    response = "No numerical columns found to plot."

            elif "line chart" in prompt.lower():
                num_cols = df.select_dtypes(include=['number']).columns
                if len(num_cols) > 0:
                    col = num_cols[0]  # Default to first numerical column
                    response = f"Showing line chart for {col}."
                    st.line_chart(df[col])
                else:
                    response = "No numerical columns found to plot."

            elif "summary" in prompt.lower():
                response = "Showing data summary."
                st.write(df.describe())

            else:
                response = "I'm not sure how to respond to that. Try asking for a histogram or line chart."

            # Append assistant message to history
            st.session_state.history.append({"role": "assistant", "content": response})

            # Display the assistant response
            with messages:
                st.chat_message("assistant").write(response)

# Display chat history
with messages:
    for msg in st.session_state.history:
        if msg["role"] == "user":
            st.chat_message("user").write(msg["content"])
        else:
            st.chat_message("assistant").write(msg["content"])
