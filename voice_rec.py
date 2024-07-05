import pyaudio
import wave
import os

class VoiceRecorder:
    def __init__(self):
        self.chunk = 1024  # Record in chunks of 1024 samples
        self.sample_format = pyaudio.paInt16  # 16 bits per sample
        self.channels = 2
        self.rate = 44100  # Record at 44100 samples per second
        self.frames = []
        self.p = pyaudio.PyAudio()

    def record(self, duration):
        print("Recording... please wait.")
        stream = self.p.open(format=self.sample_format,
                             channels=self.channels,
                             rate=self.rate,
                             input=True,
                             frames_per_buffer=self.chunk)

        self.frames = [stream.read(self.chunk) for _ in range(int(self.rate / self.chunk * duration))]

        stream.stop_stream()
        stream.close()
        print("Recording completed.")

    def playback(self):
        print("Playing back recording...")
        stream = self.p.open(format=self.sample_format,
                             channels=self.channels,
                             rate=self.rate,
                             output=True)

        for frame in self.frames:
            stream.write(frame)

        stream.stop_stream()
        stream.close()

    def save(self, filename):
        if not filename.endswith('.wav'):
            raise ValueError("Filename must have a .wav extension.")

        with wave.open(filename, 'wb') as wf:
            wf.setnchannels(self.channels)
            wf.setsampwidth(self.p.get_sample_size(self.sample_format))
            wf.setframerate(self.rate)
            wf.writeframes(b''.join(self.frames))
        
        print(f"Saved recording to {filename}")

    def terminate(self):
        self.p.terminate()

def main():
    recorder = VoiceRecorder()
    
    actions = {
        'record': lambda: recorder.record(int(input("Enter duration of recording in seconds: "))),
        'playback': recorder.playback,
        'save': lambda: recorder.save(input("Enter filename to save recording (with .wav extension): ")),
        'exit': lambda: recorder.terminate() or print("Exiting the application.") or exit()
    }

    while True:
        command = input("Enter command (record/playback/save/exit): ").strip().lower()
        action = actions.get(command)
        if action:
            action()
        else:
            print("Invalid command. Please enter 'record', 'playback', 'save', or 'exit'.")

if __name__ == "__main__":
    main()
    