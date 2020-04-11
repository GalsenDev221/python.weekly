# author @daoodaba975
# GalsenDev

import qrcode
img = qrcode.make('Hello world!')
img.save('hello-world.png')