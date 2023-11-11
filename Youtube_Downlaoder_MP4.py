from pytube import YouTube
import os

# where to save
SAVE_PATH = "E:\Youtube_Download_Demo" #to_do

if not os.path.exists(SAVE_PATH):
    os.makedirs(SAVE_PATH)

# link of the video to be downloaded
link="https://youtu.be/hYFzyK9ExuM?si=d3m1JQ9LA4XIaU7d"

yt = YouTube(link)  

try:
    yt.streams.filter(progressive = True, file_extension = "mp4", res="720p").first().download(output_path = SAVE_PATH, 
filename = "oh_sita_video_song.mp4")
    print("Video Downloaded Successfully")
except:
    print("Some Error!")




'''
try:
	# object creation using YouTube
	# which was imported in the beginning
	yt = YouTube(link)
except:
	print("Connection Error") #to handle exception

# filters out all the files with "mp4" extension
mp4files = yt.streams.filter('mp4')

#to set the name of the file
yt.set_filename('Test Video')

# get the video with the extension and
# resolution passed in the get() function
d_video = yt.get(mp4files[-1].extension,mp4files[-1].resolution)
try:
	# downloading the video
	d_video.download(SAVE_PATH)
except:
	print("Some Error!")
print('Task Completed!')
'''