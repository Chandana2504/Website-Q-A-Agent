import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def crawl_website(start_url, max_pages=50):
    visited = set()
    to_visit = [start_url]
    docs = []

    while to_visit and len(visited) < max_pages:
        url = to_visit.pop(0)
        if url in visited or not url.startswith(start_url):
            continue
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            text = soup.get_text(separator=' ', strip=True)
            docs.append({"url": url, "text": text})
            visited.add(url)

            # Discover internal links
            for a_tag in soup.find_all('a', href=True):
                full_url = urljoin(url, a_tag['href'])
                if full_url.startswith(start_url) and full_url not in visited:
                    to_visit.append(full_url)
        except Exception as e:
            print(f"Error while crawling {url}: {e}")
    return docs