import csv

read_file="data.csv"
r_mode="r"

with open(read_file,r_mode) as fd:
    read_file_fd=csv.DictReader(fd)
    for line in read_file_fd:
        print(line["email"])