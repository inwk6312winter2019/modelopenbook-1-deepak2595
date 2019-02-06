
			
import math
def list_ifname_ip():
    mytask = open('running-config.cfg')
    nameifdict=dict()

    for line in mytask:
        if "nameif" in line:
            mytemplist = line.split()

            next(mytask)
            templine = next(mytask)
            newlist= templine.split()

            if mytemplist[0]=='nameif':
                if newlist[0] == 'ip':
                    mytuple=(newlist[2:])
                    nameifdict[mytemplist[1]]=mytuple

    return (nameifdict)

ipconfigs = list_ifname_ip()
print(ipconfigs)
