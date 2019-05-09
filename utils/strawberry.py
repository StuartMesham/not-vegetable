import utils.image_database as image_database
import codecs
import random

image_database.connect()

#  n07745940 is strawberry wnid

#  select all the images that don't contain strawberries
not_strawberry_urls = image_database.query_urls('''
SELECT url FROM images WHERE id NOT IN (SELECT image_id FROM images_categories_link WHERE category_id = "n07745940")
''')

#  select all the images that don't contain anything other than strawberries
strawberry_urls = image_database.query_urls('''
SELECT url FROM images WHERE id NOT IN (SELECT image_id FROM images_categories_link WHERE NOT category_id = "n07745940")
''')

image_database.close()

random.shuffle(strawberry_urls)
random.shuffle(not_strawberry_urls)

print('strawberries:', len(strawberry_urls))
print('not-strawberries:', len(not_strawberry_urls))

not_strawberry_urls = not_strawberry_urls[:len(strawberry_urls)]
print('not-strawberries to be used:', len(not_strawberry_urls))

f = codecs.open('data/strawberry_urls.txt', 'w', 'utf-8')
for url in strawberry_urls:
    f.write(url + '\n')
f.close()

f = codecs.open('data/not-strawberry_urls.txt', 'w', 'utf-8')
for url in not_strawberry_urls:
    f.write(url + '\n')
f.close()
