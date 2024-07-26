import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Generate sample data
np.random.seed(42)
data = {
    'Category': np.random.choice(['A', 'B', 'C', 'D'], size=100),
    'Value': np.random.randn(100),
    'Age': np.random.randint(18, 70, size=100),
    'Gender': np.random.choice(['Male', 'Female'], size=100)
}
df = pd.DataFrame(data)

# Streamlit app
st.title("Streamlit App with Tabs")

# Create tabs
tabs = st.tabs(["Data Overview", "Visualization 1", "Visualization 2"])

# Tab 1: Data Overview
with tabs[0]:
    st.header("Data Overview")
    st.write("### Raw Data")
    st.write(df.head())
    st.write("### Summary Statistics")
    st.write(df.describe())

# Tab 2: Visualization 1
with tabs[1]:
    st.header("Visualization 1: Value Distribution by Category")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(df, x='Value', hue='Category', multiple='stack', ax=ax, palette='viridis')
    ax.set_title('Value Distribution by Category')
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    st.pyplot(fig)

# Tab 3: Visualization 2
with tabs[2]:
    st.header("Visualization 2: Age Distribution by Gender")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(df, x='Age', hue='Gender', multiple='stack', ax=ax, palette='magma')
    ax.set_title('Age Distribution by Gender')
    ax.set_xlabel('Age')
    ax.set_ylabel('Frequency')
    st.pyplot(fig)
