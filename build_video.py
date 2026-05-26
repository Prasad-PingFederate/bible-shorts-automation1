from moviepy.editor import *

clips = []

for i in range(3):

    clip = (
        ImageClip(f"scene{i}.jpg")
        .set_duration(10)
        .resize((1080,1920))
    )

    clips.append(clip)

video = concatenate_videoclips(clips)

audio = AudioFileClip("voice.mp3")

video = video.set_audio(audio)

video.write_videofile(
    "final.mp4",
    fps=24
)