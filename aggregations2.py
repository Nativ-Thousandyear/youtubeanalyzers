import streamlit as st
import pymongo
from pymongo import MongoClient

# MongoDB connection setup (replace with your connection string if necessary)
client = MongoClient("mongodb://localhost:27017")
db = client["youtubeDB"]
collection = db["videos"]

# Aggregation functions
def calculate_view_statistics(collection):
    result = collection.aggregate([
        {"$group": {
            "_id": None,
            "avgViews": {"$avg": "$views"},
            "maxViews": {"$max": "$views"},
            "minViews": {"$min": "$views"}
        }}
    ])
    return list(result)

def calculate_avg_rating_by_category(collection):
    result = collection.aggregate([
        {"$group": {
            "_id": "$category",
            "avgRating": {"$avg": {"$ifNull": ["$rate", 0]}}  # Default to 0 if missing
        }}
    ])
    return list(result)

def calculate_total_comments_and_ratings_by_category(collection):
    result = collection.aggregate([
        {"$group": {
            "_id": "$category",
            "totalComments": {"$sum": "$comments"},
            "totalRatings": {"$sum": "$ratings"}
        }}
    ])
    return list(result)

def calculate_avg_length_by_category(collection):
    result = collection.aggregate([
        {"$group": {
            "_id": "$category",
            "avgLength": {"$avg": "$length"}
        }}
    ])
    return list(result)

def top_uploader_by_views(collection):
    result = collection.aggregate([
        {"$group": {
            "_id": "$uploader",
            "totalViews": {"$sum": "$views"}
        }},
        {"$sort": {"totalViews": -1}},
        {"$limit": 1}
    ])
    return list(result)

def top_commented_videos(collection):
    result = collection.aggregate([
        {"$sort": {"comments": -1}},
        {"$limit": 5},
        {"$project": {"videoID": 1, "uploader": 1, "category": 1, "comments": 1}}
    ])
    return list(result)

def most_viewed_videos(collection, top_n=5):
    result = collection.aggregate([
        {"$sort": {"views": -1}},
        {"$limit": top_n},
        {"$project": {"videoID": 1, "views": 1, "uploader": 1, "category": 1}}
    ])
    return list(result)

def most_viewed_video_in_each_category(collection):
    result = collection.aggregate([
        {"$sort": {"views": -1}},
        {"$group": {
            "_id": "$category",       
            "videoID": {"$first": "$videoID"},
            "uploader": {"$first": "$uploader"},
            "views": {"$first": "$views"},
            "rate": {"$first": "$rate"},
            "comments": {"$first": "$comments"}
        }}
    ])
    return list(result)

def avg_views_per_video_by_category(collection):
    result = collection.aggregate([
        {"$group": {
            "_id": "$category",
            "avgViews": {"$avg": "$views"}
        }}
    ])
    return list(result)

# Streamlit UI setup
st.title("YouTube Analytics")

# Display View Statistics
view_stats = calculate_view_statistics(collection)
st.subheader("View Statistics")
st.write(view_stats)

# Display Average Rating by Category
avg_rating_by_category = calculate_avg_rating_by_category(collection)
st.subheader("Average Rating by Category")
st.write(avg_rating_by_category)

# Display Total Comments and Ratings by Category
total_comments_and_ratings = calculate_total_comments_and_ratings_by_category(collection)
st.subheader("Total Comments and Ratings by Category")
st.write(total_comments_and_ratings)

# Display Average Length by Category
avg_length_by_category = calculate_avg_length_by_category(collection)
st.subheader("Average Video Length by Category")
st.write(avg_length_by_category)

# Display Top Uploader by Views
top_uploader = top_uploader_by_views(collection)
st.subheader("Top Uploader by Views")
st.write(top_uploader)

# Display Top Commented Videos
top_commented = top_commented_videos(collection)
st.subheader("Top Commented Videos")
st.write(top_commented)

# Display Most Viewed Videos
most_viewed = most_viewed_videos(collection)
st.subheader("Most Viewed Videos")
st.write(most_viewed)

# Display Most Viewed Videos in Each Category
most_viewed_in_category = most_viewed_video_in_each_category(collection)
st.subheader("Most Viewed Video in Each Category")
st.write(most_viewed_in_category)

# Display Average Views per Video by Category
avg_views_by_category = avg_views_per_video_by_category(collection)
st.subheader("Average Views per Video by Category")
st.write(avg_views_by_category)
