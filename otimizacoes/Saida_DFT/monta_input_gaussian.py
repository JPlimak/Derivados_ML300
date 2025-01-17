#!/usr/bin/env python
import os
import sys
file_to_read = sys.argv[1]
directory = sys.argv[2]
extension = sys.argv[3]
with open(os.path.join(directory,file_to_read), 'r') as f:
	linesToAdd = f.readlines()
l = [f for f in os.listdir(directory) if f.endswith(extension)]
for file_to_write in l:
	with open(os.path.join(directory,file_to_write), 'r') as f:
		lines = f.readlines()
	with open(os.path.join(directory,file_to_write), 'w') as f:
		for line in linesToAdd:
			f.write(line)
		for line in lines[2:]:
			if not line.endswith("**\n"):
				f.write(line)
			else:
				f.write(file_to_write[:-4]+'\n')
		f.write("Br 1.90\n\n")
