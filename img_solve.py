from PIL import Image

x = 150
y = 600
im = Image.new("RGB", (x, y))
file = open('img_dump.mem')
for i in range(0, x):
    for j in range(0, y):
        byte = file.read(1)
        im.putpixel((i, j), (ord(byte), ord(byte), ord(byte)))
im.show()
