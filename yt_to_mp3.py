python
# Install dependencies
!pip install yt-dlp
!apt-get update -y
!apt-get install ffmpeg -y

# Download YouTube audio as MP3
!yt-dlp -x --audio-format mp3 https://www.youtube.com/watch?v=VIDEO_ID

# Download file to local machine
from google.colab import files
import os

for file in os.listdir():
    if file.endswith(".mp3"):
        files.download(file)
