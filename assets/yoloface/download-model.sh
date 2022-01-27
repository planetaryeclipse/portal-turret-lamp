#!/bin/bash

# based on the script provided in the yoloface repository but modified to only
# pull only the weights file as nothing else is needed

MODEL_ARCHIVE_FILE=yolov3-wider_16000.weights.zip

echo "Downloading the yoloface model..."
wget --load-cookies /tmp/cookies.txt -r "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=13gFDLFhhBqwMw6gf8jVUvNDH2UrgCCrX' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=13gFDLFhhBqwMw6gf8jVUvNDH2UrgCCrX" -O $MODEL_ARCHIVE_FILE && rm -rf /tmp/cookies.txt

echo "Unpacking..."
unzip -q $MODEL_ARCHIVE_FILE

echo "Cleaning up..."
rm $MODEL_ARCHIVE_FILE

echo "Done"
