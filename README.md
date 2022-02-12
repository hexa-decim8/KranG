# KrangTools
[Krang](images/krang.jpg)
KrangTools is a set of scripts that can be used in text processing for OCR and NLP pipeline building.

# Repo notes
The original repo is orphaned, and any future development on this project will happen here.

It's been a few years since I've worked on this project, but I do plan on doing some work soon, so keep an eye
on updates here in this repo.

# What Is KrangTools?
KrangTools was originally developed to deal with CREST PDFs which do not come pre-searchable. This means that there
are tens of thousands of files that cannot be easily reviewed by researchers.

# New in this repo
I'm merging all of the standalone scripts into one mighty python script to do all the things. Please see the features list below
for more details.
 
# Features
* OCR
    * Local OCR processing - WORKING!
    * Google Cloud OCR processing - Under Construction
* NLP
    * bulk part of speech processing - Under Construction
    * bulk word processing - Under Construction
    * sentence tokenizer - WORKING!
    * a la carte part of speech processing - Under Construction
    * stopword processing - Under Construction
    * a la carte word processing - Under Construction

Each of these features is currently provided by individual scripts. Current work is intended to press all of these
features into a single python exe.

# Usage
Krang.py is currently under development, but current args include:
`--localocr`
`--cloudocr`
`--tokenize_sentence` - tokenizes sentences from input file
`--bulk_speechpart`
`--stopword_filter`
`--wordripper`
`--bulk_wordripper`
`--input` - specifies file input.

# Usage

>python3 Krang.py --tokenize_sentence --input foo.txt
