fin =open ("running-config.cfg")
readfile=fin.read()
def list_ifname_ip ():
	mynote=dict()
	for line in readfile.split():
		word=line.strip()
		if  word not in mynote:
			mynote[line]=1
		else:
			mynote[line]+=1
	print(mynote)
	mylist=[]
	for key,value in mynote.items():
		if "nameif"in mynote:
			mylist.append((value,key))
	print (mylist)
list_ifname_ip()
			
