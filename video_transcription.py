import openai
import os
import math
from pydub import AudioSegment

AudioSegment.ffmpeg = "/usr/local/bin/ffmpeg"
AudioSegment.ffprobe = "/usr/local/bin/ffprobe"

# Set up OpenAI API key
openai.api_key = "OPEN_API_KEY_HERE"

# Set Paths
video_path = "videos/example_video.mp4"

# Set the maximum duration for each transcription chunk (in seconds)
max_chunk_duration = 60

# Load the audio file using pydub
# have it look in a folder called audio

audio = AudioSegment.from_file(video_path, format="mp4")


# Calculate the total number of chunks needed
num_chunks = math.ceil(len(audio) / (max_chunk_duration * 1000))

# Initialize an empty list to store the transcriptions
transcriptions = []

# Transcribe each chunk of the audio file 
for i in range(num_chunks):
    # Calculate the start and end times for the chunk
    start_time = i * max_chunk_duration * 1000
    end_time = (i + 1) * max_chunk_duration * 1000

    # Extract the chunk from the audio file
    chunk = audio[start_time:end_time]

    # Export the chunk to a temporary WAV file
    chunk.export("temp.wav", format="wav")

    # Upload the temporary WAV file to OpenAI's transcriptions API
    with open("temp.wav", "rb") as file:
        response = openai.Audio.transcribe("whisper-1", file)
        
    # Create a new file with the name of the input file remove first 6 characters and last 4 characters from video_path add _transcript.txt
    output_path = "./transcriptions" + video_path[6:-4] + "_transcript.txt"
    
    # Check if the response contains the 'text' key
    if "text" in response: 
        # Append the transcription to the list of transcriptions
        transcriptions.append(response["text"])
         # Write the transcription to the output text file:
        open(output_path, "a").write(response["text"])
        print("Transcription written to" + output_path)
    else:
        # If there was an error, append an empty string to the list of transcriptions
        transcriptions.append("")

    # Delete the temporary WAV file
    os.remove("temp.wav")

# Write the transcriptions to the output file
with open(output_path, "w") as file:
    for transcription in transcriptions:
        file.write(transcription + "\n")

print("Transcription complete!")
