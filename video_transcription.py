import openai

# Set up OpenAI API key
openai.api_key = "YOUR_API_KEY"

# Set Paths
audio_path = "example_video.mp4"
output_path = "output.txt"

# Upload the audio file to OpenAI's transcriptions API
audio_file= open(audio_path, "rb")

# Transcribe File using OpenAI Whisper
transcript = openai.Audio.transcribe("whisper-1", audio_file)

# Check if the transcript contains the 'text' key
if "text" in transcript:
    # Write the transcription to a text file:
    open(output_path, "w").write(transcript["text"])
    print("Transcription written to output.txt")
else :
    print("No transcription found")
