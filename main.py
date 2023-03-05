from bs4 import BeautifulSoup
from googletrans import Translator
import os

# Path to the folder with HTML files
html_folder_path = "F:/Projects/TestJob0503"

# Create an instance of the Translator class
translator = Translator()

# Iterate over all files in the folder with the ".html" extension
for file_name in os.listdir(html_folder_path):
    if file_name.endswith(".html"):
        # Open the file and create a BeautifulSoup object to parse the HTML code
        with open(os.path.join(html_folder_path, file_name), "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f.read(), "html.parser")
        # Extract text from the <p>, <h1>, <h2>, <h3>, and <h4> tags
        text = "\n".join([tag.text for tag in soup.find_all(["p", "h1", "h2", "h3", "h4"])])
        # Translate the text to Hindi using Google Translate
        translation = translator.translate(text, dest="hi").text
        # Output the translation result for each file in the folder
        print(f"Translation for file {file_name}: {translation}\n")
