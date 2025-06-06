import requests
import time
import os
from pytube import YouTube
import yt_dlp

def download_image():
    url = input("Enter the image URL: ")
    filename = input("Enter the name to save the file as (without extension): ")
    try:
        response = requests.get(url)
        response.raise_for_status()
        save_path = os.path.join(os.path.expanduser("~"), "Downloads", f"{filename}.jpeg")
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"Image successfully downloaded to: {save_path}")
    except Exception as e:
        print(f"Failed to download image: {e}")

def download_pdf():
    url = input("Enter the PDF URL: ")
    filename = input("Enter the name to save the file as (without extension): ")
    try:
        response = requests.get(url)
        response.raise_for_status()
        save_path = os.path.join(os.path.expanduser("~"), "Downloads", f"{filename}.pdf")
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"PDF successfully downloaded to: {save_path}")
    except Exception as e:
        print(f"Failed to download PDF: {e}")

def download_youtube_video():
    url = input("Enter the YouTube video URL: ")
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        stream.download(output_path=os.path.join(os.path.expanduser("~"), "Downloads"))
        print("YouTube video successfully downloaded!")
    except Exception as e:
        print(f"Failed to download YouTube video: {e}")

def download_facebook_video():
    url = input("Enter the Facebook video URL: ")
    try:
        options = {
            "outtmpl": os.path.join(os.path.expanduser("~"), "Downloads", "%(title)s.%(ext)s"),
        }
        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([url])
        print("Facebook video successfully downloaded!")
    except Exception as e:
        print(f"Failed to download Facebook video: {e}")

# Main logic
print("Select the option:")
print("1) Download image from the internet")
print("2) Extract PDF from link")
print("3) Download YouTube videos")
print("4) Download videos from Facebook")

try:
    user_input = int(input("Enter the option (1, 2, 3, 4): "))
    print("Loading... Please wait!")
    time.sleep(2)

    if user_input == 1:
        download_image()
    elif user_input == 2:
        download_pdf()
    elif user_input == 3:
        download_youtube_video()
    elif user_input == 4:
        download_facebook_video()
    else:
        print("Invalid option. Please choose between 1 and 4.")

except ValueError:
    print("Please enter a valid number.")
