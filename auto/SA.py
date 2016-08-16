from PIL import Image
import imagehash

hash = imagehash.average_hash(Image.open('test.png'))
print(hash)
