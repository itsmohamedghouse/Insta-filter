# import Image frm PIL
from PIL import Image

# load images into objects
base_img=Image.open("4.jpg")
img_filter=Image.open("filter.jpg")
third_image=Image.open("4.jpg")

#set image size
size=(760,760)
base_img=base_img.resize(size)
img_filter=img_filter.resize(size)
r,g,b=base_img.split()
R,G,B=img_filter.split()
Rr,Gg,Bb=third_image.split()
im=Image.merge("RGB",(r,g,B))
# im=Image.merge("HSV",(R,g,B))
im.show()
im.save('merged.jpg','jpg')