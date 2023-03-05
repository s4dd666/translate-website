import requests
from bs4 import BeautifulSoup
import os

url = "https://www.classcentral.com/"
depth = 1
output_dir = "venv/classcentral"

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# List of already downloaded pages
downloaded_urls = []

# Function to download a page and save it to a file
def download_page(url, filename):
    response = requests.get(url)
    with open(filename, "wb") as f:
        f.write(response.content)

# Function for recursively copying pages
def copy_page(url, level):
    # Check if we have already downloaded this page
    if url in downloaded_urls:
        return
    downloaded_urls.append(url)
    # Download the page and save it to a file
    filename = os.path.join(output_dir, url[len("https://www.classcentral.com/"):].replace("/", "_") + ".html")
    download_page(url, filename)
    print("Downloaded:", url)
    # If we have reached the maximum depth level, exit the function
    if level == depth:
        return
    # Find links to other pages on the current page and copy them
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    links = soup.find_all("a")
    for link in links:
        href = link.get("href")
        if href.startswith("http"):
            copy_page(href, level+1)
        elif href.startswith("/"):
            copy_page("https://www.classcentral.com" + href, level+1)

# Copy the main page
copy_page(url, 0)
