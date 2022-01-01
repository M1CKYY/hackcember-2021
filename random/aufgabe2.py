from PIL import Image, ImageChops

im1 = Image.open("A.png").convert("1")
im2 = Image.open("B.png").convert("1")

result = ImageChops.logical_xor(im1,im2)
result.save("result2.png")