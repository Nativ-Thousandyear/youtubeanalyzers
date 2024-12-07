import streamlit as st
import pandas as pd

# Streamlit app title
st.title("YouTube Analytics")

# Google Drive link to the CSV file (Make sure this is a direct downloadable link)
file_url = "https://drive.google.com/uc?export=download&id=1QlD4uL9uvNfWIMl9n8uZSHHtHArco3jk"

# Function to load data with error handling
def load_data():
    try:
        # Load the data with error handling
        videos = pd.read_csv(
            file_url,
            on_bad_lines="skip",  # Skip problematic lines
            delimiter=",",        # Explicitly specify delimiter
            engine="python"       # Use Python engine for flexibility
        )
        return videos
    except Exception as e:
        st.error(f"Error loading the CSV: {e}")
        return None

# Load dataset
videos = load_data()

# Check if data is loaded
if videos is not None:
    st.write("Preview of loaded data:", videos.head())
    st.write("Columns in the dataset:", videos.columns)  # Debugging line to show columns

    # Check if 'views' column exists
    if "views" not in videos.columns:
        st.error("'views' column is missing from the dataset.")
    else:
        # Proceed with analytics if 'views' column exists
        def calculate_view_statistics(videos):
            avg_views = videos["views"].mean()
            max_views = videos["views"].max()
            min_views = videos["views"].min()
            return {"avgViews": avg_views, "maxViews": max_views, "minViews": min_views}

        def calculate_avg_rating_by_category(videos):
            result = videos.groupby("category")["rate"].mean().reset_index()
            return result.to_dict(orient="records")

        def calculate_total_comments_and_ratings_by_category(videos):
            result = videos.groupby("category")[["comments", "ratings"]].sum().reset_index()
            return result.to_dict(orient="records")

        def calculate_avg_length_by_category(videos):
            result = videos.groupby("category")["length"].mean().reset_index()
            return result.to_dict(orient="records")

        def top_uploader_by_views(videos):
            uploader_views = videos.groupby("uploader")["views"].sum().reset_index()
            top_uploader = uploader_views.loc[uploader_views["views"].idxmax()]
            return top_uploader.to_dict()

        def top_commented_videos(videos):
            sorted_videos = videos.sort_values(by="comments", ascending=False)
            return sorted_videos[["videoID", "uploader", "category", "comments"]].head(5).to_dict(orient="records")

        def most_viewed_videos(videos, top_n=5):
            sorted_videos = videos.sort_values(by="views", ascending=False)
            return sorted_videos[["videoID", "views", "uploader", "category"]].head(top_n).to_dict(orient="records")

        def most_viewed_video_in_each_category(videos):
            result = videos.loc[videos.groupby("category")["views"].idxmax()]
            return result[["category", "videoID", "uploader", "views", "rate", "comments"]].to_dict(orient="records")

        def avg_views_per_video_by_category(videos):
            result = videos.groupby("category")["views"].mean().reset_index()
            return result.to_dict(orient="records")

        # Display View Statistics
        view_stats = calculate_view_statistics(videos)
        st.subheader("View Statistics")
        st.write(view_stats)

        # Display Average Rating by Category
        avg_rating_by_category = calculate_avg_rating_by_category(videos)
        st.subheader("Average Rating by Category")
        st.write(avg_rating_by_category)

        # Display Total Comments and Ratings by Category
        total_comments_and_ratings = calculate_total_comments_and_ratings_by_category(videos)
        st.subheader("Total Comments and Ratings by Category")
        st.write(total_comments_and_ratings)

        # Display Average Length by Category
        avg_length_by_category = calculate_avg_length_by_category(videos)
        st.subheader("Average Video Length by Category")
        st.write(avg_length_by_category)

        # Display Top Uploader by Views
        top_uploader = top_uploader_by_views(videos)
        st.subheader("Top Uploader by Views")
        st.write(top_uploader)

        # Display Top Commented Videos
        top_commented = top_commented_videos(videos)
        st.subheader("Top Commented Videos")
        st.write(top_commented)

        # Display Most Viewed Videos
        most_viewed = most_viewed_videos(videos)
        st.subheader("Most Viewed Videos")
        st.write(most_viewed)

        # Display Most Viewed Videos in Each Category
        most_viewed_in_category = most_viewed_video_in_each_category(videos)
        st.subheader("Most Viewed Video in Each Category")
        st.write(most_viewed_in_category)

        # Display Average Views per Video by Category
        avg_views_by_category = avg_views_per_video_by_category(videos)
        st.subheader("Average Views per Video by Category")
        st.write(avg_views_by_category)

else:
    st.write("No data available to perform analytics.")
