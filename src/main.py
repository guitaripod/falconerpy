# main.py
import logging
import logging_config
import json
import subprocess
import urllib.request

logging.info("Application started.")

API_KEY = 'YOUR_YOUTUBE_API_KEY'
CHANNEL_ID = 'THE_YOUTUBE_CHANNEL_ID'
VIDEO_DOWNLOAD_PATH = '/path/to/download/'

def get_latest_videos():
    logging.info("Polling YouTube channel for latest videos.")
    url = f'https://www.googleapis.com/youtube/v3/search?key={API_KEY}&channelId={CHANNEL_ID}&order=date&part=snippet'
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    logging.info("Latest videos retrieved successfully.")
    return data

def check_video_title(videos):
    logging.info("Checking for videos with 'Bruce Falconer' in the title.")
    for video in videos['items']:
        if 'Bruce Falconer' in video['snippet']['title']:
            logging.info(f"Found a video with ID: {video['id']['videoId']}")
            return video['id']['videoId']
    logging.info("No video with 'Bruce Falconer' in the title found.")
    return None

def download_video(video_id):
    logging.info(f"Downloading video with ID: {video_id}.")
    command = ['youtube-dl', f'https://www.youtube.com/watch?v={video_id}', '-o', f'{VIDEO_DOWNLOAD_PATH}/%(title)s.%(ext)s']
    subprocess.run(command)
    logging.info("Video downloaded successfully.")

def main():
    videos = get_latest_videos()
    video_id = check_video_title(videos)
    
    if video_id:
        download_video(video_id)

if __name__ == "__main__":
    main()
