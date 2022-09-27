import pyscreenshot

image=pyscreenshot.grab(bbox=(500,100,600,600))

image.show()

image.save('ss4 .png')
