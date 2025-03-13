import streamlit as st

# App Title & Description
st.title("Unit Converter App")
st.markdown("### Converts Length, Weight, and Time Instantly")
st.write("Welcome! Select a category, enter a value, and get the converted result in real-time.")

# Category Selection
category = st.selectbox("Choose a Category", ["Length", "Weight", "Time"])

# Conversion Function
def convert_units(category, value, unit):
    if category == "Length":
        if unit == "Kilometers to Miles":
            return value * 0.621371
        elif unit == "Miles to Kilometers":
            return value / 0.621371

    elif category == "Weight":
        if unit == "Kilograms to Pounds":
            return value * 2.20462
        elif unit == "Pounds to Kilograms":
            return value / 2.20462

    elif category == "Time":
        if unit == "Seconds to Minutes":
            return value / 60
        elif unit == "Minutes to Seconds":
            return value * 60
        elif unit == "Minutes to Hours":
            return value / 60
        elif unit == "Hours to Minutes":
            return value * 60
        elif unit == "Hours to Days":
            return value / 24
        elif unit == "Days to Hours":
            return value * 24
    
    return 0  # Default return if no valid unit is selected

# Unit Selection Based on Category
if category == "Length":
    unit = st.selectbox("📏 Select Conversion", ["Kilometers to Miles", "Miles to Kilometers"])
elif category == "Weight":
    unit = st.selectbox("⚖️ Select Conversion", ["Kilograms to Pounds", "Pounds to Kilograms"])
elif category == "Time":
    unit = st.selectbox("⏲️ Select Conversion", ["Seconds to Minutes", "Minutes to Seconds", 
                                                  "Minutes to Hours", "Hours to Minutes",
                                                  "Hours to Days", "Days to Hours"])

# Value Input
value = st.number_input("Enter the value to convert", min_value=0.0, format="%.2f")

# Convert Button & Display Result
if st.button("Convert"):
    result = convert_units(category, value, unit)
    st.success(f"The result is {result:.2f}!")

