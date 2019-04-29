# Not-Vegetable
A Python-based image classifier, specialising in vegetables (since UCT undergrads have no clue what counts as a veggie and what doesn't /s)

## Description

Not-Vegetable was born (as many things are) out of a heated undergrad discussion about what exactly defines a vegetable, as well as a decent number of [Silicon Valley](https://www.youtube.com/watch?v=pqTntG1RXSY) references.

Eventually, Not-Vegetable will classify images as either containing a vegetable or not, thus relieving the undergrads so that they might get round to completing their CompSci assignments.

## File Structure
```
not-vegetable/
    project_file_structure.txt
    README.md
    .gitignore
    project_files/
        duplicate_check.py
        tool_to_create_group_codes.py
        list_project_structure.py
        download_urls.py
        wordnet_id_to_word.txt
        fruit/
            fruit_names.txt
            wordnet_id_to_fruit.txt
            image_urls/
                -----files omitted for brevity-----
        vegetables/
            vegetable_names.txt
            wordnet_id_to_vegetables.txt
            image_urls/
                -----files omitted for brevity-----
```



## Contributing
All pull requests are welcome.

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

-i, --input-file=<FILE>
* Downloads the URIs listed in FILE. You can specify multiple sources for a single entity by putting multiple URIs on a single line separated by the TAB character. Additionally, options can be specified after each URI line. Option lines must start with one or more white space characters (SPACE or TAB) and must only contain one option per line. Input files can use gzip compression. When FILE is specified as -, aria2 will read the input from stdin. See the Input File subsection for details. See also the --deferred-input option. See also the --save-session option.

-d, --dir=<DIR>
* The directory to store the downloaded file.

-j, --max-concurrent-downloads=<N>
* Set the maximum number of parallel downloads for every queue item. See also the --split option. Default: 5

--connect-timeout=<SEC>
* Set the connect timeout in seconds to establish connection to HTTP/FTP/proxy server. After the connection is established, this option makes no effect and --timeout option is used instead. Default: 60

-t, --timeout=<SEC>
* Set timeout in seconds. Default: 60

-m, --max-tries=<N>
* Set number of tries. 0 means unlimited. See also --retry-wait. Default: 5

--lowest-speed-limit=<SPEED>
* Close connection if download speed is lower than or equal to this value(bytes per sec). 0 means aria2 does not have a lowest speed limit. You can append K or M (1K = 1024, 1M = 1024K). This option does not affect BitTorrent downloads. Default: 0

--dry-run [true|false]
* If true is given, aria2 just checks whether the remote file is available and doesn’t download data. This option has effect on HTTP/FTP download. BitTorrent downloads are canceled if true is specified. Default: false



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
See LICENSE.txt

