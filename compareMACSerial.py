import sys
import xml.etree.ElementTree as ET
import datetime

def main():
	tree = ET.parse('studentObjects.xml')
	root = tree.getroot()
	known_devices_updated = 0
	mac_addresses = sys.argv
	mac_addresses.pop(0)
	for address in mac_addresses:
		is_foreign = True
		for device in root.iter('device'):
			if address == device[0].text:
				device[2].text = str(datetime.datetime.now())
				known_devices_updated += 1
				is_foreign = False
		if is_foreign:
			print(address)
			new_device = ET.Element('device')
			ET.SubElement(new_device, 'address')
			ET.SubElement(new_device, 'serial')
			ET.SubElement(new_device, 'date_last_checked')
			new_device[0].text = address
			new_device[1].text = 'UNKNOWN'
			new_device[2].text = str(datetime.datetime.now())
			root.append(new_device)
		

	print('Known Devices Updated: ' + str(known_devices_updated))
	print('Foreign Devices Identified: ' + str(len(mac_addresses) - known_devices_updated))
	tree.write('studentObjects.xml')

print('===================REPORT======================')
print('Added devices:')
if __name__ == '__main__':
  main()
print('=================END_REPORT====================')
print("compareMACSerial.py complete")
