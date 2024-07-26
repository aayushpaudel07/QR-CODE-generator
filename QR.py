import qrcode
from PIL import Image
import qrcode
from PIL import Image
url = input("Enter the URL: ")
qr=qrcode.QRCode(version=1,box_size=10,border=5,error_correction=qrcode.constants.ERROR_CORRECT_L)
qr.add_data(url)
qr.make(fit=True)
img=qr.make_image(fill_color='black',back_color='white')
img.save('C:/Users/patel/Desktop/qr.png')

