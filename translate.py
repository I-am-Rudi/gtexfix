import re
import sys
import pickle
import argparse
from replace_tokens import replace_tokens
from replace_latex import replace_latex


parser = argparse.ArgumentParser()
parser.add_argument('filename', type=str)
parser.add_argument("-f", dest="in_lang", default="fr", required=True, help="Language of the source document(s) e.g. DE")
parser.add_argument("-t", dest="out_lang", default="en", required=True, help="Language of the target document e.g EN")    
args = parser.parse_args()

filename = args.filename.split('.')[0]

replace_latex(filename, args.in_lang, args.out_lang)
replace_tokens(filename)