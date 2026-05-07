from PIL import Image,ExifTags
img = Image.open("fontainhas.jpg")

exif_data = img._getexif()
for tag_id, value in exif_data.items():
    tag_name = ExifTags.TAGS.get(tag_id,"Unknown")
    print(f"{tag_name} : {value} \n")