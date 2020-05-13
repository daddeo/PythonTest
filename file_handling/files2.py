# https://docs.python.org/3/library/pathlib.html
#
# old sytle is to use {os}
# os.path
#
# >= Python 3.6 use
# Path from pathlib
# has better performance as it can avoid calls to the OS

from pathlib import Path

cwd = Path.cwd()
print(f"cwd: {cwd}")

demo_file_path = Path.joinpath(cwd, "input/filedata.txt")
demo_file = Path(demo_file_path)

print(f"name: {demo_file.name}")
print(f"suffix: {demo_file.suffix}")
print(f"folder: {demo_file.parent.name}")
print("size: " + str(demo_file.stat().st_size))

parent = cwd.parent
print(f"\nparent: {parent}")
print("Is this a directory? --> " + str(parent.is_dir()))
print("Is this a file? --> " + str(parent.is_file()))

# List child directories
print("-----directory contents-----")
for child in parent.iterdir():
    if child.is_dir():
        print(f"[d] {child}")
    elif child.is_file():
        print(f"[ ] {child}")

# Create full path name by joining path and filename
new_file = Path.joinpath(cwd, "new_file.txt")
# Full path: c:\dev\src\Python\PythonTest\new_file.txt
print("\nFull path: " + str(new_file))

# Does that 'new_file.txt' exist? False
print("Does that 'new_file.txt' exist? " + str(new_file.exists()))
# Does that 'filedata.txt' exist? True
print("Does that 'filedata.txt' exist? " + str(demo_file.exists()))
