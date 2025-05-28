# 🎙️ Speech-to-Text Transcriber

A simple and effective Python tool that records audio using your microphone and converts it into text using Google's Speech Recognition API.

## 🔧 Features

- 🎤 Records voice input using your system microphone
- 🧠 Converts speech to text with high accuracy
- 🔇 Automatically adjusts to ambient noise
- 📝 Saves the transcript to a timestamped `.txt` file
- 💻 Clean, beginner-friendly terminal interface

## 📦 Requirements

- Python 3.10 or higher
- `speechrecognition`
- `pyaudio`
- (macOS only) `portaudio` via Homebrew:
  ```bash
  brew install portaudio
