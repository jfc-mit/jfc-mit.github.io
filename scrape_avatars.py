import urllib.request
from bs4 import BeautifulSoup
import os

os.makedirs('/n/home07/anovak/work/jfc-mit.github.io/images', exist_ok=True)

urls = {
    'eric': 'https://www.linkedin.com/in/eric-a-moreno/',
    'sam': 'https://www.linkedin.com/in/sam-bright-thonney-8a5b14b4/',
    'andrzej': 'https://www.linkedin.com/in/andrzejnovak/',
    'dolores': 'https://www.linkedin.com/in/dolores-garcia-500676175/',
    'philip': 'https://physics.mit.edu/faculty/philip-harris/'
}

opener = urllib.request.build_opener()
opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/91.0.4472.124 Safari/537.36')]
urllib.request.install_opener(opener)

for name, url in urls.items():
    try:
        html = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(html, 'html.parser')
        image = soup.find('meta', property='og:image')
        if image and image['content']:
            img_url = image['content']
            print(f"[{name}] Found image: {img_url}")
            img_path = f"/n/home07/anovak/work/jfc-mit.github.io/images/author_{name}.jpg"
            urllib.request.urlretrieve(img_url, img_path)
        else:
            print(f"[{name}] No og:image found.")
            
            # Special fallback for MIT Physics faculty pages
            if name == 'philip':
                img_tag = soup.find('img', class_='attachment-faculty-portrait')
                if img_tag and img_tag.get('src'):
                    print(f"[{name}] Found MIT image: {img_tag['src']}")
                    urllib.request.urlretrieve(img_tag['src'], f"/n/home07/anovak/work/jfc-mit.github.io/images/author_{name}.jpg")
    except Exception as e:
        print(f"[{name}] Error: {e}")
