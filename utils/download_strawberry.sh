#!/bin/bash

mkdir -p data/strawberry
mkdir -p data/not-strawberry

aria2c -i data/strawberry_urls.txt -d data/strawberry -j 50 --connect-timeout=5 --timeout=30 --max-tries=2 --lowest-speed-limit=1K --optimize-concurrent-downloads=true
python3 utils/remove_non_images.py data/strawberry

aria2c -i data/not-strawberry_urls.txt -d data/not-strawberry -j 50 --connect-timeout=5 --timeout=30 --max-tries=2 --lowest-speed-limit=1K --optimize-concurrent-downloads=true
python3 utils/remove_non_images.py data/not-strawberry