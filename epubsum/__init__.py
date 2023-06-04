"""
epubsum.

Usage:
  epubsum [--preamble <preamble>] [--large] [--max_tokens <tokens>] [--verbose] <bookfile>
  epubsum -h | --help
  epubsum --version

Options:
  --large      Use a large model.
  <bookfile>   The .epub file to summarize.
  <preamble>   Text to prepend to each section before summarizing. [default: '']

The preamble can be useful in the case of fiction to identify who the narrator is.

"""

__version__ = '0.1'

from docopt import docopt, DocoptExit
from .epubsum import summarize_book


def main():
    arguments = docopt(__doc__, version=__version__)
    bookfile = arguments['<bookfile>']
    preamble = arguments['<preamble>']
    large = arguments['--large']
    verbose = arguments['--verbose']
    summarize_book(bookfile, preamble=preamble, large=large, verbose=verbose)
    
