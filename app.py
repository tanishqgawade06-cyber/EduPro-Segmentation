import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="EduPro Analytics", layout="wide")

# Load the segmented data
@st.cache_data
def load_data():
    return pd.read_csv("edupro_segments.csv")

try:
    df = load_data()
except FileNotFoundError:
    st.error("Data not found. Please run pipeline.py first.")
    st.stop()

st.title("🎓 EduPro: Student Segmentation Dashboard")

# Sidebar for filtering
st.sidebar.header("Explore Segments")
selected_segment = st.sidebar.selectbox("Filter by Cluster", df['Assigned_Segment'].unique())
segment_data = df[df['Assigned_Segment'] == selected_segment]

# Top level metrics
col1, col2, col3 = st.columns(3)
col1.metric("Learners in this Cluster", len(segment_data))
col2.metric("Avg Courses Enrolled", round(segment_data['Total_Courses_Enrolled'].mean(), 2))
col3.metric("Avg Spending ($)", round(segment_data['Avg_Spending_Per_Learner'].mean(), 2))

st.divider()

# Charts
c1, c2 = st.columns(2)
with c1:
    fig1 = px.histogram(segment_data, x="Preferred_Category", title="Top Categories in this Cluster")
    st.plotly_chart(fig1, use_container_width=True)
with c2:
    fig2 = px.scatter(segment_data, x="Diversity_Score", y="Learning_Depth_Index", color="Preferred_Level", title="Diversity vs Learning Depth")
    st.plotly_chart(fig2, use_container_width=True)