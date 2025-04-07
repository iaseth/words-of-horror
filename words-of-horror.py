#!/usr/bin/env python3

import re
from tabulate import tabulate
from collections import Counter
from ebooklib import epub, ITEM_DOCUMENT
from bs4 import BeautifulSoup

from pywoh.utils import get_epub_file_paths



def extract_text_from_epub(epub_path):
	book = epub.read_epub(epub_path, {"ignore_ncx": True})
	text_content = []

	for item in book.get_items():
		if item.get_type() == ITEM_DOCUMENT:
			soup = BeautifulSoup(item.get_content(), 'html.parser')
			text_content.append(soup.get_text())

	return ' '.join(text_content)

def clean_and_tokenize(text):
	words = re.findall(r'\b[a-z]+\b', text.lower())
	return words

def get_most_common_words(words, n=20):
	return Counter(words).most_common(n)


def analyze_epub(epub_path: str):
	print(f"Reading from {epub_path}...")

	text = extract_text_from_epub(epub_path)
	words = clean_and_tokenize(text)
	common_words = get_most_common_words(words)

	print("\nMost common words:")
	rows = [[word, count, int(1000 * 1000 * count / len(words))] for word, count in common_words]
	print(tabulate(rows))
	print(epub_path)


def main():
	epub_paths = get_epub_file_paths("./epubs")
	for epub_path in epub_paths:
		analyze_epub(epub_path)
		break


if __name__ == '__main__':
	main()
