import argparse
from pathlib import Path


BASE_DOWNLOAD_DIR = Path.cwd().resolve()


def resolve_output_dir(output_dir: str) -> Path:
    candidate = Path(output_dir).expanduser()
    if not candidate.is_absolute():
        candidate = BASE_DOWNLOAD_DIR / candidate

    resolved = candidate.resolve(strict=False)
    try:
        resolved.relative_to(BASE_DOWNLOAD_DIR)
    except ValueError as exc:
        raise ValueError(
            f"Output directory must stay inside: {BASE_DOWNLOAD_DIR}"
        ) from exc

    return resolved


def build_ydl_options(file_format: str, output_dir: str) -> dict:
    output_template = str(Path(output_dir) / "%(title)s.%(ext)s")
    options = {
        "outtmpl": output_template,
        "noplaylist": True,
    }

    if file_format == "mp3":
        options.update(
            {
                "format": "bestaudio/best",
                "postprocessors": [
                    {
                        "key": "FFmpegExtractAudio",
                        "preferredcodec": "mp3",
                        "preferredquality": "320",
                    }
                ],
            }
        )
    elif file_format == "mp4":
        options.update(
            {
                "format": (
                    "bestvideo[height>=720][ext=mp4]+bestaudio[ext=m4a]/"
                    "bestvideo[height>=720]+bestaudio/best[height>=720]"
                ),
                "merge_output_format": "mp4",
            }
        )
    else:
        raise ValueError(f"Unsupported format: {file_format}")

    return options


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Download a YouTube URL as MP3 or MP4."
    )
    parser.add_argument("url", help="YouTube video URL")
    parser.add_argument(
        "--format",
        choices=("mp3", "mp4"),
        default="mp3",
        help="Output file format (default: mp3)",
    )
    parser.add_argument(
        "--output-dir",
        default="downloads",
        help="Directory where converted files will be saved (default: downloads)",
    )
    return parser.parse_args()


def download(url: str, file_format: str, output_dir: str) -> None:
    from yt_dlp import YoutubeDL

    safe_output_dir = resolve_output_dir(output_dir)
    safe_output_dir.mkdir(parents=True, exist_ok=True)
    ydl_options = build_ydl_options(
        file_format=file_format, output_dir=str(safe_output_dir)
    )

    with YoutubeDL(ydl_options) as ydl:
        ydl.download([url])


def main() -> int:
    args = parse_args()
    download(url=args.url, file_format=args.format, output_dir=args.output_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
