from PIL import Image
img=Image.open("image3.png")
if img.mode != 'RGBA':
        img = img.convert('RGBA')
inverted_data = [(255 - r, 255 - g, 255 - b, a) for r, g, b, a in img.getdata()]
img.putdata(inverted_data)

img.show()  # To display Image 