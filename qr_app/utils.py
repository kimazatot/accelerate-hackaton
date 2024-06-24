# qr_app/utils.py
import qrcode
from io import BytesIO
from django.core.files.base import ContentFile

def generate_qr_code(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    byte_io = BytesIO()
    img.save(byte_io, format='PNG')
    byte_io.seek(0)
    return ContentFile(byte_io.read(), name='qr_code.png')
