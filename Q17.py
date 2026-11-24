source_file = "source.txt"
destination_file = "destination.txt"


with open(source_file, "w") as src:
    src.write("Hello! This is the original text.\nIt will be copied to another file.")

    with open(source_file, "r") as src, open(destination_file, "w") as dest:
        content = src.read()
        dest.write(content)
    print(f"Contents successfully copied from '{source_file}' to '{destination_file}'.")

