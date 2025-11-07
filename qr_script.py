import qrcode
img = qrcode.make('https://github.com/aastroza/talks/tree/main/9punto5')
type(img)  # qrcode.image.pil.PilImage
img.save("qr_9punto5.png")