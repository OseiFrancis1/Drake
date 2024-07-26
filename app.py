import streamlit as st

# Title of the app
st.title("Population Health Metrics")

# Displaying population health metrics
st.write("### Key Population Health Metrics")
st.write("This data comes from St.Kitts and Nevis")

# Metric 1: Average Heart Rate
st.metric(label="Average Heart Rate", value="75 bpm", delta="-2 bpm")

# Metric 2: Average Blood Pressure
st.metric(label="Average Blood Pressure", value="125/85 mmHg", delta="+3/2 mmHg")

# Metric 3: Average Blood Sugar Level
st.metric(label="Average Blood Sugar Level", value="95 mg/dL", delta="+4 mg/dL")

# Metric 4: Average Cholesterol Level
st.metric(label="Average Cholesterol Level", value="200 mg/dL", delta="+5 mg/dL")

# Metric 5: Obesity Rate
st.metric(label="Obesity Rate", value="30%", delta="+1%")

# Metric 6: Smoking Rate
st.metric(label="Smoking Rate", value="20%", delta="-1%")
