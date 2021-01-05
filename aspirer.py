import urllib.request
import re 
import sys
L=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
url='http://127.0.0.1:'+sys.argv[2]+'/vidal/vidal-Sommaires-Substances-A.htm'
f=open("subst.dic",'w',encoding="UTF-16 LE")
f.write('\ufeff')
e=open("infos.txt",'w',encoding="UTF-16 LE")
e.write('\ufeff')
A=str(sys.argv[1])
A=A.upper()
s=0
for i in range(L.index(A[0]),L.index(A[2])+1):
	url=url[:len(url)-5]+L[i]+url[len(url)-4:]
	x=urllib.request.urlopen(url)
	y=re.findall("<a href=\"Substance/.+?>(.+?)</a>",str(x.read().decode('utf8')))
	z=len(y)
	s=s+z
	for j in range(0,len(y)):
		f.write(y[j]+",.N+subst\n")
	e.write(L[i]+":"+str(z)+"\n")
e.write("Total : " + str(s))
e.close()
f.close()		











