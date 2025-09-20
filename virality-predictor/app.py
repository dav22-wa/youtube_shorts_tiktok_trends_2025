import streamlit as st
import joblib
import numpy as np
from yt_dlp import YoutubeDL
from TikTokApi import TikTokApi

# Load your trained model & training columns
model = joblib.load("virality_model.pkl")
training_columns = joblib.load("training_columns.pkl")

# ---- Fetch YouTube Shorts Metadata ----
def fetch_youtube_metadata(url):
    ydl_opts = {"quiet": True, "extract_flat": False}
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)

    return {
        "views": info.get("view_count", 0),
        "likes": info.get("like_count", 0),
        "comments": info.get("comment_count", 0),
        "shares": 0,   # Not available
        "saves": 0,    # Not available
        "completion_rate": 0.7,  # Placeholder
        "category": info.get("categories", ["General"])[0],
        "engagement_rate": (info.get("like_count", 0) + info.get("comment_count", 0)) / max(info.get("view_count", 1), 1),
    }

# ---- Fetch TikTok Metadata ----
def fetch_tiktok_metadata(url):
    with TikTokApi() as api:
        video = api.video(url=url).info()

    stats = video.get("stats", {})
    return {
        "views": stats.get("playCount", 0),
        "likes": stats.get("diggCount", 0),
        "comments": stats.get("commentCount", 0),
        "shares": stats.get("shareCount", 0),
        "saves": stats.get("collectCount", 0),
        "completion_rate": 0.7,  # TikTok doesn’t expose this
        "category": "General",
        "engagement_rate": (stats.get("diggCount", 0) + stats.get("commentCount", 0)) / max(stats.get("playCount", 1), 1),
    }

# ---- Streamlit App ----
st.title("📈 Short-Form Video Virality Predictor")

url = st.text_input("Paste a TikTok or YouTube Shorts link:")

if st.button("Predict"):
    metadata = None
    if "tiktok.com" in url:
        metadata = fetch_tiktok_metadata(url)
    elif "youtube.com" in url or "youtu.be" in url:
        metadata = fetch_youtube_metadata(url)
    else:
        st.error("❌ Please paste a valid TikTok or YouTube Shorts link.")

    if metadata:
        st.write("🔍 Video Stats:", metadata)

        # Convert metadata into model features
        input_data = [metadata.get(col, 0) for col in training_columns]
        input_array = np.array(input_data).reshape(1, -1)

        prediction = model.predict(input_array)[0]
        st.success(f"📊 Predicted Trend: **{prediction}**")
