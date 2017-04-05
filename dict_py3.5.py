#!/usr/bin/python

# searchString = input from command line argv[0]
# finalUrl = "http://www.dict.org/bin/Dict?Form=Dict1&Query=" + searchString + "&Strategy=*&Database=*";//"http://dict.cn/mini.php?q=" + searchString;
# htmlString = getStringFromUrl(finalUrl);
# textString = html2text(htmlString);
# print textString;

import urllib
import urllib.request
import html2text
import os, sys

search = 'search'
link = "http://www.dict.org/bin/Dict?Form=Dict1&Query=" + search + "&Strategy=*&Database=*";
#"http://dict.cn/mini.php?q=" + searchString
f = urllib.request.urlopen(link)

# very important, byte by utf-8 
myfile = f.read()
myfileStr = myfile.decode('utf-8')

# Open a file
fd = os.open( "foo.txt", os.O_RDWR|os.O_CREAT )

# Write one string
os.write(fd, myfile)

# Close opened file
os.close( fd )

# want to filter 

print(html2text.html2text(myfileStr))


