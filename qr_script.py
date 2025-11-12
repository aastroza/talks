import qrcode
img = qrcode.make('https://github.com/aastroza/talks/tree/main/melitalks')
type(img)  # qrcode.image.pil.PilImage
img.save("qr_melitalks.png")