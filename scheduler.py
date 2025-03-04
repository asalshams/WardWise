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

    # Sample shifts with proper times & colors
    staff_members = ["Dr. Smith", "Dr. Patel", "Dr. Chen", "Dr. Ali", "Dr. O'Connor"]
    shifts = [
        ("Morning", "08:00", "16:00", "#28a745"),  # 🟢 Green
        ("Afternoon", "14:00", "22:00", "#007bff"),  # 🔵 Blue
        ("Night", "22:00", "23:59", "#dc3545")  # 🔴 Red (Ends at 11:59PM)
    ]

    # Generate shifts per day with correct colors
    events = []
    for day_offset in range(1, 30):  # Next 30 days
        shift_date = datetime.today() + timedelta(days=day_offset)
        num_shifts = random.randint(3, 6)  # Each day gets 3-6 shifts

        for _ in range(num_shifts):
            doctor = random.choice(staff_members)
            shift_name, start_time, end_time, shift_color = random.choice(shifts)

            events.append({
                "title": f"{doctor} - {shift_name}",
                "start": f"{shift_date.strftime('%Y-%m-%d')}T{start_time}:00",
                "end": f"{shift_date.strftime('%Y-%m-%d')}T{end_time}:00",
                "backgroundColor": shift_color,  # Assign correct color
                "borderColor": "#ffffff",  # White border for clarity
                "display": "block",  # Ensures block styling
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

    # **Legend for Shift Colors**
    st.sidebar.markdown("### 🔹 Shift Color Legend")
    st.sidebar.markdown("<span style='color:#28a745; font-weight:bold;'>🟢 Morning (08:00 - 16:00)</span>", unsafe_allow_html=True)
    st.sidebar.markdown("<span style='color:#007bff; font-weight:bold;'>🔵 Afternoon (14:00 - 22:00)</span>", unsafe_allow_html=True)
    st.sidebar.markdown("<span style='color:#dc3545; font-weight:bold;'>🔴 Night (22:00 - 23:59)</span>", unsafe_allow_html=True)
