# KranG
![Krang](images/krang.jpg)

KranG is a set of scripts that can be used in text processing for OCR and NLP pipeline building.

# Repo notes
A new repository has been created for all work on this OCR/NLP tool going forward. I'm still working on consolidating the disperate collection
of scripts into one central script for better NLP pipelining.

Because of all of the confusion with the state of this (old) project, I've migrated all of the previously available KrangTools resources to this
new project forevermore known as KranG. It is possible that you'll notice some remnants of the old naming scattered around the scripts, I'll also
be working on clearing all of that out over time as well.

# What Is KranG?
Previously known as 'KrangTools', KranG was originally developed to deal with CREST PDFs which do not come as searchable documents. This means that there
are tens of thousands of files that cannot be easily reviewed by researchers. We solve this problem through OCR, and go the 
extra mile to help researchers by adding some basic Natural Language Processing to help them study the information.

# New in this repo
I'm merging all of the standalone scripts into one mighty python script to do all the things. Please see the features list below
for more details. Once the backlog of scripting has been added to the main KranG script, I can begin working on feature requests.
 
# Features
* OCR
    * Local OCR processing - WORKING!
    * Google Cloud OCR processing - Under Construction
* NLP
    * bulk part of speech processing - Under Construction
    * bulk word processing - Under Construction
    * sentence tokenizer - WORKING!
    * single file part of speech processing - WORKING!
    * stopword processing - WORKING!
    * word tokenizer - WORKING!

Each of these features is currently provided by individual scripts (which are already available in this repo if you'd like to use them.)
Current work is intended to press all of these features into a single python exe.

# Usage
Krang.py is currently under development, but current args include:
```
`--localocr` - Runs OCR processing over files using local resources
`--cloudocr` - Runs OCR processing over files using Google Docs cloud OCR resources
`--tokenize_sentence` - Tokenizes sentences from input file
`--bulk_speechpart` - Part of speech processing for a directory of files
`--stopword_filter`- Processes stopwords from a single file
`--wordripper` - Word tokenizer for individual files
`--bulk_wordripper` - Bulk word tokenizer
`--speechpart` - part-of-speech tagging for a single file
`--input` - Specifies file input
```
# Usage

>python3 Krang.py --tokenize_sentence --input foo.txt
