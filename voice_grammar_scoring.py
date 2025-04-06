import speech_recognition as sr
import language_tool_python

# Initialize recognizer and grammar checker
recognizer = sr.Recognizer()
tool = language_tool_python.LanguageTool('en-US')

# Function to process audio and check grammar
def process_audio(audio_file):
    # Transcribe audio
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)
    
    try:
        # Transcribe speech to text
        text = recognizer.recognize_google(audio)
        print("Transcription: ", text)
        
        # Check grammar
        matches = tool.check(text)
        error_count = len(matches)
        
        # Score grammar based on number of errors
        score = max(0, 100 - (error_count * 2))  # Simple scoring logic
        print(f"Grammar Score: {score}/100")
        
        # Optionally, print grammar issues
        for match in matches:
            print(f"Issue: {match.message} at position {match.offset}-{match.offset + match.errorLength}")
    
    except Exception as e:
        print(f"Error processing audio: {e}")

# Example usage
if __name__ == "__main__":
    audio_file = "path_to_your_audio_sample.wav"  # Replace with the path to your audio file
    process_audio(audio_file)
