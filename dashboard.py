import streamlit as st
import pandas as pd

from processor import process_complaint


st.set_page_config(
    page_title="AI Complaint Classification Dashboard",
    layout="wide"
)

st.title("AI-Powered Customer Complaint Classification & Routing Engine")

st.markdown(
    """
Enter a customer complaint below.
The AI agent will classify it, assign a priority,
and route it to the correct support team.
"""
)

# Session storage for complaint history
if "complaints_history" not in st.session_state:
    st.session_state.complaints_history = []


complaint = st.text_area(
    "Customer Complaint",
    height=150,
    placeholder="Example: My payment was deducted twice and I have not received a refund."
)

if st.button("Analyze Complaint"):

    if complaint.strip() == "":
        st.warning("Please enter a complaint.")
    else:

        result = process_complaint(complaint)

        st.session_state.complaints_history.append(result)

        st.success("Complaint Processed Successfully")

        st.subheader("Latest Result")

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Category",
            result["category"]
        )

        col2.metric(
            "Priority",
            result["priority"]
        )

        col3.metric(
            "Assigned Team",
            result["team"]
        )


# Show history table
if len(st.session_state.complaints_history) > 0:

    st.subheader("Complaint History")

    df = pd.DataFrame(
        st.session_state.complaints_history
    )

    st.dataframe(
        df,
        use_container_width=True
    )

    st.subheader("Complaint Statistics")

    total_complaints = len(df)

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Total Complaints",
        total_complaints
    )

    col2.metric(
        "Critical",
        len(df[df["priority"] == "Critical"])
    )

    col3.metric(
        "High",
        len(df[df["priority"] == "High"])
    )

    col4.metric(
        "Medium",
        len(df[df["priority"] == "Medium"])
    )

    st.subheader("Category Distribution")

    st.bar_chart(
        df["category"].value_counts()
    )

    st.subheader("Priority Distribution")

    st.bar_chart(
        df["priority"].value_counts()
    )

    st.subheader("Team Distribution")

    st.bar_chart(
        df["team"].value_counts()
    )

    csv = df.to_csv(index=False)

    st.download_button(
        label="Download Results CSV",
        data=csv,
        file_name="complaint_results.csv",
        mime="text/csv"
    )