import speech_recognition as sr  # Import the speech recognition module
import pyttsx3  # Import the text-to-speech module

# Initialize the speech recognizer
r = sr.Recognizer()

# Function to convert text to speech
def SpeakText(command):
    engine = pyttsx3.init()  # Initialize the text-to-speech engine
    engine.say(command)  # Pass the text to be spoken
    engine.runAndWait()  # Run the speech engine to speak the text

# Infinite loop to keep the program running
while True:
    try:
        with sr.Microphone() as source2:  # Use the microphone for input
            r.adjust_for_ambient_noise(source2, duration=0.2)  # Adjust for background noise
            audio2 = r.listen(source2)  # Listen for user input
            
            # Recognize speech using Google's speech recognition
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()  # Convert recognized text to lowercase
            
            print("Did you say", MyText)  # Display recognized text
            SpeakText(MyText)  # Convert recognized text to speech
    
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))  # Handle API request errors
    except sr.UnknownValueError:
        print("Unknown error occurred")  # Handle unrecognized speech
