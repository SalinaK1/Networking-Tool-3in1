def packet_testing(ip = "8.8.8.8"):
    import scapy.all as scapy
    from scapy.layers.inet import IP, ICMP

    alive_packets = 0
    dead_packets= 0
    packets_sent = 10

    for i in range(0,packets_sent):
        packet = IP(dst = str(ip), ttl = 2) / ICMP()
        response = scapy.sr1(packet, timeout = 1, verbose = False)
        if response is not None:
            alive_packets +=1
        else:
            dead_packets +=1

    print(f"Total {packets_sent} packets were sent to {ip}.")
    print(f"{alive_packets} are recieved.")
    print(f"{dead_packets} are lost.")
    ratio = (dead_packets)*100/(alive_packets + dead_packets)
    print(f"The packet loss is {ratio}%")

# packet_testing()