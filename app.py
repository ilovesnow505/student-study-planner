import streamlit as st
import pandas as pd

from database import (
    create_table,
    add_assignment,
    get_assignments,
    update_status,
    delete_assignment
)


st.set_page_config(
    page_title="Student Study Planner",
    page_icon="📚",
    layout="wide"
)


create_table()


st.title("📚 Student Study Planner & Assignment Tracker")


menu = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Add Assignment",
        "View Assignments",
        "Update Assignment"
    ]
)


# DASHBOARD

if menu == "Dashboard":

    st.header("📊 Study Dashboard")

    assignments = get_assignments()

    if assignments:

        df = pd.DataFrame(
            assignments,
            columns=[
                "ID",
                "Subject",
                "Assignment",
                "Due Date",
                "Priority",
                "Status"
            ]
        )

        total = len(df)

        completed = len(
            df[
                df["Status"] == "Completed"
            ]
        )

        pending = len(
            df[
                df["Status"] == "Pending"
            ]
        )

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Total Assignments",
            total
        )

        col2.metric(
            "Completed",
            completed
        )

        col3.metric(
            "Pending",
            pending
        )

        st.subheader("Assignment Status")

        chart_data = (
            df["Status"]
            .value_counts()
        )

        st.bar_chart(chart_data)

        st.subheader("All Assignments")

        st.dataframe(
            df,
            use_container_width=True
        )

    else:

        st.info(
            "No assignments added yet."
        )


# ADD ASSIGNMENT

elif menu == "Add Assignment":

    st.header("➕ Add Assignment")

    subject = st.text_input(
        "Subject Name"
    )

    assignment = st.text_input(
        "Assignment Name"
    )

    due_date = st.date_input(
        "Due Date"
    )

    priority = st.selectbox(
        "Priority",
        [
            "High",
            "Medium",
            "Low"
        ]
    )

    status = st.selectbox(
        "Status",
        [
            "Pending",
            "In Progress",
            "Completed"
        ]
    )

    if st.button(
        "Add Assignment"
    ):

        if subject and assignment:

            add_assignment(
                subject,
                assignment,
                str(due_date),
                priority,
                status
            )

            st.success(
                "Assignment Added Successfully!"
            )

            st.rerun()

        else:

            st.warning(
                "Please fill all required fields."
            )


# VIEW ASSIGNMENTS

elif menu == "View Assignments":

    st.header("📝 All Assignments")

    assignments = get_assignments()

    if assignments:

        df = pd.DataFrame(
            assignments,
            columns=[
                "ID",
                "Subject",
                "Assignment",
                "Due Date",
                "Priority",
                "Status"
            ]
        )

        st.dataframe(
            df,
            use_container_width=True
        )

    else:

        st.info(
            "No assignments found."
        )


# UPDATE ASSIGNMENT

elif menu == "Update Assignment":

    st.header("✏️ Update Assignment")

    assignments = get_assignments()

    if assignments:

        assignment_dict = {

            f"{row[0]} - {row[2]}": row[0]

            for row in assignments

        }

        selected = st.selectbox(
            "Select Assignment",
            list(
                assignment_dict.keys()
            )
        )

        new_status = st.selectbox(
            "New Status",
            [
                "Pending",
                "In Progress",
                "Completed"
            ]
        )

        if st.button(
            "Update Status"
        ):

            assignment_id = (
                assignment_dict[selected]
            )

            update_status(
                assignment_id,
                new_status
            )

            st.success(
                "Assignment Updated!"
            )

            st.rerun()

        st.subheader(
            "Delete Assignment"
        )

        if st.button(
            "Delete Selected Assignment"
        ):

            assignment_id = (
                assignment_dict[selected]
            )

            delete_assignment(
                assignment_id
            )

            st.success(
                "Assignment Deleted!"
            )

            st.rerun()

    else:

        st.info(
            "No assignments available."
        )