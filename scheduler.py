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
    shifts = [
        ("Morning", "08:00", "16:00"),
        ("Afternoon", "14:00", "22:00"),
        ("Night", "22:00", "23:59")  # Ends at 11:59PM to stay within the same day
    ]

    # Generate more dummy shifts per day
    events = []
    for day_offset in range(1, 30):  # Next 30 days
        shift_date = datetime.today() + timedelta(days=day_offset)
        num_shifts = random.randint(3, 6)  # Each day gets 3-6 shifts

        for _ in range(num_shifts):
            doctor = random.choice(staff_members)
            shift_name, start_time, end_time = random.choice(shifts)

            events.append({
                "title": f"{doctor} - {shift_name}",
                "start": f"{shift_date.strftime('%Y-%m-%d')}T{start_time}:00",
                "end": f"{shift_date.strftime('%Y-%m-%d')}T{end_time}:00",
                "backgroundColor": random.choice(["#007bff", "#28a745", "#dc3545"]),  # Blue, Green, Red
                "borderColor": "#ffffff",  # White border for clarity
                "display": "block",  # Ensures full block styling instead of dots
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
            "right": "dayGridMonth,timeGridWeek,timeGridDay"
        },
        "eventDisplay": "block",  # Forces full block styling instead of dots
    }

    # Show the interactive calendar
    selected_event = st_calendar(events=events, options=calendar_options, key=f"calendar-{st.session_state.calendar_view}")

    # **Display Selected Shift Details**
    if selected_event and "eventClick" in selected_event:
        event_data = selected_event["eventClick"]["event"]
        st.success(f"📌 **Shift Selected:** {event_data['title']}")
        st.write(f"📅 **Date:** {event_data['start'][:10]}")
        st.write(f"🕒 **Start Time:** {event_data['start'][11:16]}")
        st.write(f"🕒 **End Time:** {event_data['end'][11:16]}")
        st.write(f"🎨 **Shift Color:** `{event_data['backgroundColor']}`")
