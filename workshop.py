from PIL import Image

balloons = Image.open('ballon.jpg')
ribbons = Image.open('ribbon.jpg')


# (1-bit pixels, black and white, stored with one pixel per byte)
# balloons.convert(mode='1').show()

# (8-bit pixels, black and white)
# balloons.convert(mode='L').show()

# (3x8-bit pixels, true color)
# balloons.convert(mode='RGB').show()

# (4x8-bit pixels, true color with transparency mask)
# balloons.convert(mode='RGBA').show()

# ribbons.convert(mode='1').show()

# Cropping the image to specified width and height
# ribbons.resize((500, 300)).show()

# Resizing the image with the aspect ratio considered
# ribbons.resize((ribbons.width//2, ribbons.height//2)).show()

# Thumbnail
# b2 = balloons.copy()

# b2.thumbnail((500, 200))

# b2.show()

# Cropping
# box = (23, 450, 580, 693)
#
# b3 = balloons.copy()
#
# b3.crop(box).show()

# Rotate
balloons.rotate(40, expand=True).show()
