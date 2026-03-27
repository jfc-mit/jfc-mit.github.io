import os
import re
import glob

paper_dir = "/n/home07/anovak/work/sloppaper2"

tex_files = glob.glob(f"{paper_dir}/**/*.tex", recursive=True)

for tex in tex_files:
    with open(tex, "r") as f:
        content = f.read()
    
    # Simple heuristic to find blocks of figures
    figures = re.findall(r'\\begin\{figure\}.*?\\end\{figure\}', content, re.DOTALL)
    for fig in figures:
        graphics = re.findall(r'\\includegraphics\[.*?\]\{(.*?)\}', fig)
        captions = re.findall(r'\\caption\{(.*?)\}', fig, re.DOTALL)
        if graphics and captions:
            graphics_str = ", ".join(graphics)
            caption_str = captions[0].replace('\n', ' ')[:150]
            print(f"FILE: {graphics_str}")
            print(f"CAPTION: {caption_str}")
            print("-" * 40)
