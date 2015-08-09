#############################################################################
#																			#
# File Downloader - Utility to download files from a list of URLs with ease #
#																			#
# Created by : 													  			#
#		Aravind Suresh (8th Aug 2015)							  			#
#############################################################################

# Run this program like
# 		$ ./downloader.sh <file_list_urls> <output_directory> <extension> <file_name_prefix>
# Example : 
# 		$ ./downloader.sh urls.txt images png

# It will download the files from the list of URLs and save it in the output directory with the name and 
# extension you provide.

rm -rf "$2"
filename="$1"
mkdir "$2"
img_suffix="$3"
img_prefix="$4"
ctr=0

wget=/usr/bin/wget
WGET_OPTS="-O"

echo ""
echo "Reading URLs from $filename.."
echo "New directory $2/ created. Dowloading files to $2/ directory.."
echo ""

while read -r line
do
	let "ctr++"
	img_name="$img_prefix"
	img_name="$2/$img_name$ctr.$img_suffix"
    url=$line
    $wget ${WGET_OPTS} ${img_name} ${url}
done < "$filename"

echo ""
echo "All downloads completed"