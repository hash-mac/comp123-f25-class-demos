def print_header(title: str) -> None:
    title = "***** " + title + " "
    print(title.ljust(80, "*"))


print_header("read")
sample_file = open("sample.txt", "r")
content = sample_file.read()
print(repr(content))  # repr shows a printable representation
print(content)


print_header("readlines")
sample_file = open("sample.txt", "r")
lines = sample_file.readlines()
print(repr(lines))
print(lines)


print_header("readline")
sample_file = open("sample.txt", "r")
line = sample_file.readline()
print(repr(line))
print(line)


print_header("for")
sample_file = open("sample.txt", "r")
for line in sample_file:
    print(repr(line))
    print(line)
