# add the below to yld_opts dict to set the download location
# 'outtmpl': 'somewhere/%(extractor_key)s/%(extractor)s-%(id)s-%(title)s.%(ext)s',

from __future__ import unicode_literals
import youtube_dl
from datetime import datetime
import sys

def my_hook(d):
	if d['status'] == 'finished':
		print('Done downloading, now converting ...')

def main():
	try:
		link = sys.argv[1]
	
		link = link.replace('music', 'www')

		date_time = datetime.now()
		date_time_string = datetime.strftime(date_time, '%Y_%m_%d_%H_%M_%S')

		folder_name_by_date = date_time_string + '_folder'

		ydl_opts = {
			'format': 'bestaudio/best',
			'ffmpeg_location': 'ffmpeg/bin',
			'outtmpl': folder_name_by_date+'/%(title)s.%(ext)s',
			'postprocessors': [{
				'key': 'FFmpegExtractAudio',
				'preferredcodec': 'mp3',
				'preferredquality': '192',
			}],
			'progress_hooks': [my_hook],
		}

		with youtube_dl.YoutubeDL(ydl_opts) as ydl:
			ydl.download([str(link)])

	except Exception as e:
		print("Please enter link!")
		print(f"Please you the format - [python {sys.argv[0]} '<link>']")

if __name__ == '__main__':
	main()