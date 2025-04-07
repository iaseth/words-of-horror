import os
from typing import List


def get_filepaths_in_directory(dirpath):
	filepaths = []
	for root, _, files in os.walk(dirpath):
		for file in files:
			filepath = os.path.join(root, file)
			filepaths.append(filepath)
	return filepaths


def get_epub_file_paths(directory: str, recursive: bool = False) -> List[str]:
	if recursive:
		epub_paths = [os.path.join(root, file)
				for root, _, files in os.walk(directory)
				for file in files if file.lower().endswith('.epub')]
	else:
		epub_paths = [os.path.join(directory, file)
				for file in os.listdir(directory)
				if os.path.isfile(os.path.join(directory, file)) and file.lower().endswith('.epub')]

	epub_paths.sort()
	return epub_paths

