# Not-Vegetable
A Python-based image classifier, specialising in vegetables (since UCT undergrads have no clue what counts as a veggie and what doesn't /s)

## Description

Not-Vegetable was born (as many things are) out of a heated undergrad discussion about what exactly defines a vegetable, as well as a decent number of [Silicon Valley](https://www.youtube.com/watch?v=pqTntG1RXSY) references.

Eventually, Not-Vegetable will classify images as either containing a vegetable or not, thus relieving the undergrads so that they might get round to completing their CompSci assignments.

## File Structure
```
.
├── LICENSE.txt
├── README.md
├── data
│   └── README.md
└── utils
    ├── clean_data.py
    ├── download_strawberry.sh
    ├── download_urls.py
    ├── fruit_names.txt
    ├── image_database.py
    ├── strawberry.py
    ├── tool_to_create_group_codes.py
    ├── vegetable_names.txt
    ├── wordnet_id_to_fruit.txt
    └── wordnet_id_to_vegetables.txt
```


## Contributing
All pull requests are welcome.

## Quick Start
Run the commands listed here from the project root.

### 1. Install requirements
```bash
pip3 install -r requirements.txt
```

### 1. Create URLs database
```bash
python3 utils/download_urls.py
```

### 2. Create strawberry not-strawberry url lists
```bash
python3 utils/strawberry.py
```

### 3. Download strawberry not-strawberry images
make sure aria2 is installed before running this command
```bash
./utils/download_strawberry.sh
```

## Dependencies
### WordNet
WordNet was used to download many links to images, as well as labels for those images
> WordNet® is a large lexical database of English. Nouns, verbs, adjectives and adverbs are grouped into sets of cognitive synonyms (synsets), each expressing a distinct concept.
> 
> Princeton University "About WordNet." [WordNet](https://wordnet.princeton.edu/). Princeton University. 2010. 

### Aria2
[Aria2](https://aria2.github.io/manual/en/html/aria2c.html) is used to quickly download the image links

Currently the following command is used to download all the links found in ```urls.txt```
```bash
aria2c -i urls.txt -d images -j 50 --connect-timeout=5 --timeout=30 --max-tries=2 --lowest-speed-limit=1K
```


## Usage

Work In Progress:

Run all the python scripts here from the project root.

In the utils directory are the fruit_names.txt and vegetable_names.txt files. These contain a list of fruit and veggies from Wikipedia.

tool_to_create_group_codes.py was used to help manually create lists of wnids based on the wikipedia fruit and veg lists.

```bash
python3 utils/tool_to_create_group_codes.py utils/vegetable_names.txt
```

These manually created lists are the wordnet_id_to_fruit.txt and wordnet_id_to_vegetable.txt files

Next the download_urls.py script was used to download image url lists image-net.org using the wnids.
The urls are saved into a sqlite database in the data directory.

```bash
python3 utils/download_urls.py
```


## License
See LICENSE.txt
