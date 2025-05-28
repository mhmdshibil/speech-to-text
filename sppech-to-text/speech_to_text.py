import speech_recognition as sr
from datetime import datetime
import os

def record_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("\n🔊 Adjusting for ambient noise... Please wait.")
        recognizer.adjust_for_ambient_noise(source, duration=5)
        print("🎙️  Ready to record. Please speak clearly...\n")

        try:
            audio = recognizer.listen(source, phrase_time_limit=10)
        except sr.WaitTimeoutError:
            print("⏰ Listening timed out. Please try again.")
            return None

    return audio

def transcribe_audio(audio):
    recognizer = sr.Recognizer()
    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "❌ Could not understand the audio."
    except sr.RequestError:
        return "❌ Could not connect to the speech recognition service."

def save_transcription(text):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"transcript_{timestamp}.txt"
    filepath = os.path.join(os.getcwd(), filename)

    with open(filepath, "w") as f:
        f.write(text)

    print(f"\n💾 Transcription saved to: {filename}")

def main():
    audio = record_speech()
    if audio is None:
        return

    print("🧠 Transcribing...")
    result = transcribe_audio(audio)
    print(f"\n📝 You said: {result}")

    save_transcription(result)

if __name__ == "__main__":
    print("=== Speech to Text Transcription Tool ===")
    main()