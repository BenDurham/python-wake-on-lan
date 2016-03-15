import xml.etree.cElementTree as ET
import socket

#Host Manager

class HostManager(object):
	"""docstring for HostManager"""
	def __init__(self, arg):
		super(HostManager, self).__init__()
		self.arg = arg
		
	def set_broadcast_address():
		root = ET.Element("config")
		doc = ET.SubElement(root, "broadcast")

		ip_address = raw_input("Input subnet broadcast IP address: ")

		try:
			ET.SubElement(doc, "address").text = ip_address	

			tree = ET.ElementTree(root)
			tree.write("config.xml")
		except:
			print 'Unable to write to config.xml, check folder/file permissions'
			return

	def get_broadcast_address():
		root = ET.parse('config.xml').getroot()
		try:
			address = root.find("broadcast").find("address").text
			print("Current broadcast address: "+address)
		except:
			print 'Unable to find broadcast address. Check config.xml or enter new broadcast address'

	def delete_host():
		# root = ET.parse('config.xml').getroot()
		# .set()
		pass

	def edit_host():
		list_hosts()
		identifier = raw_input('Enter the host name to edit: ')
		tree = ET.parse('config.xml')

		for host in tree.iterfind('host/alias'):
			if host.text == identifier:
				option = raw_input('Which would you like to edit? \n 1. Host alias \n 2. Host MAC address \n Input your option: ')
				if option == '1':
					try:
						new_alias = raw_input('Define a new alias: ')
						host.text = new_alias
						tree.write("config.xml")
					except:
						print 'Failed to upadate host.'
				elif option == '2':
					try:
						new_address = raw_input('Define a new MAC address: ')
						host.text = new_address
						tree.write("config.xml")
					except:
						print 'Failed to upadate host.'
				else:
					print 'Sorry, that option was not recognized. Please try again'
					edit_host()

	def create_host():
		alias = raw_input("Input desired alias: ")
		mac_address = raw_input("Input MAC address: ")

		try:
			tree = ET.parse("config.xml")

			xmlRoot = tree.getroot()
			child = ET.Element("host")
			ET.SubElement(child, "alias").text = alias
			ET.SubElement(child, "address").text = mac_address
			xmlRoot.append(child)

			tree.write("config.xml")
		except:
			print 'Unable to write to config.xml, check folder/file permissions'
			return

	def list_hosts():
		#Print all hosts saved in config
		root = ET.parse('config.xml').getroot()

		for host in root.findall('host'):
			alias = host.find('alias').text
			address = host.find('address').text
			print alias, address

	def find_host():
		# raw_input('enter host name')
		pass

	def find_my_ip():
		#IPV4 sockets, UPD datagram for finding host
		soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		soc.connect(("gmail.com",80))
		print(soc.getsockname()[0])
		soc.close()

	function_dict = {'1':list_hosts, '2':find_host, '3':create_host, '4':edit_host, '5':delete_host, '6':get_broadcast_address, '7':set_broadcast_address}
	function_list = ['1: List current hosts','2: Find a host', '3: Create a host', '4: Edit a host', '5: Delete a host', '6: Get broadcast address', '7: Set the broadcast address']

	for value in function_list:
		print value

user_selection = raw_input('Please select an option >> ')
function_dict[user_selection]()