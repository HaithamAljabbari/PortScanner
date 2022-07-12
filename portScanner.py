import socket
from termcolor import cprint
import pyfiglet
import argparse
from IPy import IP

parser = argparse.ArgumentParser()

parser.add_argument("--ip", help="IP/DNSNAME")
parser.add_argument("-p", "--port", help="numbers of ports")
args = parser.parse_args()

title = pyfiglet.figlet_format("SOSAKORNUT")
cprint(title, "cyan", "on_blue")

def dnstoip(ip):
    try:
        IP(ip)
        return ip
    except ValueError:
        return socket.gethostbyname(ip)

if args.ip:
    ip_address = dnstoip(args.ip)

if args.port:
    ports = int(args.port)

cprint("Scanning for ports", "cyan", "on_grey")
for i in range(0, ports):
    try:
        s = socket.socket()
        s.connect((ip_address, i))
        #s.settimeout(5)
        cprint(f"port {i} is open", "green")
    except:
        pass
   




