# Not-Vegetable
A Python-based image classifier, specialising in vegetables (since UCT undergrads have no clue what counts as a veggie and what doesn't /s)

## Description

Not-Vegetable was born (as many things are) out of a heated undergrad discussion about what exactly defines a vegetable, as well as a decent number of [Silicon Valley](https://www.youtube.com/watch?v=pqTntG1RXSY) references.

Eventually, Not-Vegetable will classify images as either containing a vegetable or not, thus relieving the undergrads so that they might get round to completing their CompSci assignments.

## File Structure
To be reorganised

## Contributing
To be confirmed

### Dependencies
#### WordNet
WordNet was used to download many links to images, as well as labels for those images
> WordNet® is a large lexical database of English. Nouns, verbs, adjectives and adverbs are grouped into sets of cognitive synonyms (synsets), each expressing a distinct concept.
> 
> Princeton University "About WordNet." [WordNet](https://wordnet.princeton.edu/). Princeton University. 2010. 

#### Aria2
[Aria2](https://aria2.github.io/manual/en/html/aria2c.html) is used to quickly download the image links

Currently the following command is used to download all the links found in ```urls.txt```
```bash
aria2c -i urls.txt -d images -j 50 --connect-timeout=5 --timeout=30 --max-tries=2 --lowest-speed-limit=1K
```


## Usage

Work In Progress:

Run all the python scripts here from the "data" directory

words.txt is a list of the image-net.org wnids (WordNet IDs)

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


## License
To be determined


