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


def summarize_epub_file(summarizer, bookfile, preamble=''):
    print(f'Summarizing {bookfile}\n')
    parts = []
    for i, text in enumerate(extract_sections_from_epub(bookfile)):
        parts.append(f'\n\n=====[ Section {i} ]=======================================\n\n')
        parts.append(summarizer.summarize_string(preamble + clean(text)))

    return ''.join(parts)


def summarize_epub_files(summarizer, directory, preamble):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.epub'):
                epub_path = os.path.join(root, file)
                summary = summarize_epub_file(summarizer, epub_path, preamble)
                summary_path = os.path.splitext(epub_path)[0] + '-summary.txt'
                with open(summary_path, 'w') as summary_file:
                    summary_file.write(summary)


def summarize(target, preamble='', large=False):
    if large:
        summarizer = Summarizer(model_name_or_path='pszemraj/long-t5-tglobal-xl-16384-book-summary')
    else:
        # pszemraj/long-t5-tglobal-base-16384-book-summary
        summarizer = Summarizer()

    if os.path.isdir(target):
        summarize_epub_files(summarizer, target, preamble)
    else:
        print(summarize_epub_file(summarizer, target, preamble))
        




