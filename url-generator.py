###################################################################
#																  #
# URL List generator - Utility to create a list of URLs with ease #
#											(random params)		  #
###################################################################

# Run this program like
# 		$ python url-generator.py <output_filename> <base_url> <number_of_random_urls>
# Example : 
# 		$ python url-generator.py urls.txt https://api.qrserver.com/v1/create-qr-code/?size=300x300&data= 10

# It will create the required output file with random URLs.

import string
import random
import sys

def random_generator(size=300, chars=string.ascii_lowercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

argv = sys.argv
file_out = open(argv[1], 'w')
#base_url = "https://api.qrserver.com/v1/create-qr-code/?size=300x300&data="
base_url = argv[2]
count = int(argv[3])

print "Output file : " + argv[1] + " created.."

for i in range(0, count):
	file_out.write(base_url + random_generator() + "\n")

print "All operations completed."

file_out.close()