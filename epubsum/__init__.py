"""
epubsum.

Usage:
  epubsum [--preamble <preamble>] [--large] [--overwrite] <bookfile>
  epubsum -h | --help
  epubsum --version

Options:
  --large      Use a large model.
  --overwrite  In directory mode, overwrite existing summaries.
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
from .epubsum import summarize


def main():
    arguments = docopt(__doc__, version=__version__)
    target = arguments['<bookfile>']
    preamble = arguments['<preamble>']
    large = arguments['--large']
    overwrite = arguments['--overwrite']
    summarize(target, preamble=preamble, large=large, overwrite=overwrite)
    
