#!/bin/bash
# Installation script for Time Reminder App

set -e

echo "=========================================="
echo "Time Reminder App - Installation"
echo "=========================================="
echo ""

# Check Python version
echo "Checking Python version..."
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "Found Python $python_version"

# Install dependencies
echo ""
echo "Installing Python dependencies..."
pip3 install -r requirements.txt

# Create config if it doesn't exist
if [ ! -f "config.yaml" ]; then
    echo ""
    echo "Creating config.yaml from example..."
    cp config.example.yaml config.yaml
    echo "⚠️  Please edit config.yaml to set your speaker name!"
fi

# List devices
echo ""
echo "Discovering Google Home devices..."
python3 time_reminder.py --list-devices

echo ""
echo "=========================================="
echo "Installation complete!"
echo "=========================================="
echo ""
echo "Next steps:"
echo "1. Edit config.yaml and set your speaker name"
echo "2. Test the connection: python3 time_reminder.py --test"
echo "3. Run the app: python3 time_reminder.py"
echo ""
echo "For more information, see README.md"
