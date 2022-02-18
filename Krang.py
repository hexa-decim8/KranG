# Library imports
import argparse
import ocrmypdf
import subprocess
import httplib2
import os
import io
import shutil
import time
import sys
import nltk
import re
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

# from __future__ import print_function
# from apiclient import discovery
# from oauth2client import client
# from oauth2client import tools
# from oauth2client.file import Storage
# from apiclient.http import MediaFileUpload, MediaIoBaseDownload


#Keep this bundle for when specifying a directory is needed.
#def dir_path(string):
#    if os.path.isdir(string):
#        return string
#    else:
#        raise NotADirectoryError(string)

#Keep this bundle for when specifying a file is needed
#def is_valid_file(parser, arg):
#    if not os.path.exists(arg):
#        parser.error("The file %s does not exist!" % arg)
#    else:
#        return open(arg, 'r')  # return an open file handle


# Argparse body for flags
parser = argparse.ArgumentParser(description='Process files for OCR & NLP needs!')

# OCR arguments
parser.add_argument('--localocr', action='store_true', help='Process all pdfs in the current directory with OCR using local resources.')
parser.add_argument('--cloudocr', action='store_true', help='Process OCR in Google Cloud.')
parser.add_argument('--ocrconvert', action='store_true', help='Converts single pdf to a text file. Also outputs a separate OCRd pdf file')

# Single file arguments
parser.add_argument('--tokenize_sentence', action='store_true', help='Rips out full sentences from a single raw text file.')
parser.add_argument('--stopword_filter', action='store_true', help='Tokenizes stopwords from input text.')
parser.add_argument('--wordripper', action='store_true', help='Tokenizes single words from a single input text file.')
parser.add_argument('--speechpart', action='store_true', help='part-of-speech tagging for a single file.')
parser.add_argument('--crypto_trigraphs', action='store_true', help='searches for cryptonym trigraphs (in testing).')

# Bulk processing arguments
parser.add_argument('--bulk_speechpart', action='store_true', help='Bulk part-of-speech tagging.')
parser.add_argument('--bulk_wordripper', action='store_true', help='Tokenizes all words from the current directory of files.')
#parser.add_argument('--bulk_sentence_tokenizer', action='store_true', help='Bulk sentence tokenizer.')

# Additional arguments
parser.add_argument('--input', type=str, help="input filename")

args = parser.parse_args()

############################
# What u know about loopz? #
############################

# Convert PDF documents to text files
if args.ocrconvert==True:
	os.system('ocrmypdf ' + args.input + ' - | tee output.pdf | pdftotext - output.txt')
sys.exit()

# Local OCR loop
if args.localocr==True:
	for f in glob.glob("*.pdf"):
		print("Running OCR on", f)
		ocrmypdf.ocr(f, f, deskew=True)
	sys.exit()

# Sentence tokenizer
if args.tokenize_sentence==True:
	with open(args.input, 'r', encoding="UTF8") as myfile:
		data=myfile.read().replace('\n', '')
		print(sent_tokenize(data))
	sys.exit()

# Single file wordripper
if args.wordripper==True:
	with io.open(args.input, 'r', encoding="UTF8") as myfile:
		data=myfile.read()
		print(word_tokenize(data))
	sys.exit()

# Stopword filter
if args.stopword_filter==True:
	with open(args.input, 'r', encoding="UTF8") as myfile:
		stop_words = set(stopwords.words("english"))
		print(stop_words)
	sys.exit

# Speechparts
if args.speechpart==True:
	with open(args.input, 'r', encoding="UTF8") as myfile:
		data=myfile.read().replace('\n', '')
		text = word_tokenize(data)
		finished = nltk.pos_tag(text)
		print(finished)
	sys.exit

#########################
# bulk processing loopz #
#########################

# Cloud OCR loop
if args.cloudocr==True:
	print("coming soon!")
sys.exit

# Bulk sentence tokenizer
#if args.bulk_sentence_tokenizer==True:
#	print("coming soon!")
#sys.exit

# Bulk wordripper
# Bulk speechparts

################
# Experimental #
################

# Single file trigraph finder
# I'm going to have to reconstruct the pipeline here. I think it starts with a part of speech processed text file.
# So it should look like, input > part of speech output
if args.crypto_trigraphs==True:
	with open(args.input, 'r', encoding="UTF8") as f:
		data=f.read().replace('\n', '')
# This part tokenizes the part of speech processed text file
		text = word_tokenize(data)
		finished = nltk.pos_tag(text)
		print(finished)

for line in finished:
    match = re.search('[A-Z]{4,}', 'NNP', line)
    print(match)
#    if match:
#        new_line=match.group() + '\n'
#        print(match)

# Bulk trigraph finder
# This feature is nowhere near ready
#for filename in os.listdir("."):
#	if filename.endswith(".txt"):
#		with io.open(filename, 'r', encoding="UTF8") as f:
#			data=f.read().replace('\n', '')
#			text = word_tokenize(data)
#			finished = nltk.pos_tag(text)
#			print(finished)

#for line in finished:
#    match = re.search('[A-Z]{4,}', 'NNP', line)
#    print(match)
#    if match:
#        new_line=match.group() + '\n'
#        print(match)
