import scapy.all as scapy
import argparse
from scapy.layers.inet import IP, ICMP

def get_argument():     #get the target IP or IP range that are needed to be scanned as argument.
    parser = argparse.ArgumentParser()
    parser.add_argument('-t','--target',dest ='target', help='Target IP address/range.')
    argument = parser.parse_args()
    # print(argument.target)

    if not argument.target:   #Check for errors i.e if the user does not specify the target IP Address
        parser.error("[-] Please specify target IP address/ range. Use --help for more information.")       #Display the error mesage and quit the program if the argument is missing.
    return argument

def create_packet(ip):      # create packets to send.
    arp_request = scapy.ARP(pdst = ip)      #creates a scapy ARP request object 
    broadcast_ether = scapy.Ether( dst = "ff:ff:ff:ff")        #broadcast the Ethernet frame.
    ether_arp_frame = broadcast_ether / arp_request
    return ether_arp_frame

def send_packet(packet):        # send ARP request and recieve response.
    response_list = scapy.srp(packet, timeout = 2, verbose = False )[0]     # the first element has all the answered response list. 
    return (response_list)

def parse_response(response_list):      #parse the response of our previous ARP request and extract its IP address and MAC address only.
    result = []
    for response in response_list:
        device = {"ip" : response[1].psrc, "mac" : response[1].hwsrc}
        result.append(device)
    return result

def display_result(result):
    print("------------------------------------------")
    print("| IP\t\t| MAC \t\t\t |")
    print("------------------------------------------")
    for device in result:
        print("| " + device["ip"] + "\t| " + device["mac"] + "\t\t\t  |\n")

target_IP = get_argument()
# print (target_IP)
if target_IP.target is not None:
    packet = create_packet(target_IP)
    response_packets = send_packet(packet)
    result_devices = parse_response(response_packets)
    display_result(result_devices)
