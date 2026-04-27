# 🎵 YouTube to MP3 Downloader (Google Colab)

This project allows you to download audio from a YouTube video as an MP3 file using **yt-dlp** and **ffmpeg** inside Google Colab.

---

## 📌 Features

- Downloads audio from any public YouTube video
- Converts audio to MP3 format
- Automatically downloads the MP3 file to your local machine (via Google Colab)
- Simple and beginner-friendly setup

---

## 🛠 Requirements

This project is designed to run in **Google Colab**.

### Dependencies:

- Python 3
- yt-dlp
- ffmpeg



### How to Use
## Step 1: Install Dependencies
python
!pip install yt-dlp
!apt-get update -y
!apt-get install ffmpeg -y
## Step 2: Download Audio from YouTube
Replace VIDEO_ID with the actual YouTube video ID.

Example:

https://www.youtube.com/watch?v=dQw4w9WgXcQ

!yt-dlp -x --audio-format mp3 https://www.youtube.com/watch?v=VIDEO_ID
This will:

Extract audio from the video
Convert it to MP3
Save it in the current working directory
## Step 3: Download the MP3 File to Your Computer
python
from google.colab import files
import os

# Find and download the first MP3 file in the directory
for file in os.listdir():
    if file.endswith(".mp3"):
        files.download(file)
!apt-get install ffmpeg -y
