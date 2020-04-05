#!/bin/sh

# randacek.dev - my personal webserver software
# Copyright (C) 2020  Prokop Randáček
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

#echo "

#$(cat ./assets/logo.txt)
#$(neofetch --cpu_temp on --disk_percent --disk_subtitle name mount --disable GPU DE WM Resolution Theme Icons --stdout)" > ./assets/content/nf.md
echo "

$(neofetch --cpu_temp on --disk_percent --disk_subtitle name mount --disable Packages GPU DE WM Resolution Theme Icons --stdout)" > ./assets/content/nf.md
