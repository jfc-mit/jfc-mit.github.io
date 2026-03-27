from PIL import Image
import os

files = [
    ("/n/home07/anovak/.gemini/antigravity/brain/d3c55ff5-955f-4604-8d8a-fa5687de71d2/media__1774645818654.jpg", "eric"),
    ("/n/home07/anovak/.gemini/antigravity/brain/d3c55ff5-955f-4604-8d8a-fa5687de71d2/media__1774645824763.jpg", "sam"),
    ("/n/home07/anovak/.gemini/antigravity/brain/d3c55ff5-955f-4604-8d8a-fa5687de71d2/media__1774645828472.png", "andrzej"),
    ("/n/home07/anovak/.gemini/antigravity/brain/d3c55ff5-955f-4604-8d8a-fa5687de71d2/media__1774645833747.jpg", "dolores"),
    ("/n/home07/anovak/.gemini/antigravity/brain/d3c55ff5-955f-4604-8d8a-fa5687de71d2/media__1774645837673.png", "philip")
]

for fp, name in files:
    try:
        if os.path.exists(fp):
            img = Image.open(fp).convert('RGB')
            dest = f"/n/home07/anovak/work/jfc-mit.github.io/images/author_{name}.jpg"
            img.save(dest, "JPEG")
            print(f"Successfully converted {name} image.", flush=True)
        else:
            print(f"Could not find {fp}!", flush=True)
    except Exception as e:
        print(f"Error converting {name}: {e}", flush=True)
