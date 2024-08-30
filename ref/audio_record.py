import pyaudio
import numpy as np
import wave
import time
import os

# Parameters for recording
FORMAT = pyaudio.paInt16  # 16-bit resolution
CHANNELS = 1  # 1 channel (mono)
RATE = 44100  # 44.1kHz sampling rate
CHUNK = 1024  # 2^10 samples per frame
THRESHOLD = 8  # Silence threshold for detecting voice start
SILENCE_THRESHOLD = 8  # Silence threshold for stopping recording
SILENCE_LIMIT = 1  # Silence limit in seconds



def main(dir):
# Open a stream with the specified parameters# Initialize PyAudio
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

    # print("Waiting for you to start speaking...")

    # Wait for voice to start
    while True:
        data = stream.read(CHUNK)
        audio_data = np.frombuffer(data, dtype=np.int16)
        volume = np.linalg.norm(audio_data) / CHUNK
        # print(volume, end='\r')

        if volume > THRESHOLD:
            # print("Voice detected, starting recording...")
            print("You: recording...", end='\r')
            break

    # Start recording
    frames = []
    silent_chunks = 0

    while True:
        data = stream.read(CHUNK)
        frames.append(data)

        audio_data = np.frombuffer(data, dtype=np.int16)
        volume = np.linalg.norm(audio_data) / CHUNK

        if volume < SILENCE_THRESHOLD:
            silent_chunks += 1
        else:
            silent_chunks = 0

        if silent_chunks > (SILENCE_LIMIT * RATE / CHUNK):
            # print("Silence detected, stopping recording.")
            break

    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    p.terminate()

    # Save the recorded audio to a file
    timestamp = time.time()
    file_name = f'Records_{timestamp}.mp3'
    full_path = os.path.join(dir, 'records')
    file_path = os.path.join(full_path, file_name)

    wave_file = wave.open(file_path, 'wb')
    wave_file.setnchannels(CHANNELS)
    wave_file.setsampwidth(p.get_sample_size(FORMAT))
    wave_file.setframerate(RATE)
    wave_file.writeframes(b''.join(frames))
    wave_file.close()

    return file_path

