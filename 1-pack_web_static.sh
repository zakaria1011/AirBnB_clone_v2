#!/bin/bash
#
# Bash script that generates a .tgz archive from the contents of the web_static
# folder of your AirBnB Clone repo.

# Create the 'versions' folder if it doesn't exist
mkdir -p versions

# Format the current date and time
date_time=$(date +"%Y%m%d%H%M%S")

# Create the archive file name
archive_name="web_static_${date_time}.tgz"

# Compress the contents of the web_static folder
tar -cvzf "versions/${archive_name}" web_static

# Check if the archive was generated successfully
archive_path="versions/${archive_name}"
if [ -e "${archive_path}" ]; then
    echo "${archive_path}"
else
    exit 1
fi

