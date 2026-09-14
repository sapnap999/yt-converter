from pathlib import Path

import streamlit as st

from yt_converter import download


st.set_page_config(page_title="YT Converter", page_icon="🎵", layout="centered")

st.markdown(
    """
    <style>
      .stApp {
        background: radial-gradient(circle at 20% 20%, #3b82f6 0%, #111827 42%, #020617 100%);
      }
      .title {
        text-align: center;
        font-size: 2.2rem;
        font-weight: 800;
        color: #f8fafc;
        margin-bottom: 0.25rem;
      }
      .subtitle {
        text-align: center;
        color: #cbd5e1;
        margin-bottom: 1.5rem;
      }
      .glass-card {
        background: rgba(15, 23, 42, 0.65);
        border: 1px solid rgba(148, 163, 184, 0.25);
        border-radius: 16px;
        padding: 1rem;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="title">🎬 YT Converter</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Download YouTube videos as high-quality MP3 or 720p+ MP4.</div>',
    unsafe_allow_html=True,
)

st.markdown('<div class="glass-card">', unsafe_allow_html=True)
url = st.text_input("YouTube URL", placeholder="https://www.youtube.com/watch?v=...")
file_format = st.selectbox("Format", options=("mp3", "mp4"), index=0)
output_dir = st.text_input("Output folder", value="downloads")

download_clicked = st.button("⬇️ Convert & Download", type="primary", use_container_width=True)

if download_clicked:
    if not url.strip():
        st.error("Please enter a valid YouTube URL.")
    else:
        target = Path(output_dir)
        with st.spinner("Downloading and converting..."):
            try:
                download(url=url.strip(), file_format=file_format, output_dir=str(target))
                st.success(f"Done! Saved into: {target.resolve()}")
                files = sorted(target.glob("*"))
                if files:
                    st.write("Recent files:")
                    for item in files[-10:]:
                        st.write(f"- {item.name}")
            except Exception as exc:  # pragma: no cover - UI runtime path
                st.error(f"Download failed: {exc}")

st.markdown("</div>", unsafe_allow_html=True)
