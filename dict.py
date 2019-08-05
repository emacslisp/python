#!/usr/bin/python

# searchString = input from command line argv[0]
# finalUrl = "http://www.dict.org/bin/Dict?Form=Dict1&Query=" + searchString + "&Strategy=*&Database=*";//"http://dict.cn/mini.php?q=" + searchString;
# htmlString = getStringFromUrl(finalUrl);
# textString = html2text(htmlString);
# print textString;

import urllib.request
search = 'search'
link = "http://www.dict.org/bin/Dict?Form=Dict1&Query=" + search + "&Strategy=*&Database=*";
#"http://dict.cn/mini.php?q=" + searchString
f = urllib.request.urlopen(link)           
myfile = f.read()  
print(myfile)
