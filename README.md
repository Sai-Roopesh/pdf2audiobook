
# PDF to Audio Conversion Script

This project extracts text from a PDF document, formats it using Google Generative AI, and converts the formatted text into an audio file using Google Cloud Text-to-Speech.

## Prerequisites

- Python 3.x
- `pdfminer.six` library
- `google-cloud-texttospeech` library
- `google-generativeai` library
- `python-dotenv` library
- Google Cloud credentials JSON file

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/pdf-to-audio.git
    cd pdf-to-audio
    ```

2. **Install the necessary libraries**:
    ```bash
    pip install pdfminer.six google-cloud-texttospeech google-generativeai python-dotenv
    ```

3. **Set up Google Cloud**:
    - Obtain a Google Cloud credentials JSON file and place it in a secure location on your machine.
    - Enable the Text-to-Speech API on Google Cloud.

4. **Set up environment variables**:
    - Create a `.env` file in the project directory with the following content:
      ```plaintext
      API_KEY=your_google_generative_ai_api_key
      ```

## Usage

1. **Ensure the environment variables are loaded**:
    ```python
    from dotenv import load_dotenv
    load_dotenv()
    API_KEY = os.getenv("API_KEY")
    ```

2. **Set the environment variable for Google Cloud credentials**:
    ```python
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "/path/to/your/credentials_key.json"
    ```

3. **Extract text from a PDF**:
    ```python
    from pdfminer.high_level import extract_text
    text = extract_text("/path/to/your/pdf_document.pdf")
    ```

4. **Configure the Generative AI API**:
    ```python
    import google.generativeai as genai
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
    ```

5. **Format the text using Generative AI**:
    ```python
    response = model.generate_content(
        "In the Following text remove all the numbers and special characters, make it more readable and give the response in paragraphs, don't give it in points only in paragraphs. Here is text: \n" + text)
    formatted_text = response.text
    ```

6. **Set up the Google Cloud Text-to-Speech client**:
    ```python
    from google.cloud import texttospeech
    client = texttospeech.TextToSpeechClient()
    ```

7. **Convert the formatted text to audio**:
    ```python
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
        out.write(response.audio_content)
        print('Audio content written to file "output.mp3"')
    ```

## Notes

- Ensure that the paths to your PDF document and Google Cloud credentials JSON file are correct.
- Make sure to handle any exceptions and errors as needed to ensure smooth execution of the script.
- You can customize the voice and audio settings by modifying the `VoiceSelectionParams` and `AudioConfig`.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

