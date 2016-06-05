import exifread

f = open(r'C:\Users\jacob\Desktop\Python\exif\img_1771.jpg', 'rb')

tags = exifread.process_file(f)

print("\nBelow is some information hidden in your image:\n")

for tag in tags.keys():
	if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'FileName', 'EXIF Makernote'):
		print ("\t%s: %s" % (tag, tags[tag]))