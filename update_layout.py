import re
import urllib.request
import os

os.chdir('/n/home07/anovak/work/jfc-mit.github.io')

html_insertion = """            <div class="author-profiles animate delay-1">
                <div class="author-card">
                    <img src="images/author_eric.jpg" class="author-image" onerror="this.src='images/placeholder_thumb.png'" alt="Eric A. Moreno">
                    <a href="https://www.linkedin.com/in/eric-a-moreno/" class="author-name" target="_blank">Eric A. Moreno</a>
                    <div class="author-title">PhD Researcher<br>MIT / CERN</div>
                </div>
                <div class="author-card">
                    <img src="images/author_sam.jpg" class="author-image" onerror="this.src='images/placeholder_thumb.png'" alt="Samuel Bright-Thonney">
                    <a href="https://www.linkedin.com/in/sam-bright-thonney-8a5b14b4/" class="author-name" target="_blank">Samuel Bright-Thonney</a>
                    <div class="author-title">IAIFI Fellow<br>MIT / IAIFI</div>
                </div>
                <div class="author-card">
                    <img src="images/author_andrzej.jpg" class="author-image" onerror="this.src='images/placeholder_thumb.png'" alt="Andrzej Novak">
                    <a href="https://www.linkedin.com/in/andrzejnovak/" class="author-name" target="_blank">Andrzej Novak</a>
                    <div class="author-title">Researcher<br>MIT / IAIFI</div>
                </div>
                <div class="author-card">
                    <img src="images/author_dolores.jpg" class="author-image" onerror="this.src='images/placeholder_thumb.png'" alt="Dolores Garcia">
                    <a href="https://www.linkedin.com/in/dolores-garcia-500676175/" class="author-name" target="_blank">Dolores Garcia</a>
                    <div class="author-title">Senior Fellow<br>CERN</div>
                </div>
                <div class="author-card">
                    <img src="images/author_philip.jpg" class="author-image" onerror="this.src='images/placeholder_thumb.png'" alt="Philip Harris">
                    <a href="https://physics.mit.edu/faculty/philip-harris/" class="author-name" target="_blank">Philip Harris</a>
                    <div class="author-title">Associate Professor<br>MIT</div>
                </div>
            </div>"""

css_insertion = """
/* AUTHOR PROFILES */
.author-profiles {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 2.5rem;
    margin: 3rem 0;
}
.author-card {
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    max-width: 160px;
}
.author-image {
    width: 100px;
    height: 100px;
    border-radius: 50%;
    object-fit: cover;
    border: 3px solid var(--accent-blue);
    margin-bottom: 1rem;
    box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    transition: transform 0.3s ease;
}
.author-card:hover .author-image {
    transform: scale(1.05);
}
.author-name {
    font-family: 'Merriweather', serif;
    font-size: 1.05rem;
    font-weight: 700;
    color: var(--text-color);
    margin-bottom: 0.25rem;
    text-decoration: none;
}
.author-name:hover {
    color: var(--accent-blue);
}
.author-title {
    font-family: 'Inter', sans-serif;
    font-size: 0.70rem;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: 0.05em;
    font-weight: 600;
    line-height: 1.4;
}

@media (max-width: 768px) {
    .author-profiles {
        gap: 1.5rem;
    }
}
"""

with open("index.html", "r") as f:
    content = f.read()

# Replace the authors AND institutions block securely
content = re.sub(r'<div class="authors animate delay-1">.*?<p class="animate delay-2">', html_insertion + '\n\n            <p class="animate delay-2">', content, flags=re.DOTALL)

with open("index.html", "w") as f:
    f.write(content)

with open("styles.css", "r") as f:
    css_content = f.read()

if ".author-profiles" not in css_content:
    with open("styles.css", "a") as f:
        f.write(css_insertion)

# Download Philip Harris photo
try:
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
    urllib.request.install_opener(opener)
    html = urllib.request.urlopen("https://physics.mit.edu/faculty/philip-harris/").read().decode('utf-8')
    match = re.search(r'img.*?class="[^"]*attachment-faculty-portrait[^"]*".*?src="([^"]+)"', html)
    if match:
        urllib.request.urlretrieve(match.group(1), 'images/author_philip.jpg')
        print("Philip Harris photo downloaded.")
except Exception as e:
    print(f"Error downloading photo: {e}")
