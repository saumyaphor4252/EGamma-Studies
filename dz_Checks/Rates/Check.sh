#!/bin/bash

# Loop through all subdirectories in the current directory
for dir in */; do
    # Count the number of regular files (not directories, not hidden files) in the folder
    file_count=$(find "$dir" -maxdepth 1 -type f | wc -l)
    
    # Check if the file count is exactly 2
    if [ "$file_count" -eq 2 ]; then
        echo "Folder with 2 files: $dir"
    fi
done

