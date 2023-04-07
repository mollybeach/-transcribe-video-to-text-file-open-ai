import openai

audio_file= open("example_video.mp4", "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file)
print(transcript)
