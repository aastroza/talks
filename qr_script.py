import qrcode
img = qrcode.make('https://postgrados.udd.cl/programas/conferencia-iadevs-2025-%e2%80%93-concepcion-235269/')
type(img)  # qrcode.image.pil.PilImage
img.save("qr_iadevs_conce.png")