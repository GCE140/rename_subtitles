# Automatic subtitles renamer

## Table of contents
* [General info](#general-info)
* [How it works](#how-it-works)
* [Technologies](#technologies)

## General info
This script allows you to rename multiple subtitles to made them coincide with the corresponding videos, that's useful to enable the subtitle automatic display when reproducing the video on a compatible media player.

## How it works
First introduce the path of the directory with the videos, the script will list everything in the folder, use that list to detect the media file type, then type the media extension (example: .mkv), you will get a list only cointaining the videos. The process will be repeted with the subtitles and its extension (example: .srt).
After that the program will rename all the subtitles with the name of the corresponding video name but maintaining the subtitle extension.
For expample, if the video is: "Seinfeld.S04E01.The.Trip.1.1080p.AMZN.WEBRip.DD2.0.x264-NTb.mkv" and the original subtitle is: "Seinfeld.S04E01.The.Trip.1.720p.HULU.WEBRip.AAC2.0.H.264-NTb.srt" the new name of the subtitle will be: "Seinfeld.S04E01.The.Trip.1.1080p.AMZN.WEBRip.DD2.0.x264-NTb.srt"

## Technologies
This project has been created with:
* Python 3.9
