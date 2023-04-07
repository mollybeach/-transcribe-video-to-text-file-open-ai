import openai

# Set up OpenAI API key
openai.api_key = "YOUR_API_KEY"

audio_file= open("example_video.mp4", "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file)
print(transcript)
