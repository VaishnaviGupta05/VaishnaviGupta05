
from urllib.request import urlopen
from PIL import Image
from io import BytesIO
import html
import os

USERNAME = "VaishnaviGupta05"
WIDTH = 75
CHARS = "@%#*+=-:. "

url = f"https://github.com/{USERNAME}.png"

with urlopen(url, timeout=20) as response:
    image = Image.open(BytesIO(response.read())).convert("L")

height = max(1, int(image.height / image.width * WIDTH * 0.48))
image = image.resize((WIDTH, height))

pixels = list(image.getdata())
lines = []

for y in range(height):
    row = pixels[y * WIDTH:(y + 1) * WIDTH]
    lines.append("".join(
        CHARS[min(len(CHARS) - 1, pixel * len(CHARS) // 256)]
        for pixel in row
    ))

line_height = 10
svg_height = height * line_height + 70

svg = [
    f'<svg xmlns="http://www.w3.org/2000/svg" width="760" height="{svg_height}" viewBox="0 0 760 {svg_height}">',
    '<rect width="100%" height="100%" rx="12" fill="#0d1117"/>',
    '<rect x="1" y="1" width="758" height="36" rx="12" fill="#161b22" stroke="#30363d"/>',
    '<circle cx="18" cy="18" r="5" fill="#ff5f57"/>',
    '<circle cx="35" cy="18" r="5" fill="#febc2e"/>',
    '<circle cx="52" cy="18" r="5" fill="#28c840"/>',
    '<text x="380" y="23" text-anchor="middle" font-family="monospace" font-size="12" fill="#8b949e">vaishnavi@github: ~/portrait</text>',
    f'<g font-family="monospace" font-size="9" xml:space="preserve">'
]

for index, line in enumerate(lines):
    # Light characters form the brighter parts of the portrait.
    svg.append(
        f'<text x="20" y="{55 + index * line_height}" fill="#58a6ff">'
        f'{html.escape(line)}</text>'
    )

svg.extend([
    '</g>',
    f'<text x="20" y="{svg_height - 12}" font-family="monospace" font-size="10" fill="#39d353">$ portrait generated successfully_</text>',
    '</svg>'
])

os.makedirs("assets", exist_ok=True)

with open("assets/ascii-portrait.svg", "w", encoding="utf-8") as file:
    file.write("\n".join(svg))

print("Created assets/ascii-portrait.svg")
