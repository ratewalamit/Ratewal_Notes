#!/bin/bash

# Directory to process
DIRECTORY="$1"

# Change to the specified directory
cd "$DIRECTORY" || exit

# Process directories first to avoid conflicts
find . -depth | while read -r item; do
    # Get the base name of the item
    item_name=$(basename "$item")
    
    # Remove spaces and replace brackets with underscores
    new_name=$(echo "$item_name" | sed 's/  */_/g; s#)#_#g; s#(#_#g; s/\[/_/g; s/\]/_/g; s/{/_/g; s/}/_/g')

    # Get the parent directory of the item
    parent_dir=$(dirname "$item")

    # Construct the new path
    new_path="$parent_dir/$new_name"

    # Rename if the name has changed
    if [ "$item" != "$new_path" ]; then
        echo "Renaming: '$item' -> '$new_path'"
        mv "$item" "$new_path"
    fi
done

echo "Renaming completed."

