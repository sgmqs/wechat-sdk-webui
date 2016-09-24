# -*- coding:utf-8 -*-
import StringIO
from PIL import Image

import request


def show_qrcode():
    uuid = request.get_uuid()
    img_src = request.get_qrcode(uuid)

    msg = 'Scan QR Code to log in'
    image = Image.open(StringIO.StringIO(img_src))
    image.show(title=msg)
    image.close()

    print '!!! %s' % msg


def main():
    show_qrcode()


if __name__ == '__main__':
    main()