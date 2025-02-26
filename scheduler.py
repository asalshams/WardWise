import streamlit as st
import random
from datetime import datetime, timedelta
from streamlit_calendar import calendar as st_calendar

def schedule():
    """ WardWise Interactive Shift Calendar with Real-Time View Switching """
    st.title("📅 WardWise Interactive Shift Calendar")

    # Sidebar for View Options
    st.sidebar.title("📌 Calendar Options")

    # Initialize session state for calendar view
    if "calendar_view" not in st.session_state:
        st.session_state.calendar_view = "dayGridMonth"  # Default to Month View

    # View Selection with Buttons
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("📅 Month View"):
            st.session_state.calendar_view = "dayGridMonth"
            st.rerun()
    with col2:
        if st.button("🗓️ Week View"):
            st.session_state.calendar_view = "timeGridWeek"
            st.rerun()
    with col3:
        if st.button("📆 Day View"):
            st.session_state.calendar_view = "timeGridDay"
            st.rerun()

    # Sample shifts
    staff_members = ["Dr. Smith", "Dr. Patel", "Dr. Chen", "Dr. Ali", "Dr. O'Connor"]
    shifts = ["Morning", "Afternoon", "Night"]

    # Generate dummy event data for doctors' shifts
    events = []
    for _ in range(15):  # Create 15 random shifts
        date = datetime.today() + timedelta(days=random.randint(1, 30))  # Next 30 days
        events.append({
            "title": f"{random.choice(staff_members)} - {random.choice(shifts)}",
            "start": date.strftime("%Y-%m-%dT%H:%M:%S"),
            "end": (date + timedelta(hours=8)).strftime("%Y-%m-%dT%H:%M:%S"),  # 8-hour shift
            "backgroundColor": random.choice(["#007bff", "#28a745", "#dc3545"]),  # Blue, Green, Red
            "borderColor": random.choice(["#007bff", "#28a745", "#dc3545"]),
        })

    # Calendar Configuration (Dynamically Updates View)
    calendar_options = {
        "initialView": st.session_state.calendar_view,
        "editable": True,
        "selectable": True,
        "themeSystem": "standard",
        "headerToolbar": {
            "left": "today prev,next",
            "center": "title",
            "right": "dayGridMonth,timeGridWeek,timeGridDay"  # Buttons for Month, Week, Day
        },
    }

    # Show the interactive calendar
    selected_event = st_calendar(events=events, options=calendar_options, key=f"calendar-{st.session_state.calendar_view}")

    # **Clean Shift Selection Display**
    if selected_event and "eventClick" in selected_event:
        event_data = selected_event["eventClick"]["event"]
        st.success(f"📌 **Shift Selected:** {event_data['title']}")
        st.write(f"📅 **Date:** {event_data['start'][:10]}")
        st.write(f"🕒 **Start Time:** {event_data['start'][11:16]}")
        st.write(f"🕒 **End Time:** {event_data['end'][11:16]}")
        st.write(f"🎨 **Shift Color:** `{event_data['backgroundColor']}`")
