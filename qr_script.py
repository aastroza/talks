import qrcode
img = qrcode.make('https://github.com/aastroza/talks/tree/main/duoc-summitia-scl')
type(img)  # qrcode.image.pil.PilImage
img.save("some_file.png")