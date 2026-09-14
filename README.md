# yt-converter

Small CLI utility to convert/download a YouTube URL as either **MP3** or **MP4**.

## Setup

```bash
python -m pip install -r requirements.txt
```

> Note: MP3 conversion requires `ffmpeg` to be installed on your system.

## Usage

Download as MP3:

```bash
python /home/runner/work/yt-converter/yt-converter/yt_converter.py "https://www.youtube.com/watch?v=VIDEO_ID" --format mp3
```

Download as MP4:

```bash
python /home/runner/work/yt-converter/yt-converter/yt_converter.py "https://www.youtube.com/watch?v=VIDEO_ID" --format mp4
```

Choose output directory:

```bash
python /home/runner/work/yt-converter/yt-converter/yt_converter.py "https://www.youtube.com/watch?v=VIDEO_ID" --format mp3 --output-dir /path/to/downloads
```
