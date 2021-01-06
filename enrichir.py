#coding:utf-8

import re
import sys

q=1
while q<len(sys.argv):
	v=str(sys.argv[q])
	f=open(v,'r')
	i=f.readline()
	l=[]
	while i!="":
	    r=re.findall("([^[\s*’,]+) ([0-9]+|[0-9]+,[0-9]+)( |)(mL|mg|g|cL|dL|L|dg|cg|gr|cp)",i)
	    l=l+r
	    i=f.readline()
	l=list(set(l))

	n=[]
	i=0
	while i<len(l):
	    if  ':'  not in l[i][0] and l[i][0] !="ØALDACTONE" and l[i][0] !="A" and 'à' not in l[i][0] and '('  not in l[i][0] and len(l[i][0]) >=5  and l[i][0]!="béta" and l[i][0]!="ampoul" and l[i][0]!="bêta" and l[i][0]!="faible" and l[i][0]!="spécial" and l[i][0]!="alpha" and l[i][0]!="sang sous" and  l[i][0]!="SPECIAL" and l[i][0]!="jusque" and l[i][0]!="retrouvent" and l[i][0]!="avait" and l[i][0]!="jours" and l[i][0]!="après":
	        i=i+1
	    else:
	        n.append(l[i])
	        l.pop(i)
	i=0


	l.append(("ALDACTONE"))
	f=open("subst_enri.dic",'w',encoding="UTF-16 LE")
	f.write('\ufeff')




	for i in range(0,len(l)-1):
		f.write(l[i][0]+",.N+subst\n")

	f.close()


	i=0
	s=[]

	while i<len(l):
		j=i+1
		s.append(l[i][0].lower())
		while j<len(l):
			if l[i][0]==l[j][0]:
				l.pop(j)
			else:
				j=j+1
		i=i+1


	g=open("subst.dic",'r',encoding="UTF-16 LE")

	i=g.readline()
	l=[]
	while i!="":
		l.append(re.findall(".+(?=,)",i)[0])
		i=g.readline()
	g.close()

	L=['A', 'B', 'C', 'D', 'E','É', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	e=open("infos2.txt",'w',encoding="UTF-16 LE")
	e.write('\ufeff')
	m=[]

	for i in s:
		if i not in l:
			l.append(i)
			m.append(i)

	l.sort()
	n=0
	for i in L :
		k=0
		for j in l:
			if j[0].upper()==i:
				k=k+1
		n=n+k
		e.write(i+":"+str(k)+"\n")
	e.write("Total : "+str(n))
	e.close()
	f=open("subst.dic",'w',encoding="UTF-16 LE")
	f.write('\ufeff')
	l.pop(len(l)-1)
	f.write("abacavir,.N+subst\n")





	for i  in l :
		if i != 'a':
			f.write(i+",.N+subst\n")
	f.close()
	q=q+1










