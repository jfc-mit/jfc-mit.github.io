import re
import os

os.chdir('/n/home07/anovak/work/jfc-mit.github.io')

with open("index.html", "r") as f:
    html = f.read()

# Append superscripts
html = re.sub(r'(>Eric A.\s*Moreno</a>)(?!<sup)', r'\1<sup>1,2</sup>', html)
html = re.sub(r'(>Samuel Bright-Thonney</a>)(?!<sup)', r'\1<sup>1,2</sup>', html)
html = re.sub(r'(>Andrzej\s*Novak</a>)(?!<sup)', r'\1<sup>1,2</sup>', html)
html = re.sub(r'(>Dolores\s*Garcia</a>)(?!<sup)', r'\1<sup>3</sup>', html)
html = re.sub(r'(>Philip\s*Harris</a>)(?!<sup)', r'\1<sup>1,2</sup>', html)

# Add institutions div
inst_html = """            <div class="institutions animate delay-1" style="text-align: center; font-size: 0.85rem; color: var(--text-muted); margin-top: -1.5rem; margin-bottom: 2.5rem; line-height: 1.6;">
                <sup>1</sup> Department of Physics, Massachusetts Institute of Technology<br>
                <sup>2</sup> <a href="https://iaifi.org/" target="_blank" rel="noopener noreferrer" style="color: inherit; border-bottom: 1px dotted var(--text-muted); text-decoration: none;">NSF AI Institute for Artificial Intelligence and Fundamental Interactions</a><br>
                <sup>3</sup> CERN
            </div>"""

if "class=\"institutions" not in html:
    html = html.replace('</div>\n\n            <p class="animate delay-2">', '</div>\n\n' + inst_html + '\n\n            <p class="animate delay-2">')

with open("index.html", "w") as f:
    f.write(html)
