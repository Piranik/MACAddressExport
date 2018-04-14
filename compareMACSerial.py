import sys
import xml.etree.ElementTree as ET

def main():
    mac_addresses = sys.argv
    for address in mac_addresses:
    	print(address)

def generateReport(): #Prints report (NEED TO CONVERT TO RETURN MULTILINE STR) 
	i = 0
	for device in root:
		if device[3].text == 'true':
			i += 1
			print
			print("-----------------[Device Number " + str(i) + "]----------------")
			print("MAC Address---------: " + device[0].text)
			print("Serial Number-------: " + device[1].text)
			print("Date last Checked in: " + device[2].text)
			print("--------------------------------------------------")
			print



tree = ET.parse('studentObjects.xml')
root = tree.getroot()


if __name__ == '__main__':
  main()

generateReport()

print("compareMACSerial.py complete")