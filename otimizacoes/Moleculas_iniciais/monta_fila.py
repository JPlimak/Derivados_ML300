#!/usr/bin/env python
import os
import sys
command = sys.argv[1]
directory = sys.argv[2]
extension = sys.argv[3]
l = [f for f in os.listdir(directory) if f.endswith(extension)]
l.sort()
with open(os.path.join(directory,"fila.sh"), 'w') as f:
	f.write("#!/bin/bash\n")
	for arq in l[:-1]:
		f.write("{} {} &&\n".format(command,arq))
	f.write("{} {} &".format(command,l[-1]))
