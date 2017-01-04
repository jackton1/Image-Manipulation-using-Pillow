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

# Rotate and expand if image out of screen proportion
# balloons.rotate(40, expand=True).show()

# Save the image after manipulation
# balloons.rotate(-90, expand=True).save('balloon2_rot.jpg')

# Save the image after manipulation with a different format
# balloons.rotate(90, expand=True).save('balloon1_rot.jpg', format='png')

box = (23, 450, 580, 693)


# Convert a image to two subsets by cropping and pasting the cropped image back
# with the original
# region = balloons.crop(box)
# region = region.convert(mode='L')
# balloons2 = balloons.copy()
# balloons2.paste(region, box)
# balloons2.show()

# region2 = balloons.crop(box)
# # Transpose only does 90' conversion
# region2 = region2.transpose(Image.FLIP_TOP_BOTTOM)
# balloons3 = balloons.copy()
# balloons3.paste(region2, box)
# balloons3.show()
