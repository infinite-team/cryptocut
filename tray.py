import pystray
from PIL import Image, ImageDraw

icon = pystray.Icon('CryptoCut')

width=100
height=100
color1="red"
color2=""

# Generate an image
image = Image.new('RGB', (width, height), color1)
dc = ImageDraw.Draw(image)
dc.rectangle((width // 2, 0, width, height // 2), fill=color2)
dc.rectangle((0, height // 2, width // 2, height), fill=color2)

icon.icon = image
