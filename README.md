# run_yt-dl
The python script inside enables you to use the standalone youtube-dl file on linux with a custom config. Normal config files relate always to PPA installation of youtube-dl on my system. Since this is outdated I need an alternative.

You can adjust the config if needed. Just consider youtube-dl -h for assistance which options are available.
It's important to enter only full options in config. Means the "output" option is not allowed to shorten to "o".

To run the script:
1. Place the latest youtube-dl release from [here]([url](https://github.com/ytdl-patched/youtube-dl/releases)) in the same directory as the run_yt-dl.py file.
2. Call the file with "python3 run_yt-dl.py" from CLI (add the path to the file, if you are in a different directory)

Now the CLI asks you to enter the URL to download.
