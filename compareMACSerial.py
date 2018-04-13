import sys
import xml.etree.ElementTree as ET

def main():

    mac_addresses = sys.argv




tree = ET.parse('/Users/walkersorensen/Dropbox/MACAddressExport/studentObjects.xml')
root = tree.getroot()
i = 0
for child in root:
	i += 1
	print
	print("--------------------[Device Number " + str(i) + "]--------------------")
	print("MAC Address---------:", child[0].text)
	print("Serial Number-------:", child[1].text)
	print("Date last Checked in:", child[2].text)
	print("---------------------------------------------------------")

if __name__ == '__main__':
  main()



