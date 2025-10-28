import qrcode
img = qrcode.make('https://forms.gle/5FqBuDMa93xyoK7C7')
type(img)  # qrcode.image.pil.PilImage
img.save("qr_humo_conce.png")