import _csv
read_file="data.csv"
r_mode="r"

write_file="output.csv"
w_mode="wt"

with open(read_file,r_mode)as fr:
    readfd=_csv.reader(fr)

    with open(write_file,w_mode)as fw:
        writefd = _csv.writer(fw,delimiter='\t')

        for line in readfd:
            writefd.writerow(line)
            #print(line)
