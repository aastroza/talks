import qrcode
img = qrcode.make('https://conferencia.iadevs.cl/')
type(img)  # qrcode.image.pil.PilImage
img.save("qr_iadevs.png")