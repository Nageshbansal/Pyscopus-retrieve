from lxml import etree


parser = etree.XMLParser(ns_clean=True)
with open('response.xml','rb') as f :
    tree  = etree.parse(f,parser)

root = tree.getroot()
print(root)

# E = "/e:full-text-retrieval-response"
# ART = "*[self::ja:converted-article or self::ja:article]"

# CE = "http://www.elsevier.com/xml/common/dtd"
# TAG = "{%s}%%s" % CE
# XREFS = {TAG % "cross-ref", TAG % "cross-refs"}
# ITALIC = {TAG % "italic"}

print(root.nsmap)