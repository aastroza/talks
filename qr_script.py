import qrcode
img = qrcode.make('https://github.com/aastroza/talks/tree/main/paillaco')
type(img)  # qrcode.image.pil.PilImage
img.save("qr_paillaco.png")