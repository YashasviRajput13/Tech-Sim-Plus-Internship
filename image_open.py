from PIL import Image,ImageFilter
img = Image.open("my.jpeg")
new_img=img.filter(ImageFilter.BLUR)
img.show()
# new_img.show()
# bw_img=img.convert("L")
# bw_img.show()
# rotateimage = img.rotate(75)
# rotateimage.show()