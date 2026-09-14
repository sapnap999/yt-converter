import unittest

from yt_converter import BASE_DOWNLOAD_DIR, build_ydl_options, resolve_output_dir


class BuildYdlOptionsTests(unittest.TestCase):
    def test_builds_mp3_options(self) -> None:
        options = build_ydl_options("mp3", "downloads")

        self.assertEqual(options["format"], "bestaudio/best")
        self.assertEqual(options["postprocessors"][0]["key"], "FFmpegExtractAudio")
        self.assertEqual(options["postprocessors"][0]["preferredcodec"], "mp3")
        self.assertEqual(options["postprocessors"][0]["preferredquality"], "320")
        self.assertTrue(options["outtmpl"].endswith("%(title)s.%(ext)s"))

    def test_builds_mp4_options(self) -> None:
        options = build_ydl_options("mp4", "downloads")

        self.assertIn("bestvideo[height>=720][ext=mp4]", options["format"])
        self.assertIn("best[height>=720]", options["format"])
        self.assertEqual(options["merge_output_format"], "mp4")
        self.assertTrue(options["outtmpl"].endswith("%(title)s.%(ext)s"))

    def test_unsupported_format_raises(self) -> None:
        with self.assertRaises(ValueError):
            build_ydl_options("wav", "downloads")


class ResolveOutputDirTests(unittest.TestCase):
    def test_relative_path_stays_inside_base_directory(self) -> None:
        resolved = resolve_output_dir("downloads")
        self.assertEqual(resolved, (BASE_DOWNLOAD_DIR / "downloads").resolve())

    def test_unsafe_characters_are_sanitized(self) -> None:
        resolved = resolve_output_dir("../tmp/new folder")
        self.assertEqual(
            resolved, (BASE_DOWNLOAD_DIR / "tmp_new_folder").resolve()
        )


if __name__ == "__main__":
    unittest.main()
