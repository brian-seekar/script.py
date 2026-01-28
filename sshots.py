# a gentle introduction to system automation on linux using python and crontab
# to sort screenshots taken on my system into folders matching the month of capture
# using pathlib

source = Path.home() / 'Pictures' / 'Screenshots'

sshots = source.glob('*.png')

for file_path in sshots:
	if file_path.is_file():
		name_str = file_path.name
		month_label = name_str[16:23]
	
		new_folder = source / month_label
	
		new_folder.mkdir(parents=True, exist_ok=True)
	
		shutil.move(file_path, new_folder / name_str)