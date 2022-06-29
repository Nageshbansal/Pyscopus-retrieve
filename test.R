library(XML)

doc = xmlTreeParse('response.xml', useInternalNodes = TRUE)
top = xmlRoot(doc)
xmlName(top)
names(top)
ack = names(top[[6]][["doc"]][["serial-item"]][["article"]][["body"]][["acknowledgment"]])

ack_xmls = xmlSApply(top[[6]][["doc"]][["serial-item"]][["article"]][["body"]][["acknowledgment"]][['para']], xmlValue)
ack_xmls
