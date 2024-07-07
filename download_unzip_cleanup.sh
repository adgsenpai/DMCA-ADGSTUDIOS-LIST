#!/bin/bash

# Configuration
ZIP_URL="https://storage.googleapis.com/transparencyreport/google-websearch-copyright-removals.zip"
DOWNLOAD_DIR="."
CSV_DIR="$DOWNLOAD_DIR/google-websearch-copyright-removals"
ZIP_FILE="$DOWNLOAD_DIR/google-websearch-copyright-removals.zip"

# Ensure the download directory exists
mkdir -p $DOWNLOAD_DIR

# Check if the CSV directory exists and remove it if it does
if [ -d "$CSV_DIR" ]; then
    echo "Directory $CSV_DIR already exists. Removing it."
    rm -rf "$CSV_DIR"
fi

# Check if the ZIP file exists and remove it if it does
if [ -f "$ZIP_FILE" ]; then
    echo "ZIP file $ZIP_FILE already exists. Removing it."
    rm "$ZIP_FILE"
fi

# Download the ZIP file
echo "Downloading the ZIP file..."
wget -O "$ZIP_FILE" "$ZIP_URL"

# Unzip the file
echo "Unzipping the file..."
unzip "$ZIP_FILE" -d "$DOWNLOAD_DIR"

# Remove the ZIP file
echo "Cleaning up the ZIP file..."
rm "$ZIP_FILE"

echo "Download, unzip, and cleanup completed successfully."