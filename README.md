📈 Short-Form Video Virality Predictor

A Streamlit-based machine learning app that predicts whether a short-form video (TikTok or YouTube Shorts) is likely to be:

Rising

Declining

Seasonal

Stable

The app uses video metadata (views, likes, comments, shares, etc.) to estimate the virality trend.

🚀 Features

URL Analysis: Paste a TikTok or YouTube Shorts link to auto-fetch video statistics.

Manual Input Mode: Enter your own stats if fetching is unavailable.

Trend Prediction: Classifies the video trend as Rising, Declining, Seasonal, or Stable.

Confidence Score: Displays model confidence (if the model supports probabilities).

Debugging Info: Sidebar shows raw model output and aligned features.

🛠️ Requirements

Python 3.9+

Required Python packages (listed in requirements.txt):

streamlit
pandas
numpy
scikit-learn
joblib
yt-dlp           # For YouTube metadata
TikTokApi        # (Optional) For TikTok metadata


⚡ If you only need manual input mode, you can skip yt-dlp and TikTokApi.

📥 Installation & Setup

Clone the repository

git clone https://github.com/yourusername/virality-predictor.git
cd virality-predictor


Create a virtual environment (recommended)

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows


Install dependencies

pip install -r requirements.txt


Add the model files
Place your trained model files in the project root:

virality_model.pkl
training_columns.pkl
label_encoder.pkl   # optional

▶️ Running the App

Run the Streamlit server:

streamlit run app.py


Then open the provided local URL (e.g. http://localhost:8501) in your browser.

💡 Usage

Paste a video URL (TikTok or YouTube Shorts).

The app automatically fetches metadata and predicts the trend.

OR enable Manual Input to enter:

Views, Likes, Comments, Shares, Saves

Completion Rate

Category

Engagement Rate

Click Predict to view:

Predicted trend (Rising / Declining / Seasonal / Stable)

Model confidence (if available)

🔧 Model Training (Optional)

To retrain or update the model:

Prepare a dataset with video metrics and labeled trends.

Train using your ML algorithm of choice (e.g., RandomForest, XGBoost).

Save the model and training columns:

joblib.dump(model, "virality_model.pkl")
joblib.dump(list(X.columns), "training_columns.pkl")
joblib.dump(label_encoder, "label_encoder.pkl")  # if using encoded labels

⚠️ Troubleshooting
Issue	Solution
Prediction always the same	The model might be underfitted or trained on imbalanced data. Retrain with more diverse samples.
yt_dlp errors	Update yt_dlp: pip install --upgrade yt-dlp.
TikTok fetching fails	TikTokApi often needs cookies or may be region-restricted. Use manual input as a fallback.
📜 License

This project is released under the MIT License.
You are free to use, modify, and distribute with attribution.

👨‍💻 Author

David Waihenya
University of Embu – Computer Science
