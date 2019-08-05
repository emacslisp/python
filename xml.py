import lxml.etree as etree
FileName = '/Users/di.wu/test/2.xml';
x = etree.parse("/Users/di.wu/test/1.xml");
with open(FileName, "w") as f:
    f.write(etree.tostring(x, pretty_print=True).decode('utf-8'))
print('DONE');
