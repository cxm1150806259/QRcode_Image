import qrcode
from PIL import Image

# type1
# img = qrcode.make('simpleqrcode')
# img.save('simpleqrcode.jpg')

# type2
# qr = qrcode.QRCode(version=2,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=10,border=10,)
# qr.add_data('https://www.baidu.com')
# qr.make(fit=True)
# img = qr.make_image()
# img.show()

# type3
arr = ["A","B"]
# qr = qrcode.QRCode(version=5,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=8,border=4)

# for data in arr:
    # qr.clear()
    # qr.add_data(data)
    # qr.make(fit=True)
    #
    # img = qr.make_image()
    # img = img.convert("RGBA")
    #
    # icon = Image.open("icon.png")
    #
    # img_w, img_h = img.size
    # factor = 4
    # size_w = int(img_w / factor)
    # size_h = int(img_h / factor)
    #
    # icon_w, icon_h = icon.size
    # if icon_w > size_w:
    #     icon_w = size_w
    # if icon_h > size_h:
    #     icon_h = size_h
    # icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)
    #
    # w = int((img_w - icon_w) / 2)
    # h = int((img_h - icon_h) / 2)
    # icon = icon.convert("RGBA")
    # img.paste(icon, (w, h), icon)
    # # img.show()
    # filename = data + ".png"
    # img.save('QRImages/' + filename)
    # print(filename+"---"+data)

def createQRImage(data):
    qr = qrcode.QRCode(version=5, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=8, border=4)
    qr.clear()
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image()
    img = img.convert("RGBA")

    icon = Image.open("icon.png")

    img_w, img_h = img.size
    factor = 4
    size_w = int(img_w / factor)
    size_h = int(img_h / factor)

    icon_w, icon_h = icon.size
    if icon_w > size_w:
        icon_w = size_w
    if icon_h > size_h:
        icon_h = size_h
    icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)

    w = int((img_w - icon_w) / 2)
    h = int((img_h - icon_h) / 2)
    icon = icon.convert("RGBA")
    img.paste(icon, (w, h), icon)
    # img.show()
    filename = data + ".png"
    img.save('QRImages/' + filename)
    print(filename + "---" + data)

for data in arr:
    createQRImage(data)