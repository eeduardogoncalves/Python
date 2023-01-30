"""
by Eduardo Gonçalves
Consulte - https://www.youtube.com/channel/UCYl0lZjwjafsQyGQ_6xfiKw?sub_confirmation=1
"""

from pytube import YouTube

url = input("Enter the YouTube video URL: ")
yt = YouTube(url)

# Set the video quality (options: 1080p, 720p, etc.)
video = yt.streams.filter(resolution='720p').first()

# Download the video
video.download()

print("Video downloaded successfully!")
