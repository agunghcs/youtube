from pytube import YouTube
import time

url = input("\nInput The Url For The Video:  ")

video = YouTube(url)

print("\nInfo:")
print("\nVideo Title")
print(video.title)
print("\nVideo view")
print(video.views)
print("\nDurasi video (sec)")
print(video.length)
print("\nVideo Thumbnail Url")
print(video.thumbnail_url)
print("\nVideo Download")

video = video.streams.get_highest_resolution()

video.download()

print("\nVideo Successful Downloaded In The Same Directory As This Script.")
