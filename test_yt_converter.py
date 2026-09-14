import unittest

from yt_converter import build_ydl_options


class BuildYdlOptionsTests(unittest.TestCase):
    def test_builds_mp3_options(self) -> None:
        options = build_ydl_options("mp3", "downloads")

        self.assertEqual(options["format"], "bestaudio/best")
        self.assertEqual(options["postprocessors"][0]["key"], "FFmpegExtractAudio")
        self.assertEqual(options["postprocessors"][0]["preferredcodec"], "mp3")
        self.assertTrue(options["outtmpl"].endswith("%(title)s.%(ext)s"))

    def test_builds_mp4_options(self) -> None:
        options = build_ydl_options("mp4", "downloads")

        self.assertIn("bestvideo[ext=mp4]", options["format"])
        self.assertEqual(options["merge_output_format"], "mp4")
        self.assertTrue(options["outtmpl"].endswith("%(title)s.%(ext)s"))

    def test_unsupported_format_raises(self) -> None:
        with self.assertRaises(ValueError):
            build_ydl_options("wav", "downloads")


if __name__ == "__main__":
    unittest.main()
