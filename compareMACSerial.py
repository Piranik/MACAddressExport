import sys

def main():

    mac_addresses = sys.argv
    i = 0
    for address in mac_addresses:
    	print(address + " Device" + str(i))
    	i += 1








if __name__ == '__main__':
  main()
