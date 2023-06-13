import os
from pytube import Playlist, YouTube

# Specify the playlist URL and directory to save the videos
playlist_url = 'https://www.youtube.com/playlist?list=PLhiFu-f80eo8dnOxALGCclPan-QdUa0Ob'
save_directory = 'D:\ASP.net Core'

# Create the save directory if it does not exist
if not os.path.exists(save_directory):
    os.makedirs(save_directory)

# Create a Playlist object and fetch the videos
playlist = Playlist(playlist_url)

# Download each video in the playlist and save it to the specified directory
for video_url in playlist.video_urls:
    video = YouTube(video_url)
    video.streams.get_highest_resolution().download(output_path=save_directory)
   
    # Download the video
    print('Downloading:', video.title)
print('All videos downloaded successfully.')





# from pytube import YouTube
# import os

# # URL of the YouTube video to download
# urls = ["https://www.youtube.com/watch?v=FuW5NMj3jB0&list=PLtGOJcWqvbqcpzGeMPJXvw7pomKePcfi-&index=52&ab_channel=MahmoudAhmed-%D9%85%D8%AD%D9%85%D9%88%D8%AF%D8%A3%D8%AD%D9%85%D8%AF"
#                ,"https://www.youtube.com/watch?v=8MWZL72fB30&list=PLtGOJcWqvbqcpzGeMPJXvw7pomKePcfi-&index=53&ab_channel=MahmoudAhmed-%D9%85%D8%AD%D9%85%D9%88%D8%AF%D8%A3%D8%AD%D9%85%D8%AF"
#                ,"https://www.youtube.com/watch?v=Ybj0G3-fxyw&list=PLtGOJcWqvbqcpzGeMPJXvw7pomKePcfi-&index=54&ab_channel=MahmoudAhmed-%D9%85%D8%AD%D9%85%D9%88%D8%AF%D8%A3%D8%AD%D9%85%D8%AF"
#                ,"https://www.youtube.com/watch?v=iR3U7Lpq9Z0&list=PLtGOJcWqvbqcpzGeMPJXvw7pomKePcfi-&index=55&ab_channel=MahmoudAhmed-%D9%85%D8%AD%D9%85%D9%88%D8%AF%D8%A3%D8%AD%D9%85%D8%AF"
#                ,"https://www.youtube.com/watch?v=l33f3BcZSPo&list=PLtGOJcWqvbqcpzGeMPJXvw7pomKePcfi-&index=56&ab_channel=MahmoudAhmed-%D9%85%D8%AD%D9%85%D9%88%D8%AF%D8%A3%D8%AD%D9%85%D8%AF","https://www.youtube.com/watch?v=STcCX6s2T38&list=PLtGOJcWqvbqcpzGeMPJXvw7pomKePcfi-&index=57&ab_channel=MahmoudAhmed-%D9%85%D8%AD%D9%85%D9%88%D8%AF%D8%A3%D8%AD%D9%85%D8%AF"
#                ]
# # Set the directory to save the downloaded videos
# save_path = 'D:\\python course\\full qt5'

# # Create the directory if it doesn't exist
# if not os.path.exists(save_path):
#     os.makedirs(save_path)

# # Loop through the list of URLs and download each video
# for url in urls:
#     try:
#         # Create a YouTube object
#         yt = YouTube(url)

#         # Get the first stream with the highest resolution
#         stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()

#         # Download the video
#         print('Downloading:', yt.title)
#         stream.download(output_path=save_path)

#     except Exception as e:
#         print('Error:', str(e))

# print('All videos downloaded successfully!')
