import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
import numpy as np
import os
import subprocess
import shlex
from tqdm import tqdm




def get_all_urls(url):
    # Send a GET request to the URL
    response = requests.get(url)
    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")

    # Extract all anchor tags from the HTML
    anchors = soup.find_all("a")
    
    # Set to store unique URLs
    unique_urls = set()

    # Iterate over the anchor tags
    for anchor in anchors:
        href = anchor.get("href")
        if href and not href.startswith("#"):
            # Normalize and join the URL with the base URL
            full_url = urljoin(url, href)
            # Parse the URL and extract the netloc (domain)
            parsed_url = urlparse(full_url)
            domain = parsed_url.netloc
            # Exclude external URLs and URLs with invalid schemes
            if domain and domain in url:
                unique_urls.add(full_url)

    return unique_urls


def get_pdf_links(url):
    # Send a GET request to the URL
    response = requests.get(url)
    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")

    # Set to store PDF URLs
    pdf_urls = set()

    # Iterate over anchor tags
    for anchor in soup.find_all("a"):
        href = anchor.get("href")
        if href and href.endswith(".pdf"):
            # Normalize and join the URL with the base URL
            full_url = urljoin(url, href)
            pdf_urls.add(full_url)

    return pdf_urls





if __name__ == "__main__":

    url = "https://www.physicsbyfiziks.com/learn_physics/index.php"  # Replace with your desired website URL
    all_urls = get_all_urls(url)
    for suburl in tqdm(all_urls):
        if "learn_physics" in suburl:
            pdf_links = get_pdf_links(suburl)
            # Print all the extracted PDF links
            for link in pdf_links:
                if "learn_physics" in link:
                    command="wget  --no-check-certificate --recursive  --no-parent '%s'"%link
                    try:
                        cmd_result=subprocess.run(shlex.split(command),shell=False,text=True,check=True,capture_output=True) #shell=True : you give full command in double quotes
                        print(cmd_result.stdout) #shell=False give command in list wiht elements in quotss ["wc", "-l"]
                    except:
                        print("Error in ",link)
                    
                    
                    
                    
                    
                    
