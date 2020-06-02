bytes = 0
lines = 0
wc = 0
with open("text.txt") as f:
    for l in f.readlines():
        lines+=1
        wc+= len(l.split())
bytes = len(open("text.txt",'rb').read())
print(bytes,lines,wc)