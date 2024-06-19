# Import necessary libraries
from pdfminer.high_level import extract_text
import google.generativeai as genai
import os
from dotenv import load_dotenv
from google.cloud import texttospeech

# Load environment variables
load_dotenv()
API_KEY = os.getenv("API_KEY")

# Set the environment variable for Google Cloud credentials
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "/Users/sairoopesh/Desktop/pdf2audio/credentials_key.json"

# Extract text from PDF
text = extract_text(
    "/Users/sairoopesh/Desktop/pdf2audio/sairoopesh_resume_2.5.pdf")

# Configure the Generative AI API
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# Format the text using Generative AI
response = model.generate_content(
    "In the Following text remove all the numbers and special characters, make it more readable and give the response in paragraphs, don't give it in points only in paragraphs. Here is text: \n" + text)

formatted_text = response.text

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "/Users/sairoopesh/Documents/pdf-2-audiobook/credentials_key.json"

client = texttospeech.TextToSpeechClient()

synthesis_input = texttospeech.SynthesisInput(text=formatted_text)

voice = texttospeech.VoiceSelectionParams(
    language_code="en-US",
    ssml_gender=texttospeech.SsmlVoiceGender.MALE
)

audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
)

response = client.synthesize_speech(
    input=synthesis_input, voice=voice, audio_config=audio_config
)

with open("output.mp3", "wb") as out:
    # Write the response to the output file.
    out.write(response.audio_content)
    print('Audio content written to file "output.mp3"')
