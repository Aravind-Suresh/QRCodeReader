#############################################################################
#																			#
# QR Code reader accuracy - Utility to determine accuracy of QR code reader	#
#																			#
# Created by : 													  			#
#		Aravind Suresh (9th Aug 2015)							  			#
#############################################################################

# Run this program like
# 		$ python code-reader.py <input_filename_urls> <image_dir> <number_of_files> <extension>
# Example :
#  		$ python code-reader.py urls.txt images 100 png

# It will verify the accuracy of the qrtools library in python

import qrtools
import sys

qr = qrtools.QR()

argv = sys.argv
file_in = open(argv[1], "r")
root_dir = argv[2]
total = int(argv[3])
ext = argv[4]
count = 0

for i in range(1, total + 1):
	img_path = root_dir + "/" + str(i) + "." + ext
	print "Processing " + img_path
	qr.decode(img_path)
	text_decoded = qr.data
	text_original = file_in.readline().split("=")[2].replace("\n", "")
	if text_original == text_decoded:
		count = count + 1

print "Correct matches : " + str(count) + " out of " + str(total) + " images"
print "Accuracy : " + str(count*100/total) + "%"