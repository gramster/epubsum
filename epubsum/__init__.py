"""
epubsum.

Usage:
  epubsum [--preamble <preamble>] [--large] <bookfile>
  epubsum [--suffix <suffix>] [--large] [--overwrite] <directory>
  epubsum -h | --help
  epubsum --version

Options:
  --large      Use a large model.
  --overwrite  In directory mode, overwrite existing summaries.
  <bookfile>   The .epub file to summarize or a directory path (see below).
  <preamble>   Text to prepend to each section before summarizing. [default: '']
  <suffix>     The suffix to use for summary files [default: '-summary.txt']

If the <bookfile> form is used, the output will be printed to standard output.
The preamble can be useful in the case of fiction to identify who the narrator is.
It will be prepended on to each section before passing it to the summarizer.

If the <directory> form is used, epubsum will recurse through the directory
and summarize every epub it finds, writing them to files with the same
path and name as the epub file but with the '.epub' extension replaced 
with '-summary.txt' (or whatever is passed as the --suffix argument).

"""

__version__ = '0.3'

from docopt import docopt, DocoptExit
from .epubsum import summarize


def main():
    arguments = docopt(__doc__, version=__version__)
    target = arguments['<bookfile>']
    if not target:
        target = arguments['<directory>']
    preamble = arguments['<preamble>']
    suffix = arguments['<suffix>']
    large = arguments['--large']
    overwrite = arguments['--overwrite']
    summarize(target, preamble=preamble, suffix=suffix, large=large, overwrite=overwrite)
    
