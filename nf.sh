#!/bin/sh

#echo "

#$(cat ./assets/logo.txt)
#$(neofetch --cpu_temp on --disk_percent --disk_subtitle name mount --disable GPU DE WM Resolution Theme Icons --stdout)" > ./assets/content/nf.md
echo "

$(neofetch --cpu_temp on --disk_percent --disk_subtitle name mount --disable Packages GPU DE WM Resolution Theme Icons --stdout)" > ./assets/content/nf.md
