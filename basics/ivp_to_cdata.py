#!/usr/bin/python2

import sys,re
infile = open(sys.argv[1])

state=0
for line in infile.readlines():
    if state==0 and line.startswith("CheckBlock") or line.startswith("WriteBlock"):
        sys.stdout.write(line)
        state=1
    elif state==1 and line.startswith("Data"):
        sys.stdout.write(line)
        m=re.match(r'Data\s+(\d+)',line)
        blocklen=int(m.group(1))
        bytesread=0
        sys.stdout.write("{\n")
        state=2
    elif state==2:
        words=line.split()
        bytelist = []
        for w in words:
            for i in range(4):
                b=int(w[6-2*i:8-2*i], 16)
                bytelist.append(b)
        nbytes=4*len(words)
        if nbytes+bytesread > blocklen:
            nbytes = blocklen-bytesread
        bytesread+=nbytes
        for i in range(nbytes):
             sys.stdout.write("0x%02x, " % bytelist[i])
             if i % 8 == 7:
                 sys.stdout.write("\n")
        if bytesread == blocklen:
            if nbytes % 8:
                sys.stdout.write("\n")
            sys.stdout.write("};\n")
            state=0
    else:
        sys.stdout.write(line)
        state=0


infile.close()
