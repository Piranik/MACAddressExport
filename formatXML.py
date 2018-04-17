from xml.dom.minidom import parse, parseString
file = open('studentObjects.xml', 'r')
string = ""
for line in file:
	string += line.strip()
dom = parseString(string)
file.close()
file = open('studentObjects.xml', 'w')
file.truncate()
file.write(dom.toprettyxml())