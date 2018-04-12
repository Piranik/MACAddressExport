import sys
import xml.etree.ElementTree as ET

def main():

    mac_addresses = sys.argv
    i = 0
    for address in mac_addresses:
    	print(address + " Device" + str(i))
    	i += 1




tree = ET.parse('studentObjects.xml')
root = tree.getroot()



if __name__ == '__main__':
  main()



print(root)