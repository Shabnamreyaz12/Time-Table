import streamlit as st

# App title
st.title("Student Daily Schedule Planner")

# Sidebar for input
st.sidebar.header("Input Schedule Details")
name = st.sidebar.text_input("Student Name")
date = st.sidebar.date_input("Select Date")
subjects = st.sidebar.text_area("Enter Subjects (one per line)").split("\n")

# Inputs for time slots
st.sidebar.subheader("Time Slots")
time_slots = st.sidebar.text_area("Enter Time Slots (e.g., 8:00-9:00 AM)").split("\n")

# Display the schedule
st.header(f"Schedule for {name} on {date}")
if len(subjects) == len(time_slots) and subjects and time_slots:
    for time, subject in zip(time_slots, subjects):
        st.write(f"**{time}**: {subject}")
elif not subjects or not time_slots:
    st.warning("Please enter both subjects and time slots.")
else:
    st.warning("The number of subjects and time slots must match.")

# Option to save the schedule
if st.button("Save Schedule"):
    if name and subjects and time_slots:
        schedule_content = f"Schedule for {name} on {date}:\n"
        for time, subject in zip(time_slots, subjects):
            schedule_content += f"{time}: {subject}\n"
        st.success("Schedule saved successfully!")
        st.download_button(
            label="Download Schedule",
            data=schedule_content,
            file_name=f"{name}_schedule_{date}.txt",
            mime="text/plain",
        )
    else:
        st.error("Make sure to fill in all the required details.")
