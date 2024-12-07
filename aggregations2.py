import streamlit as st
import pandas as pd

# Streamlit app title
st.title("YouTube Analytics")

# Google Drive link to the CSV file (Please update this with the actual download link)
file_url = "https://drive.google.com/file/d/1QlD4uL9uvNfWIMl9n8uZSHHtHArco3jk/view?usp=drive_link"

try:
    # Load the data with error handling
    videos = pd.read_csv(
        file_url,
        error_bad_lines=False,  # Skip problematic lines
        delimiter=",",          # Explicitly specify delimiter
        engine="python"         # Use Python engine for flexibility
    )
    st.write("Preview of loaded data:", videos.head())
except Exception as e:
    st.error(f"Error loading the CSV: {e}")
    videos = None

# Proceed only if data is loaded successfully
if videos is not None:
    try:
        # Perform analytics
        view_stats = videos["views"].mean()
        st.write("Average views:", view_stats)
    except KeyError:
        st.error("Required column 'views' is missing.")
    except Exception as e:
        st.error(f"An error occurred during analytics: {e}")
else:
    st.write("No data available to perform analytics.")

# Add additional analytics and visualizations as needed
