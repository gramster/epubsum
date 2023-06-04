import os
from bs4 import BeautifulSoup
from cleantext import clean
from ebooklib import ITEM_DOCUMENT, epub
from textsum.summarize import Summarizer


def extract_sections_from_epub(epub_file_path):
    book = epub.read_epub(epub_file_path)
    section_texts = []

    for item in book.get_items():
        # Check if the item is an XHTML content file
        if item.get_type() == ITEM_DOCUMENT and item.media_type == 'application/xhtml+xml':
            content = item.get_content()
            soup = BeautifulSoup(content, 'html.parser')
            text = soup.get_text(separator=' ').strip()
            if text:
                section_texts.append(text)

    return section_texts


def summarize_book(bookfile, preamble='', large=False, verbose=False):
    if large:
        summarizer = Summarizer(model_name_or_path='pszemraj/long-t5-tglobal-xl-16384-book-summary')
    else:
        # pszemraj/long-t5-tglobal-base-16384-book-summary
        summarizer = Summarizer()
    parts = []
    for i, text in enumerate(extract_sections_from_epub(bookfile)):
        parts.append(f'\n\n=====[ Section {i} ]=======================================\n\n')
        parts.append(summarizer.summarize_string(preamble + clean(text)))

    return ''.join(parts)





