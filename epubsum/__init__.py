"""
epubsum.

Usage:
  epubsum [--preamble <preamble>] [--large] [--max_tokens <tokens>] <bookfile>
  epubsum -h | --help
  epubsum --version

Options:
  --large      Use a large model.
  <bookfile>   The .epub file to summarize or a directory path (see below).
  <preamble>   Text to prepend to each section before summarizing. [default: '']

The preamble can be useful in the case of fiction to identify who the narrator is.

If <bookfile> is a directory, epubsum will recurse through the directory
and summarize every epub it finds, writing them to files with the same
path and name asd the epub file but with the '.epub' extension replaced 
with '-summary.txt'.

"""

__version__ = '0.2'

from docopt import docopt, DocoptExit
from .epubsum import summarize_book


def main():
    arguments = docopt(__doc__, version=__version__)
    bookfile = arguments['<bookfile>']
    preamble = arguments['<preamble>']
    large = arguments['--large']
    verbose = arguments['--verbose']
    summarize_book(bookfile, preamble=preamble, large=large, verbose=verbose)
    
