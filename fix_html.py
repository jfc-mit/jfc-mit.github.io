import re
import os

os.chdir('/n/home07/anovak/work/jfc-mit.github.io')

with open("index.html", "r") as f: content = f.read()

# Replace images with cache bust version
content = re.sub(r'src="images/author_(\w+)\.(jpg|png)"', r'src="images/author_\1.jpg?v=3"', content)

# Replace specific titles with explicit <br>s
content = content.replace(
    '<div class="author-title">Researcher with LHC &amp; Physics PhD at MIT</div>',
    '<div class="author-title">Researcher with LHC<br>Physics PhD at MIT</div>'
)
content = content.replace(
    '<div class="author-title">IAIFI Fellow at MIT</div>',
    '<div class="author-title">IAIFI Fellow<br>at MIT</div>'
)
content = content.replace(
    '<div class="author-title">Postdoc @ MIT | Particle Physics &amp; Machine Learning</div>',
    '<div class="author-title">Postdoc @ MIT<br>Particle Physics &amp; Machine Learning</div>'
)
content = content.replace(
    '<div class="author-title">Fellow at CERN</div>',
    '<div class="author-title">Fellow<br>at CERN</div>'
)
content = content.replace(
    '<div class="author-title">Associate Professor of Physics</div>',
    '<div class="author-title">Associate Professor<br>of Physics</div>'
)

with open("index.html", "w") as f: f.write(content)
