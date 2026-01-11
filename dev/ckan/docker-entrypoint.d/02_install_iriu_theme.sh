#!/bin/bash
set -e

# Install IRIU Theme extension if it exists
THEME_DIR="/srv/app/src_extensions/ckanext-iriu-theme"

if [ -d "$THEME_DIR" ]; then
    echo "Installing IRIU Theme extension..."
    pip3 install -e "$THEME_DIR"
    echo "IRIU Theme extension installed successfully."
else
    echo "IRIU Theme extension directory not found at $THEME_DIR"
    echo "Make sure the extension is mounted correctly in docker-compose."
fi
