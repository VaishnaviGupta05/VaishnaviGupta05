
from PIL import Image
from urllib.request import urlopen
from io import BytesIO

USERNAME = "VaishnaviGupta05"
WIDTH = 65

# Download your GitHub profile picture
url = f"https://github.com/{USERNAME}.png"
image_data = urlopen(url).read()
image = Image.open(BytesIO(image_data)).convert("L")

# Resize while accounting for character height
height = int(image.height / image.width * WIDTH * 0.45)
image = image.resize((WIDTH, height))

characters = "@%#*+=-:. "
pixels = list(image.getdata())

ascii_art = "\n".join(
    "".join(
        characters[pixel * (len(characters) - 1) // 255]
        for pixel in pixels[y * WIDTH:(y + 1) * WIDTH]
    )
    for y in range(height)
)

with open("assets/portrait.txt", "w", encoding="utf-8") as file:
    file.write(ascii_art)

print(ascii_art)
print("\nSaved to assets/portrait.txt")
