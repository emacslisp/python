#!/usr/bin/python

FileName = '/path/to/file';

with open(FileName) as f:
    newText=f.read().replace('A', 'orange')
    
with open(FileName, "w") as f:
    f.write(newText)
