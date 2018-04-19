import xml.etree.ElementTree as ET

def getDashLength(device, i): # Used to make lists of devices human readable
	number_of_dashes_needed = 17 - len(device[0].text)
	if i >= 10:
		number_of_dashes_needed += 1
	elif i >= 100:
		number_of_dashes_needed += 1
	dash_text = '---------'
	while number_of_dashes_needed != 0:
		dash_text += '-'
		number_of_dashes_needed -= 1
	return dash_text

def unknownDevicesConfig(): # Display unset devices for organization & formatting
	print('Displaying unknown MAC addresses')
	mac_addresses = []
	for device in root:
		if device[1].text == 'UNKNOWN':
			mac_addresses.append(device[0].text)
	i = 0
	for address in mac_addresses:
		i += 1
		print( str(i) + '. ' + address)
	print('Input the number correlated with your MAC Address you want to configure')
	user_index = input() - 1
	print('Selected MAC Address:' + mac_addresses[user_index])
	print('What should the serial # for this address be?')
	user_serial = raw_input()
	print('Your input: ' + user_serial)
	print('Overwrite current address? [y/n]')

	if raw_input() == 'y':
		for device in root:
			if device[0].text == mac_addresses[user_index]:
				device[1].text = user_serial
				tree.write('studentObjects.xml')

def knownDevicesConfig(): # Display set devices for organization & formatting
	print('Displaying known Devices')
	i = 0
	device_index = []
	for device in root:
		if device[1].text != 'UNKNOWN':
			i += 1
			device_index.append(device[0].text)
			print(str(i) + '. ' + device[0].text + getDashLength(device, i) + device[1].text)

	print('Input the number correlated with your MAC Address you want to configure')
	user_index = input() - 1
	print('Selected device: ' + device_index[user_index])
	print('What should the serial # for this address be?')
	user_serial = raw_input()
	print('Your input: ' + user_serial)
	print('Overwrite current address? [y/n]')

	if raw_input() == 'y':
		for device in root:
			if device[0].text == device_index[user_index]:
				device[1].text = user_serial
				tree.write('studentObjects.xml')
				

print('Configuration program initilized')
tree = ET.parse('studentObjects.xml')
root = tree.getroot()

print('Configure [1. known] or [2. unknown] addresses?')
menu_option_1 = input()
if menu_option_1 == 1 or menu_option_1 == 'known':
	knownDevicesConfig()
elif menu_option_1 == 2 or menu_option_1 == 'unknown':
	unknownDevicesConfig()






