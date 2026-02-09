#!/usr/bin/env python3

from  pathlib import Path
import shutil

source = Path.home() / 'Pictures' / 'Screenshots'

sshots = source.glob('*.png')

for file_path in sshots:
	if file_path.is_file():
		name_str = file_path.name
		month_label = name_str[16:23]
	
		new_folder = source / month_label
	
		new_folder.mkdir(parents=True, exist_ok=True)
	
		shutil.move(file_path, new_folder / name_str)