import zipfile
from pathlib import Path

p = Path(".")
example_zip = zipfile.ZipFile(p / "example.zip")
print(example_zip.namelist())

spam_info = example_zip.getinfo("spam.txt")
print(f"File Size: {spam_info.file_size}")
print(f"Compress Size: {spam_info.compress_size}")

smaller = round(spam_info.file_size / spam_info.compress_size, 2)
print(f"Compressed file is {smaller}x smaller!")
