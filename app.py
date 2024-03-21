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
