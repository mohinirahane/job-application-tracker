import streamlit as st
import pandas as pd
import os

st.title("Job Application Tracker")

file_name = "applications.csv"

# Create file if not exists
if not os.path.exists(file_name):
    df = pd.DataFrame(columns=["Company", "Role", "Status"])
    df.to_csv(file_name, index=False)

# Input Section
st.header("Add New Application")

company = st.text_input("Company Name")
role = st.text_input("Job Role")

status = st.selectbox(
    "Application Status",
    ["Applied", "Interview", "Selected", "Rejected"]
)

if st.button("Add Application"):

    new_data = pd.DataFrame({
        "Company": [company],
        "Role": [role],
        "Status": [status]
    })

    new_data.to_csv(file_name, mode='a', header=False, index=False)

    st.success("Application Added Successfully!")

# Read Data
df = pd.read_csv(file_name)

# Search
st.header("Search Company")

search = st.text_input("Search by Company Name")

if search:
    filtered_df = df[df["Company"].str.contains(search, case=False)]
    st.dataframe(filtered_df)
else:
    st.dataframe(df)

# Status Filter
st.header("Filter by Status")

filter_status = st.selectbox(
    "Select Status",
    ["All", "Applied", "Interview", "Selected", "Rejected"]
)

if filter_status != "All":
    filtered_status_df = df[df["Status"] == filter_status]
    st.dataframe(filtered_status_df)