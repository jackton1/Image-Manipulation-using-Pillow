from PIL import ImageEnhance, ImageFilter, Image

ribbon = Image.open('ribbon.jpg')

box = (22, 342, 456, 677)

# ribbon_enhancer = ImageEnhance.Color(ribbon)
#
# ribbon_enhancer.enhance(0.6).show()
#
# ribbon_enhancer2 = ImageEnhance.Sharpness(ribbon)
#
# ribbon_enhancer2.enhance(1.2).show()

# ribbon.filter(ImageFilter.GaussianBlur(radius=4)).show()

ribbon.filter(ImageFilter.EMBOSS).show()


