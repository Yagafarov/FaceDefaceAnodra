README.md
# Rasmlardagi Yuzlarni Anonimlashtirish

Rasmlardagi Yuzlarni Anonimlashtirish, OpenCV va Python Imaging Library (Pillow) yordamida yuzlarni blur qilish va EXIF ma'lumotlarini o'chirish uchun Python skripti.

## Xususiyatlar

- **Yuzni Anonimlashtirish va Blur qilish**: Rasmlarda yuzlarni aniqlab olib, ularni anonimlashtirish uchun Gavay blur qiladi.
- **EXIF Ma'lumotlarini O'chirish**: Rasmlardan shaxsiy ma'lumotlar (EXIF metadata)ni o'chiradi, shuningdek, foydalanuvchining himoyasini ta'minlash uchun.

## O'rnatish

1. Repositoriyani klonlashtiring:

    ```bash
    git clone https://github.com/Yagafarov/FaceDefaceAnodra.git
    cd FaceDefaceAnodra
    ```

2. Zarur qo'llanmalarni o'rnatish:

    ```bash
    pip install -r requirements.txt
    ```

## Foydalanish

Rasmni anonimlashtirish va uning EXIF ma'lumotlarini o'chirish uchun berilgan skriptdan (`deface_image.py`) foydalaning. Skriptni rasm faylini argument sifatida bering.

```code
	from FaceDefaceAnodra import deface_image, clear_exif

	# Rasm manzilini olish
	img_path = './rasm.jpg'

	# Rasmni blur qilish, yuzlarni aniqlash va EXIF metadatalarini tozalash
	output_path_defaced = deface_image(img_path)
	output_path_cleared = clear_exif(output_path_defaced)

	print("Rasm blur qilingan va EXIF metadatalari tozalandi.")
	print("Natijalarni quyidagi manzillarda topasiz:")
	print("Blur qilingan rasm:", output_path_defaced)
	print("Tozalangan rasm:", output_path_cleared)

```
## Natija

Bu sizga ikkita o'zgartirilgan rasmlar yaratadi:

- `defaced_image.jpg`: Yuzlarni blur qilgan rasm.
- `exif_cleared_image.jpg`: EXIF ma'lumotlarini o'chirilgan rasm.


## Talablar

- Python 3.x
- OpenCV (cv2)
- NumPy
- Pillow (PIL)

## Ogohlantirish

Ushbu dastur foydalanuvchining himoyasini ta'minlash uchun yaratilgan va faqat ta'limiy maqsadlar uchun mo'ljallangan. 

## Minnatdorchiliklar

- Yuz aniqlash funksionali OpenCV tomonidan taqdim etilgan Haar xususiyatlarga asoslanadi.
- EXIF ma'lumotlarini o'chirish funksionali Python Imaging Library (Pillow) orqali amalga oshirilgan.


## Before and After

<table>
  <tr>
    <td align="center">Before</td>
    <td align="center">After</td>
  </tr>
  <tr>
    <td><img src="https://github.com/Yagafarov/FaceDefaceAnodra/raw/main/rasm.jpg" alt="Before Image" width="400"/></td>
    <td><img src="https://github.com/Yagafarov/FaceDefaceAnodra/raw/main/test/defaced_rasm.jpg" alt="After Image" width="400"/></td>
  </tr>
</table>
