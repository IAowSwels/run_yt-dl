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

# Check if youtube-dl is available in directory
if not os.path.exists(youtube_dl_path): 
        download = input('Youtube-dl is missing. Download latest version from Github now? [Y], n: ')
        if download == 'Y' or download == 'y' or download == '':
                # Construct the command
                command = ['wget', '-O', 'youtube-dl', 'https://github.com/ytdl-patched/youtube-dl/releases/latest/download/>
                # Execute the command to download latest release of youtube-dl from official git repo
                subprocess.run(command)

# Prompt the user to enter the URL
video_url = input("Enter the URL of the video you want to download: ")

# Construct the command
command = ['python3', youtube_dl_path] + options + [video_url]

# Execute the command
subprocess.run(command)
