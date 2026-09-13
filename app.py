import streamlit as st
from PIL import Image
import tempfile
import os
from moviepy.editor import ImageClip, AudioFileClip

st.set_page_config(page_title="AURORAAZAH Studio", page_icon="🌊")
st.title("🌊 AURORAAZAH Studio")
st.write("Upload foto + audio = video ngomong")

photo = st.file_uploader("1. Upload Foto Kamu", type=["jpg","jpeg","png"])
audio = st.file_uploader("2. Upload Audio Kamu", type=["mp3","wav","m4a"])

if st.button("🚀 GENERATE VIDEO NGOMONG"):
    if photo and audio:
        with st.spinner("Lagi bikin video... tunggu 20 detik"):
            # simpan file sementara
            with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as f1:
                f1.write(photo.read())
                photo_path = f1.name
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as f2:
                f2.write(audio.read())
                audio_path = f2.name
            
            # bikin video: foto diam + audio
            try:
                audioclip = AudioFileClip(audio_path)
                imgclip = ImageClip(photo_path, duration=audioclip.duration)
                imgclip = imgclip.set_audio(audioclip)
                
                output_path = "/tmp/result.mp4"
                imgclip.write_videofile(output_path, fps=24, verbose=False, logger=None)
                
                st.success("✅ Jadi bang!")
                st.video(output_path)
                
                with open(output_path, "rb") as f:
                    st.download_button("⬇️ Download Video", f, file_name="auroraazah.mp4")
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Upload foto & audio dulu!")

st.caption("Versi 1 - Foto + Audio. Versi 2 nanti pakai Wav2Lip biar bibir gerak.")
