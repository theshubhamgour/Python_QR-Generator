import qrcode

feature= qrcode.QRCode(version=1,box_size=40,border=3)
feature.add_data('https://www.instagram.com/theshubhamgour')
feature.make(fit=True)

Generator_image = feature.make_image(fill_color="black", back_color="White")
Generator_image.save('image1.png')
