# yt-converter

Small CLI utility to convert/download a YouTube URL as either **MP3** or **MP4**.
- MP3 downloads target high audio quality (320 kbps conversion).
- MP4 downloads target at least 720p with best available audio.

## Setup

```bash
python -m pip install -r requirements.txt
```

> Note: MP3 conversion requires `ffmpeg` to be installed on your system.

## Usage

### Friendly UI (recommended)

```bash
streamlit run /home/runner/work/yt-converter/yt-converter/ui.py
```

This opens a polished local web UI where you can paste a YouTube link, choose MP3/MP4, and download.
For safety, output is always written inside this repository directory using the folder name you enter.

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
