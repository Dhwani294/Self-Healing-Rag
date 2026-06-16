from pathlib import Path
from pypdf import PdfReader

def load_pdf(path):

    reader = PdfReader(path)

    text = ""

    for page in reader.pages:
        text += page.extract_text() + "\n"

    return text

def load_txt(path):

    with open(path,"r",encoding="utf-8") as f:
        return f.read()
    

import requests
from bs4 import BeautifulSoup

def load_url(url):

    html = requests.get(
        url,
        timeout=30
    ).text

    soup = BeautifulSoup(
        html,
        "html.parser"
    )

    return soup.get_text()