import sys, struct, socket

''' 
Wake on Lan for SleePy computers
'''

# Configuration variables
broadcast = ['192.168.1.255']
udp_port = 9

# Soon to be replaced with call to ReadConfig.py to extend functionality
known_computers = {
    'polaris'    : '00:00:00:00:00:00',
    'office1'    : '00:00:00:00:00:00',
    'office2'    : '00:00:00:00:00:00',
    'finance'    : '00:00:00:00:00:00'
}

def WakeOnLan(ethernet_address):

    # Construct 6 byte hardware address
    add_oct = ethernet_address.split(':')
    if len(add_oct) != 6:
        print "\n*** Invalid MAC address\n"
        print "Please reformat the MAC address, it should resemble this: 00:11:22:33:44:55\n"
        return
    hwa = struct.pack('BBBBBB', int(add_oct[0],16),
        int(add_oct[1],16),
        int(add_oct[2],16),
        int(add_oct[3],16),
        int(add_oct[4],16),
        int(add_oct[5],16))

    # Build magic packet

    msg = '\xff' * 6 + hwa * 16

    # Send packet to broadcast address using UDP port 9

    soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    soc.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST,1)
    for i in broadcast:
        soc.sendto(msg,(i,udp_port))
    soc.close()

def wol(*macs):
    if len(macs) == 0:
        print "\n*** No computer given to power up\n"
        print "Use: 'wol computername' or 'wol 00:11:22:33:44:55'"
    else:
        for i in macs:
            if i[0] != '/':
                # Check for colon in string to suggest MAC address formating
                if ":" in i:
                    # Wake up using MAC address
                    WakeOnLan(i)
                else:
                    # Wake up known computers
                    if i in known_computers:
                        WakeOnLan(known_computers[i])
                    else:
                        print "\n*** Unknown computer " + i + "\n"
                        quit()

        if len(macs) == 2:
            print "\nDone! The computer should be up and running in a short while."
        else:
            print "\nDone! The computers should be up and running in a short while."
        print

wol(input('Enter MAC address or known host name: '))