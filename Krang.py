# Library imports
import argparse
import ocrmypdf
import glob, os
import subprocess
import httplib2
import os
import io
import shutil
import time
import sys
from nltk.tokenize import sent_tokenize, word_tokenize
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
parser = argparse.ArgumentParser(description='Process OCR & NLP needs.')
parser.add_argument('--localocr', action='store_true', help='Process all pdfs in the current directory with OCR using local resources.')
parser.add_argument('--cloudocr', action='store_true', help='Process OCR in Google Cloud.')
parser.add_argument('--tokenize_sentence', action='store_true', help='Rips out full sentences from raw text files.')
parser.add_argument('--bulk_speechpart', action='store_true', help='Bulk part-of-speech tagging.')
parser.add_argument('--stopword_filter', action='store_true', help='Removes stopwords from input text.')
parser.add_argument('--wordripper', action='store_true', help='Word tokenizer.')
parser.add_argument('--bulk_wordripper', action='store_true', help='Rips tokenized words out of the current directory of files.')
parser.add_argument('--input', type=str, help="input filename")
args = parser.parse_args()

#################################
# What u know about loopz mfer? #
#################################
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
