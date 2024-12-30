import os
import uuid
from PIL import Image
import pytesseract
import boto3
from config import IMAGEDIR,PDFDIR,AUDIODIR,REGION,AWS_SECRET_ACCESS_KEY,AWS_ACCESS_KEY_ID,REGION


# Initialize Polly client
polly =boto3.client("polly",
                    region_name=REGION,
                    aws_access_key_id=AWS_ACCESS_KEY_ID,
                    aws_secret_access_key=AWS_SECRET_ACCESS_KEY)


def image_to_text(path: str, image_name: str) -> str:
    """
    Extract text from an image using pytesseract.
    Args:
        path (str): Directory path of the image.
        image_name (str): Name of the image file.

    Returns:
        str: Extracted text from the image.
    """
    try:
        # Path to the image file
        image_path = os.path.join(path, image_name)

        # Read the image using PIL
        image = Image.open(image_path)

        # Extract text from the image
        text = pytesseract.image_to_string(image)

        return text
    except Exception as e:
        return f"Error processing image: {e}"
    
    
    
def text_to_audio(voice:str,text: str,audio_id:str) -> str:
    """
    Convert text to speech using AWS Polly.
    Args:
        text (str): Text to be converted to speech.

    Returns:
        str: Path to the saved audio file.
    """
    try:
        response = polly.synthesize_speech(
            Text=text,
            VoiceId=voice,  # You can change the voice here
            OutputFormat="mp3"
        )

        # Save the audio file
         # Generate a unique filename
        unique_audiofile = f"{audio_id}.mp3"


        
        audio_file_path = os.path.join(AUDIODIR,unique_audiofile)
        with open(audio_file_path, "wb") as file:
            file.write(response["AudioStream"].read())

        print("Audio file saved to", audio_file_path)
        path_for_html=f"/audios/{unique_audiofile}"
        return path_for_html

    except Exception as e:
        return f"Error generating audio: {e}"