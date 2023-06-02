#!/usr/bin/python3

import os
import subprocess

def load_options_from_config(config_file):
    with open(config_file, 'r') as f:
        lines = f.readlines()
        options = []
        for line in lines:
            line = line.strip()
            if line and not line.startswith('#'):
                options.append('--'+line)
    return options

# Load options from the config file
config_file = os.path.join(os.getcwd(), 'config')
options = load_options_from_config(config_file)

# Path to youtube-dl.py
youtube_dl_path = os.path.join(os.getcwd(), 'youtube-dl')

# Prompt the user to enter the URL
video_url = input("Enter the URL of the video you want to download: ")

# Construct the command
command = ['python3', youtube_dl_path] + options + [video_url]

# Execute the command
subprocess.run(command)
