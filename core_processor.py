import os
import requests
from bs4 import BeautifulSoup

def parse_poetry_file(file_path):
    """File se metadata aur kavita/article ki lines nikalta hai."""
    meta = {}
    poem_lines = []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if '---' in content:
            parts = content.split('---', 1)
            meta_part = parts[0].strip()
            poem_part = parts[1].strip()
        else:
            meta_part = ""
            poem_part = content.strip()

        # Metadata parse karna (TITLE, AUTHOR, etc.)
        for line in meta_part.split('\n'):
            if ':' in line:
                key, val = line.split(':', 1)
                meta[key.strip().upper()] = val.strip()
                
        # Text/Poem ki lines nikalna
        poem_lines = poem_part.split('\n')
        
        return meta, poem_lines
        
    except Exception as e:
        print(f"Error parsing file: {e}")
        return {}, []


def fetch_article_from_url(url):
    """Website link se article fetch karke pipeline format mein badalta hai."""
    try:
        # Website ko request bhejna (headers zaruri hain taaki site block na kare)
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        response = requests.get(url, headers=headers)
        response.raise_for_status() # Check if request was successful
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Heading (h1) nikalna
        title_tag = soup.find('h1')
        title = title_tag.text.strip() if title_tag else "Web Article"
        
        # Paragraphs (p) nikalna
        paragraphs = soup.find_all('p')
        article_text = "\n".join([p.text.strip() for p in paragraphs if p.text.strip()])
        
        # Hamare pipeline format (TITLE, AUTHOR, ---) mein string banana
        formatted_text = f"TITLE: {title}\nAUTHOR: Web Source\n---\n{article_text}"
        return formatted_text
        
    except Exception as e:
        return f"TITLE: Error\nAUTHOR: System\n---\nURL fetch nahi ho paya: {e}"