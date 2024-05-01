import streamlit as st
from datetime import datetime
import time
from pytz import timezone

# Define the time zones
time_zones = {
    "Athens": "Europe/Athens",
    "Moscow": "Europe/Moscow",
    "New York": "America/New_York",
    "Japan": "Asia/Tokyo",
    "UK": "Europe/London",
    "Atlanta": "America/New_York",
    "Dubai": "Asia/Dubai",
    "Alaska": "America/Anchorage"
}

# Function to get the current time in a specific time zone
def get_current_time(time_zone):
    tz = timezone(time_zone)
    return datetime.now(tz)

# Set page configuration
st.set_page_config(
    page_title="Real-Time World Clock",
    page_icon="⏰",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Streamlit app layout
st.title("Real-Time World Clock")
st.markdown("The Real-Time World Clock App is a simple yet powerful tool that provides users with live updates of the current time across different time zones around the globe. With an intuitive interface, users can effortlessly keep track of time differences between various locations, making it an invaluable resource for individuals, businesses, and travelers alike.")
st.markdown("---")

# Define CSS styles
css = """
<style>
.time-zone {
    border: 2px solid #ccc;
    border-radius: 10px;
    padding: 20px;
    margin: 10px;
    font-size: 20px;
}
</style>
"""

# Display CSS styles
st.markdown(css, unsafe_allow_html=True)

# Create time zone elements with initial time
time_zone_elements = {zone: st.empty() for zone in time_zones.keys()}
for zone, tz in time_zones.items():
    current_time = get_current_time(tz)
    time_zone_elements[zone].markdown(f'<div class="time-zone" id="{zone}"><b>{zone}:</b> {current_time.strftime("%Y-%m-%d %H:%M:%S")}</div>', unsafe_allow_html=True)

# Continuously update the time in each time zone
while True:
    for zone, tz in time_zones.items():
        current_time = get_current_time(tz)
        time_zone_elements[zone].markdown(f'<div class="time-zone" id="{zone}"><b>{zone}:</b> {current_time.strftime("%Y-%m-%d %H:%M:%S")}</div>', unsafe_allow_html=True)
    time.sleep(1)  # Update every second
