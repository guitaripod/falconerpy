"""
Main script for polling YouTube for videos and downloading them.
"""

import json
import subprocess
import urllib.request
import logging

API_KEY = 'YOUR_YOUTUBE_API_KEY'
CHANNEL_ID = 'THE_YOUTUBE_CHANNEL_ID'
VIDEO_DOWNLOAD_PATH = '/path/to/download/'

logging.info("Application started.")

def get_latest_videos():
    """Poll YouTube channel for latest videos."""
    logging.info("Polling YouTube channel for latest videos.")
    url = (
        f'https://www.googleapis.com/youtube/v3/search?'
        f'key={API_KEY}&channelId={CHANNEL_ID}&order=date&part=snippet'
    )
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read())
    logging.info("Latest videos retrieved successfully.")
    return data

def check_video_title(videos):
    """Check for videos with 'Bruce Falconer' in title."""
    logging.info("Checking for videos with 'Bruce Falconer' in the title.")
    for video in videos['items']:
        if 'Bruce Falconer' in video['snippet']['title']:
            logging.info("Found a video with ID: %s", video['id']['videoId'])
            return video['id']['videoId']
    logging.info("No video with 'Bruce Falconer' in title found.")
    return None

def download_video(video_id):
    """Download YouTube video by ID."""
    logging.info("Downloading video with ID: %s", video_id)
    command = [
        'youtube-dl',
        f'https://www.youtube.com/watch?v={video_id}',
        '-o',
        f'{VIDEO_DOWNLOAD_PATH}/%(title)s.%(ext)s'
    ]
    subprocess.run(command, check=True)
    logging.info("Video downloaded successfully.")

def main():
    """Main function to run script."""
    videos = get_latest_videos()
    video_id = check_video_title(videos)
    if video_id:
        download_video(video_id)

if __name__ == "__main__":
    main()
