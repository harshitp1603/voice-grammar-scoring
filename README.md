# Voice Grammar Scoring Engine

This project is an AI-based engine that transcribes audio samples (speech) into text and then checks the grammar of the transcribed text. It assigns a grammar score based on the detected issues, helping evaluate the quality of spoken language.

## Features
- **Speech-to-Text**: Converts audio samples (WAV format) into text using Google Speech Recognition API.
- **Grammar Checking**: Analyzes the grammar of the transcribed text using LanguageTool.
- **Grammar Scoring**: Assigns a score based on the number of grammar issues found in the transcribed text.

## Requirements
Before you begin, ensure you have Python 3.x installed on your system. You will also need the following Python packages:

- `speechrecognition`: For converting audio to text.
- `pyaudio`: Required by `speechrecognition` to access the microphone or audio files.
- `spacy`: A natural language processing library.
- `language_tool_python`: A wrapper for LanguageTool, used to check grammar.

### Install Required Libraries
You can easily install the required libraries using the `requirements.txt` file.

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/voice-grammar-scoring.git
   cd voice-grammar-scoring
2. Install the required libraries:

   ```bash
   pip install -r requirements.txt
3. Download the English language model for spaCy (required by the language_tool_python library):

   ```bash
   python -m spacy download en_core_web_sm
#### Setup
Clone the repository: Clone the repository to your local machine to start working with the project.

   ```bash
git clone https://github.com/your-username/voice-grammar-scoring.git
Install dependencies: Install all the required dependencies listed in requirements.txt:

   ```bash
pip install -r requirements.txt
Download spaCy model: Download the necessary language model for spaCy:

   ```bash
python -m spacy download en_core_web_sm
##### Usage

Prepare an audio file: The script expects a WAV audio file. Ensure the file is in a supported format (WAV), or you can modify the script to support other formats if needed.

Modify the audio file path: In the script voice_grammar_scoring.py, replace the audio_file variable with the path to your own audio file. For example:

   ```python
audio_file = "path_to_your_audio_sample.wav"
Run the script: After setting the correct path to the audio file, you can run the script to transcribe the audio and check its grammar:

   ```bash
python voice_grammar_scoring.py
The script will output:

The transcription of the audio.

The grammar score (out of 100).

Any grammar issues detected in the transcribed text (e.g., spelling mistakes, punctuation errors, etc.).

###### Example Output
    ```bash
Transcription: This is a test of the voice transcription system.
Grammar Score: 100/100
If there are grammar issues in the transcribed text, you will see a detailed output like this:

    ```bash
Transcription: This is a test of the voice transcription system.
Grammar Score: 80/100
Issue: Possible spelling mistake found at position 5-6
####### How It Works
Speech-to-Text: The script uses the speech_recognition library and Google's Speech-to-Text API to convert the audio file into text.

Grammar Checking: After transcribing the audio to text, the script uses the language_tool_python library to check for grammar mistakes. LanguageTool is an open-source grammar checker that can detect various types of grammatical errors, such as punctuation issues, spelling mistakes, and sentence structure problems.

Scoring: The script assigns a simple grammar score based on the number of issues detected. It uses a basic scoring mechanism: 100 - (errors * 2), where errors is the total number of grammar issues detected.

######## Project Structure
    ```bash
voice-grammar-scoring/
├── voice_grammar_scoring.py       # Main script for processing audio and checking grammar
├── requirements.txt              # List of required dependencies
├── README.md                     # Project documentation
