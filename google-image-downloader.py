from google_images_download import google_images_download  
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-k", "--keywords", required=True,
	help="The keywords/key phrases you want to search for.")
ap.add_argument("-l", "--limit", required=True,
	help="The number of images that you want to download.")
args = vars(ap.parse_args())

response = google_images_download.googleimagesdownload()
arguments = {"keywords":args["keywords"],"limit":args["limit"],"print_urls":True}  
paths = response.download(arguments)
print(paths) 