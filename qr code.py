import qrcode
import image
qr=qrcode.QRCode(
    version=16,
    box_size=10,
    border=5
)
data=" https://en.wikipedia.org/wiki/Varanasi"
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill='black',back_color='white')
img.save('mzp.png')