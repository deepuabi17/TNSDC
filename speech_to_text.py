import speech_recognition as sr

# Create a recognizer instance
recognizer = sr.Recognizer()

# Set energy threshold
recognizer.energy_threshold = 4000

# Set timeout
recognizer.pause_threshold = 1

# Define a function to transcribe audio from microphone
def transcribe_audio():
    with sr.Microphone() as source:
        print("Listening...")
        audio_data = recognizer.listen(source, timeout=5)  # Set timeout to 5 seconds
        print("Recognizing...")

        try:
            # Use Google Web Speech API to transcribe audio
            text = recognizer.recognize_google(audio_data)
            print("Transcription:", text)
            # Write the transcribed text to a file
            with open("transcription.txt", "w") as file:
                file.write(text)
                print("Transcription saved to transcription.txt")
        except sr.UnknownValueError:
            print("Sorry, could not understand audio.")
        except sr.RequestError as e:
            print("Error fetching results; {0}".format(e))

# Define a function to start transcription
def start_transcription():
    transcribe_audio()

# Call the function to start transcription
start_transcription()
