s=" this is the end hold you breathe and count to ten  to"

word= s.split(" ")
dct={}
for i in word:
    if i in dct:
	    dct[i]+=1
    else:
	    dct[i]=1
print(dct)
