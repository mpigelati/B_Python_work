
def generatots(num):
    n=0
    while(n<num):
        yield n
        n=n+1

gen =generatots(10)
for i in gen:
    print(i)
