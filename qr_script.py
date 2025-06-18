import qrcode
img = qrcode.make('https://github.com/aastroza/talks/tree/main/duoc-summitia-valpo')
type(img)  # qrcode.image.pil.PilImage
img.save("some_file_2.png")