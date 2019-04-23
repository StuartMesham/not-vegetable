Run all the python scripts here from the "data" directory

words.txt is a list of the image-net.org wndis (WordNet IDs)

In the fruit and vegetable directories there are fruit_names.txt and vegetable_names.txt files respectively. These contain a list of fruit and veggies from Wikipedia.

tool.py was used to help manually create lists of wnids based on the wikipedia fruit and veg lists.

```bash
python3 tool.py python3 tool.py vegetables/vegetable_names.txt
```

These manually created lists are the group_codes.txt files in the fruit and vegetable directories

Next the download_urls.py script was used to download image url lists image-net.org using the wnids

NOTE: don't run this command, it will overwrite the files
```bash
python3 download_urls.py fruit
```

This script automatically downloads and saves the URLs to .txt files in the fruit/image_urls and vegetable/image_urls directories.

Next duplicate_check.py was used to work out how many usable URLs there are (ignoring that many URLs don't work)
```bash
python3 duplicate_check.py
```
