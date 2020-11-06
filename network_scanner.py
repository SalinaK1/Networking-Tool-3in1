import scapy.all as scapy
import argparse
from scapy.layers.inet import IP, ICMP

def get_argument():
    parser= argparse.ArgumentParser()
    parser.add_argument('-t','--target',dest ='target', help='Target IP address/range.')
    argument = parser.parse_args()
    print("1")
    print(argument.target)

    if not argument.target:   #Check for errors i.e if the user does not specify the target IP Address
        parser.error("[-] Please specify target IP address/ range. Use --help for more information.")       #Display the error mesage and quit the program if the argument is missing.
        print("2")
    return argument


target = get_argument()
print("3")
print (target)
