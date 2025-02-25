import streamlit as st
import pandas as pd
import random
from datetime import datetime, timedelta
from streamlit_calendar import calendar as st_calendar

def schedule():
    """ WardWise Interactive Shift Calendar """
    st.title("📅 WardWise Interactive Shift Calendar")

    # Sample shifts
    staff_members = ["Dr. Smith", "Dr. Patel", "Dr. Chen", "Dr. Ali", "Dr. O'Connor"]
    shifts = ["Morning", "Afternoon", "Night"]

    # Generate dummy event data for doctors' shifts
    events = []
    for i in range(10):  # Create 10 random shifts
        date = datetime.today() + timedelta(days=random.randint(1, 30))  # Next 30 days
        events.append({
            "title": f"{random.choice(staff_members)} - {random.choice(shifts)}",
            "start": date.strftime("%Y-%m-%dT%H:%M:%S"),
            "end": (date + timedelta(hours=8)).strftime("%Y-%m-%dT%H:%M:%S"),  # 8-hour shift
            "backgroundColor": random.choice(["blue", "green", "red"]),
            "borderColor": random.choice(["blue", "green", "red"]),
        })

    # Calendar options
    calendar_options = {
        "initialView": "dayGridMonth",  # Options: timeGridWeek, dayGridMonth, listWeek
        "editable": True,
        "selectable": True,
        "themeSystem": "standard",
    }

    # Show the interactive calendar
    selected_event = st_calendar(events=events, options=calendar_options, key="calendar")

    # **Better Event Display**
    if selected_event and "eventClick" in selected_event:
        event_data = selected_event["eventClick"]["event"]
        st.success(f"📌 **Shift Selected:** {event_data['title']}")
        st.write(f"📅 **Date:** {event_data['start'][:10]}")
        st.write(f"🕒 **Start Time:** {event_data['start'][11:16]}")
        st.write(f"🕒 **End Time:** {event_data['end'][11:16]}")
        st.write(f"🎨 **Shift Color:** `{event_data['backgroundColor']}`")

