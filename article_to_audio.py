import sys
import requests
from newspaper import Article
from gtts import gTTS
from pydub import AudioSegment
import nltk

nltk.download('punkt')

def extract_text_from_url(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        article.nlp()  # Perform NLP analysis of article
        return article.summary  # Return summarized article
    except Exception as e:
        print("Error:", e)
        return None

def text_to_audio(text, output_filename):
    try:
        tts = gTTS(text, lang="en")
        tts.save(f"{output_filename}.mp3")
        print(f"Audio saved as {output_filename}.mp3")
    except Exception as e:
        print("Error:", e)

def main():
    if len(sys.argv) < 2:
        print("Usage: python article_to_audio.py <url> [<output_filename>]")
        sys.exit(1)

    url = sys.argv[1]
    output_filename = sys.argv[2] if len(sys.argv) > 2 else "article_audio"

    text = extract_text_from_url(url)
    if text:
        text_to_audio(text, output_filename)

if __name__ == "__main__":
    main()