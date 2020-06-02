#Source: https://codegolf.stackexchange.com/questions/3783/implement-wc-word-count-shortest-code-wins
q="text.txt"
g=len
z=open(q,'r')
w=z.read()
z.close()
b,e,f=g(w),g(w.replace('\n',' ').split()),w.split('\n')
d,c,a=g(max(f)),g(f),g(open(q,'rb').read())

print(a,b,c,d,e,f)