from pytube import YouTube
from pytubefix import YouTube
from pathlib import Path

#Ask the user to enter YouTube URL
url = input ("Enter YouTube URL: ")

def main():
  yt = YouTube(url)

  print("Video Title: ", yt.title)
  print("Number of Views: ", yt.views)

  #Get the highest resolution stream
  yd = yt.streams.get_highest_resolution()

  #Download the video
  out_dir = Path(r"C:\Users\aksha\Desktop\My projects\YouTube video downloder using python\Download_Videos")
  out_dir.mkdir(parents=True, exist_ok=True)

  try:
    yd.download(output_path=str(out_dir))
    print("Download Completed")
  except Exception as e:
    print("Download Failed:", e)

if __name__ == "__main__":
    main()
