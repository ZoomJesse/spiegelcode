import os
import glob
from moviepy.editor import VideoFileClip, ColorClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from PIL import Image
import numpy as np

def ensure_directory_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Created directory: {directory}")
        return False
    return True

def play_video_with_moviepy(video_path):
    try:
        video = VideoFileClip(video_path)
        video = video.resize(newsize=(1920, 1080))
        video.preview(fps=video.fps, fullscreen=True)
    except Exception as e:
        print(f"Failed to play video: {e}")

def display_black_screen(duration=5):
    # Create a black screen clip of 5 seconds and display it
    black_clip = ColorClip(size=(1920, 1080), color=(0, 0, 0), duration=duration)
    black_clip.preview(fullscreen=True)

def get_video_input():
    return input("Enter the video input (e.g., 'input1') or 'exit' to quit: ")

def main():
    display_black_screen(3)  # Display a black screen for 10 seconds at startup
    while True:
        video_input = get_video_input()
        if video_input.lower() == 'exit':
            break  # Exit the program if 'exit' is entered
        directory = f'videos/{video_input}/'
        if ensure_directory_exists(directory):
            video_files = glob.glob(f'{directory}*.mp4')
            if video_files:
                play_video_with_moviepy(video_files[0])  # Play the first .mp4 file found using moviepy
                display_black_screen(5)  # Display a black screen for 5 seconds after video
            else:
                print(f"No video found in {directory}. Please place an MP4 file in the directory.")
                display_black_screen(5)  # Display a black screen if no video is found
        else:
            # If the directory is newly created, look for a backup video
            backup_video_path = 'videos/backup/backup.mp4'
            if os.path.exists(backup_video_path):
                play_video_with_moviepy(backup_video_path)
                display_black_screen(5)  # Display a black screen after backup video
            else:
                print("No backup video found and no videos in the new directory.")
                display_black_screen(5)  # Display a black screen if no backup is found
    display_black_screen(3)  # Display a black screen for 10 seconds before the program exits

if __name__ == '__main__':
    main()
