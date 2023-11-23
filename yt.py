from pytube import YouTube, Stream
import time

link = input("YouTube Link: ")
video = YouTube(link)

print("\nInfo:")
print(f"""
Judul: {video.title}
Penayangan video: {video.views}
Durasi video (detik): {video.length}
Penulis video: {video.author}
Tanggal publikasi: {video.publish_date}
""")
print("\nVideo Download")

video_resolution = video.streams.get_highest_resolution()
time.sleep(1)
print("Donwloading... ")
video_resolution.download('/sdcard/')
print("Download complete!")