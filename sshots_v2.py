#!/usr/bin/env python3

from  pathlib import Path
import shutil

source = Path.home() / 'Pictures' / 'Screenshots'
sshots = source.glob('*.png')

month_data = {
    "01": "JAN", "02": "FEB", "03": "MAR", "04": "APR",
    "05": "MAY", "06": "JUN", "07": "JUL", "08": "AUG",
    "09": "SEP", "10": "OCT", "11": "NOV", "12": "DEC"
}

for file_path in sshots:
    if file_path.is_file():
        name_str = file_path.name
        year_part = name_str[16:20]
        
        month_num = name_str[21:23]
        month_name = month_data.get(month_num, 'UNKNOWN')
        
        new_label = f'{year_part}-{month_name}'
        new_folder = source / new_label
        new_folder.mkdir(parents=True, exist_ok=True)
        
        shutil.move(file_path, new_folder / name_str)