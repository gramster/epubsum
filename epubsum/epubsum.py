import os
from bs4 import BeautifulSoup
from cleantext import clean
from ebooklib import ITEM_DOCUMENT, epub
from textsum.summarize import Summarizer
from textwrap import wrap


def extract_sections_from_epub(epub_file_path):
    book = epub.read_epub(epub_file_path)
    section_texts = {}

    for item in book.get_items():
        if isinstance(item, epub.EpubHtml) and item.is_chapter():
            title = item.title if item.title else item.get_name()
            content = item.get_content()
            soup = BeautifulSoup(content, 'html.parser')
            text = soup.get_text(separator=' ').strip()
            if text:
                section_texts[title] = text

    return section_texts


def summarize_epub_file(summarizer, bookfile, preamble=''):
    print(f'Summarizing {bookfile}\n')
    parts = []
    for name, text in extract_sections_from_epub(bookfile).items():
        parts.append(f'\n\n=====[ {name} ]=====\n\n')
        summary = summarizer.summarize_string(preamble + clean(text))
        paragraphs = summary.split('\n')
        summary = '\n\n'.join(['\n'.join(wrap(p)) for p in paragraphs])
        parts.append(summary)

    return ''.join(parts)


def summarize_epub_files(summarizer, directory, preamble, overwrite):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.epub'):
                epub_path = os.path.join(root, file)
                summary_path = os.path.splitext(epub_path)[0] + '-summary.txt'
                if overwrite or not os.path.exists(summary_path):
                    summary = summarize_epub_file(summarizer, epub_path, preamble)
                    with open(summary_path, 'w') as summary_file:
                        summary_file.write(summary)


def summarize(target, preamble='', large=False, overwrite=False):
    if large:
        summarizer = Summarizer(model_name_or_path='pszemraj/long-t5-tglobal-xl-16384-book-summary')
    else:
        # pszemraj/long-t5-tglobal-base-16384-book-summary
        summarizer = Summarizer()

    if os.path.isdir(target):
        summarize_epub_files(summarizer, target, preamble, overwrite)
    else:
        print(summarize_epub_file(summarizer, target, preamble))
        




